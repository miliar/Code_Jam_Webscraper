#include <iostream>
#include <string>
#include <cstring>
using namespace std;

bool hash[15][26];
string words[5000];

int main(){
  int L,D,N;
  cin >> L >> D >> N;
  for (int i=0;i<D;i++){
    cin >> words[i];
  }
  for (int i=0;i<N;i++){
    memset(hash,false,sizeof(hash));
    int ans = 0;
    string str;
    cin >> str;
    int pr=0;
    bool flag=false;
    for (int j=0;j<(int)str.size();j++){
      if (str[j]=='('){
        flag = true;
      }else if (str[j]==')'){
        pr++;
        flag = false;
      }else{
        hash[pr][str[j]-'a'] = true;
        if (!flag) pr++;
      }
    }
    for (int j=0;j<D;j++){
      bool ok = true;
      for (int k=0;k<L;k++){
        if (hash[k][words[j][k]-'a']) continue;
        ok = false;
        break;
      }
      //if (ok) cout << "ok" <<" "  <<  words[j] << endl;
      if (ok) ans++;
    }
    printf("Case #%d: %d\n",i+1,ans);
  }
}
