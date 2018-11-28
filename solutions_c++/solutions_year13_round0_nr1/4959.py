#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>

#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int n,cont;
string b[5];

int f(char chr){
  int cnt = 0;
  
  rep(i,4){
    cnt = 0;
    rep(j,4)cnt+=(b[i][j]==chr || b[i][j]=='T');
    if(cnt==4)return 1;
  }
  rep(i,4){
    cnt = 0;
    rep(j,4)cnt+=(b[j][i]==chr || b[j][i]=='T');
    if(cnt==4)return 1;
  }

  cnt = 0; rep(i,4)cnt+=(b[i][i]==chr || b[i][i]=='T');
  if(cnt==4)return 1;

  cnt = 0; rep(i,4)cnt+=(b[i][3-i]==chr || b[i][3-i]=='T');
  if(cnt==4)return 1;

  return 0;


}

int main(){
  cin>>n;

  rep(i,n){
    cont = 0;

    cout<<"Case #"<<i+1<<": ";

    rep(i,4)cin>>b[i];
    if(f('O')){
      cout<<"O won"<<endl;
      continue;
    }
    else if(f('X')){
      cout<<"X won"<<endl;
      continue;
    }
    rep(i,4)rep(j,4)if(b[i][j]=='.')cont=1;
    cout<<(cont?"Game has not completed":"Draw")<<endl;
  }
  
}
