#include <iostream>
using namespace std;

const int maxN = 2048;
string s[maxN];
bool in[maxN];

int doit(){
  int i, j, sl, pl, res = 0, jp;
  string str;
  bool fl;
  cin >> sl;
  memset(in, 0, sizeof(in));
  for(i = 0; i < sl; i++) s[i].clear();
  getline(cin, str);
  for(i = 0; i < sl; i++) getline(cin, s[i]);
  
  cin >> pl;
  getline(cin, str);
  for(i = 0; i < pl; i++){
    jp = -1;
    getline(cin, str);
    for(j = 0; j < sl; j++)
    if(str == s[j]){
      in[j] = true;
      jp = j;
      break;
    }
    if(i < pl){
      fl = true;
      for(j = 0; j < sl; j++) if(!in[j]){fl = false; break;}
      if(fl){
        //cout << str << endl;
        res ++;
        memset(in, 0, sizeof(in));
        if(jp != -1) in[jp] = true;
      }
    }
  }
  return res;
}

int main(){
  int tst, tc;
  cin >> tst;
  for(tc = 1; tc <= tst; tc++){
    cout << "Case #" << tc << ": " << doit() << endl;
  }
  return 0;
}
