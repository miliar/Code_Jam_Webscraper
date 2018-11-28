#include<cstdio>
#include<iostream>
using namespace std;
int t,L,D,N;
bool ok[300][300];
string s[10000];
main(){
  cin>>L>>D>>N;
  for(int i=0;i<D;i++)cin>>s[i];
  for(int tt=1;tt<=N;tt++){
    int cnt=0;
    string cur;
    cin>>cur;
    memset(ok,0,sizeof(ok));
    int pos=0;
    for(int i=0;i<L;i++)if(cur[pos]=='('){
      pos++;
      while(cur[pos]!=')')ok[i][cur[pos++]]=1;
      pos++;
    }else ok[i][cur[pos++]]=1;
    for(int i=0;i<D;i++){
      bool found=1;
      for(int j=0;j<L;j++)found&=ok[j][s[i][j]];
      cnt+=found; 
    }
    cout<<"Case #"<<tt<<": "<<cnt<<endl;
  }
}
