#include<iostream>
#include<fstream>
#include<cmath>
#include<vector>
using namespace std;

long long MoneyMade(long long R, long long k, vector<long long> g)
{
  long long money = 0;
  vector<long long> allsums;
  vector<long long> sums_end_idx;
  int sum = 0;
  int i = 0;
  for(i=0; i < g.size(); i++) {
    sum+=g[i];
    if(sum > k) {
      sum-=g[i];
      i--;
      break;
    }
  }
  allsums.push_back(sum);
  sums_end_idx.push_back(i==g.size()? i-1:i);
  for(int j = 1; j < g.size(); j++) {
    int endidx = 0;
    int cursum = allsums[j-1]-g[j-1];
    while(cursum <= k && endidx < g.size()) {
      endidx++;
      cursum += g[(sums_end_idx[j-1]+endidx)%g.size()];
    }
    if(cursum > k) {
      cursum -= g[(sums_end_idx[j-1]+endidx)%g.size()];
      endidx--;
    }
    if(endidx == g.size()) endidx--;
    
    allsums.push_back(cursum);
    sums_end_idx.push_back((sums_end_idx[j-1]+endidx)%g.size());
    
  }
  int curidx = 0;
  for(int counter = 0; counter < R; counter++) {
    money += allsums[curidx];
    curidx = (sums_end_idx[curidx]+1)%g.size();
  }

  return money;
}
long long MoneyMadeBF(long long R, long long k, vector<long long> g) {
  long long money = 0;
  long long money_this_round = 0;
  int j = 0;
  for(int i = 0; i < R; i++) {
    money_this_round = 0;
    int p = 0;
    for(p = 0; p < g.size(); p++) {
      long long cursum = money_this_round + g[(j+p)%g.size()];
      if(cursum <= k) {
	money_this_round = cursum;
      } else {
	j = (j+p)%g.size();
	break;
      }
    }
    money += money_this_round;
  }
  return money;
}
template<class T> 
void ShowVector(vector<T> showme, string startstr = "", string endstr = "")
{
  cout << startstr << endl;
  for(int i = 0; i < showme.size(); i++) {
    cout << showme[i] << endl;
  }
  cout << endstr << endl;
}

int main(int argc, char *argv[])
{
  if(argc < 2) return -1;
  ifstream infile(argv[1]);
  
  int numtests = 0;
  infile >> numtests;
  char inputstring[501];
  infile.getline(inputstring, 501);
  for(int test_idx = 0; test_idx < numtests; test_idx++) {

    /*******************/
    long long R, k, N;
    infile >> R;
    infile >> k;
    infile >> N;
    infile.getline(inputstring, 501);
    vector<long long> g(N);
    for(int i = 0; i < N; i++) {
      infile >> g[i];
    }
    infile.getline(inputstring, 501);

    /*******************/
    // Process data
    
    // Output relevant data.
    //cout << "Case #" << (test_idx+1) << ": " << MoneyMadeBF(R,k,g);
    cout << "Case #" << (test_idx+1) << ": " << MoneyMade(R,k,g);
    // Terminate output properly.
    cout << endl;
  }

  return 0;
}
