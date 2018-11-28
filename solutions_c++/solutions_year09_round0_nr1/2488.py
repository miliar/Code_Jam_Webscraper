#include <iostream>
#include <vector>
using namespace std;

vector<string> dic;
int mmm;

void rec(string tmp, string str, int L, int len, int i){
  if(L == len){
    //cout << " " << tmp << endl;
    for(int j=0; j<dic.size(); j++){
      if(dic[j]==tmp){ mmm++; return; }
    }
    return;
  }
  if(str[i]=='('){
    int t=i;
    bool flg;
    while(str[t]!=')') t++;
    for(int j=i+1; j<t; j++){
      flg = false;
      for(int k=0; k<dic.size(); k++){
	//cout << tmp+str[j] << "  " << dic[k].substr(0, len+1) << endl;
	if((tmp+str[j])==dic[k].substr(0, len+1)){ flg = true; break; }
      }
      if(flg) rec(tmp+str[j], str, L, len+1, t+1);
    }
  }else{
    rec(tmp+str[i], str, L, len+1, i+1);
  }
}


int check(int L, string str){
  mmm = 0;
  rec("", str, L, 0, 0);
  return mmm;
}

int main(){
  int L, D, N;
  string str;
  while(cin >> L >> D >> N){
    dic.clear();
    for(int i=0; i<D; i++){
      cin >> str;
      dic.push_back(str);
    }
    int cases = 1;
    for(int i=0; i<N; i++){
      cin >> str;
      cout << "Case #" << cases++ << ": " << check(L, str) << endl;
    }
  }
  return 0;
}
