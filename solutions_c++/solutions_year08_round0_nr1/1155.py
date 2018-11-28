#include <iostream>
#include <vector>

#define REP(i,e) for(int i=0;i<(int)(e);i++)
using namespace std;

int compute(vector<string> &s,vector<string> &q){
  bool used[s.size()];
  REP(i,s.size()) used[i]=false;
  int uct=0;
  int result=0;

  REP(i,q.size()){
    int n=distance(s.begin(),find(s.begin(),s.end(),q[i]));
    if (!used[n]){
      if (uct==s.size()-1){
	result++;
	uct=1;
	REP(j,s.size()) used[j]=false;
	used[n]=true;
      }
      else {
	used[n]=true;
	uct++;
      }
    }
  }
  return result;
}

main(){
  int ct;
  cin >> ct;
  REP(c,ct){
    cout << "Case #" << c+1 << ": " ;
    int sn,qn;

    vector<string> s,q;
    string line;

    cin >> sn;
    getline(cin,line);
    while(sn--)getline(cin,line),s.push_back(line);
    cin >> qn;
    getline(cin,line);
    while(qn--)getline(cin,line),q.push_back(line);

    cout << compute(s,q) << endl;
  }
}
