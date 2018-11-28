#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
char buf[10000];
string p="welcome to code jam",s;
int N,a[600][600];
main(){
  gets(buf);
  sscanf(buf,"%d",&N);
  for(int t=1;t<=N;t++){
    gets(buf);
    s=buf;
    memset(a,0,sizeof(a));
    a[s.size()][p.size()]=1;
    for(int i=s.size()-1;i>=0;i--){
       a[i][p.size()]=1;
       for(int j=0;j<p.size();j++)a[i][j]=s[i]==p[j]?(a[i+1][j+1]+a[i+1][j])%10000:a[i+1][j];
    }
    printf("Case #%d: %04d\n",t,a[0][0]);
  }
}
