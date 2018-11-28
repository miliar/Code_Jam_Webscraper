#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<sstream>

using namespace std;


unsigned int next_num(int v, const int base){
  int nv = 0;
  while(v>1){
    nv += (v%base)*(v%base);
    v /= base;
  }
  nv += v;
  return nv;
}
int solve(unsigned int st_v, const int base){
  vector<unsigned int> stk;
  bool flg;
  if(base == 2) return true;
  unsigned int v = st_v;
  unsigned int v2 = next_num(v, base);
  while(1){
    //    cout << st_v << "  " << v << " " << v2 << endl; 
    if(v == 1) return true;
    if(v == v2) return false;
    v = next_num(v, base);
    v2 = next_num(next_num(v2, base), base);
  }
}
int main(){
  int T; cin >> T; 
  string ns; getline(cin, ns);
  for(int i = 1;i<=T;++i){
    //    cout << i << endl;
    vector<int> bases;
    string line;  getline(cin, line);
    istringstream iss(line);
    int v;
    while(iss>>v) bases.push_back(v);
    int K=0;
    for(int v=2;v<500000000;++v){
      for(int i=0;i<bases.size();++i){
	if(!solve(v, bases[i])){
	  goto next;
	}
      }
      K = v;
      break;
    next:;
    }
    cout << "Case #" <<  i <<  ": " << K << endl;;
  }
}
