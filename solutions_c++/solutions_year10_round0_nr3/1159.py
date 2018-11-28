#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
using namespace std;

int coasters(int R, int k, const vector<int> &groups){
  int result=0;
  int sidx=0;
  for(int r=0;r<R;r++){
    int ride=0;
    int gidx = sidx;
    do {
      ride += groups[gidx];
      gidx = (gidx+1) % groups.size();
    }while((ride + groups[gidx]) <= k && sidx != gidx);
    sidx = gidx;
    result += ride;
  }
  return result;
}


int main()
{
  string line;
  int T;
  getline(cin, line);
  istringstream fiss(line);
  fiss >> T;

  for(int i=0;i<T;i++){
    int R,k,N;
    getline(cin, line);
    istringstream paramline(line);
    paramline >> R;
    paramline >> k;
    paramline >> N;

    vector<int> groups;
    getline(cin, line);
    istringstream groupline(line);
    for(int g=0;g<N;g++){
      int gnum;
      groupline >> gnum;
      groups.push_back(gnum);
    }
    
    int paid = coasters(R, k, groups);
    
    cout << "Case #" << i+1 << ": " << paid << endl;    
  }
  return 0;
}
