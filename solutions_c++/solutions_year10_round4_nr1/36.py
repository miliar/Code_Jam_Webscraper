#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

#define INF 1000000000
int r,s;
bool h[110],v[110];
char buf[1000],t[110][110];
inline char get(int x,int y){
  return x<0||y<0||x>=110||y>=110?' ':t[x][y];
}
inline bool ok(char a,char b){
  return a==' '||b==' '||a==b;
}
main(){
  int C;
  gets(buf);
  sscanf(buf,"%d",&C);
  for(int c=1;c<=C;c++){
    gets(buf);
    sscanf(buf,"%d",&s);
    memset(t,' ',sizeof(t));
    for(int i=0;i<2*s-1;i++){
      gets(buf);
      for(int j=0;buf[j];j++)t[i][j]=buf[j];
    }
    r=INF;
    memset(h,1,sizeof(h));
    memset(v,1,sizeof(v));
    for(int k=0;k<110;k++)for(int i=0;i<110;i++)for(int j=0;j<110;j++)h[k]&=ok(get(i,j),get(2*k-i,j));
    for(int k=0;k<110;k++)for(int i=0;i<110;i++)for(int j=0;j<110;j++)v[k]&=ok(get(i,j),get(i,2*k-j));
    for(int i=0;i<110;i++)if(h[i])for(int j=0;j<110;j++)if(v[j]){
      int m=0;
      for(int x=0;x<110;x++)for(int y=0;y<110;y++)if(get(x,y)!=' ')m>?=abs(i-x)+abs(j-y);
      bool odd=false,even=false;
      for(int x=0;x<110;x++)for(int y=0;y<110;y++)if(get(x,y)!=' '){
        even|=(i-x+j-y)%2==0;
        odd|=(i-x+j-y)%2==1;
      }
      if(odd&&even)continue;
      if(odd&&m%2==0)m++;
      if(even&&m%2==1)m++;
      r<?=(m+1)*(m+1);
    }
    cout<<"Case #"<<c<<": "<<r-s*s<<endl;
  }
}
