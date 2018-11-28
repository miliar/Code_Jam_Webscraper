#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

int mysqrt(int r, int base){
  ll ret = 0, tmp;
  while(true){
    tmp = r%base;
    r = r/base;
    ret += tmp*tmp;
    if(r<base) break;
  }
  return (int)(ret+r*r);
}

bool ishappy(int n, int base){
  bool checked[100000];
  for(int i=0; i<100000; i++) checked[i] = false;
  int ret = n;
  while(ret != 1){
    ret = mysqrt(ret, base);
    if(!checked[ret]) checked[ret] = true;
    else return false;
  }
  return true;
}

int calc(vector<int> v){
  bool flg;
  for(int n=2; n<100000; n++){
    flg = true;
    for(int i=0; i<v.size(); i++){
      if(flg)
	if(ishappy(n, v[i])==false) flg = false;
    }
    if(flg) return n;
  }
  return 0;
}

int main(){
  int T;
  string str;
  vector<int> v;
  cin >> T;
  cin.get();
  for(int i=0; i<T; i++){
    v.clear();
    getline(cin, str);
    for(int j=0; j<str.length(); j++){
      if(str[j]!=' ' && str[j]!='0'){
	if(str[j]=='1') v.push_back(10);
	else v.push_back((int)(str[j]-'0'));
      }
    }
    cout << "Case #" << i+1 << ": " << calc(v) << endl;
  }
  return 0;
}
