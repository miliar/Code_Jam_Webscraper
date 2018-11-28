#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<cctype>
using namespace std;
#define inf 1e100
#define eps 1e-6
template<class T> void chkmax(T&a,T b){if(a<b)a=b;}
template<class T> void chkmin(T&a,T b){if(a>b)a=b;}



int m[1025];
bool vis[11][1025];
int rec[11];

int n;
int main(){
  int Cas,ca=0;
  scanf("%d",&Cas);
  while(Cas--){
    int i,k,j,p,nn,t;
    scanf("%d",&p);
    n=(1<<p);
    for(i=0;i<n;++i)scanf("%d",m+i);
    for(k=0,nn=(n>>1);nn>0;nn>>=1){
      for(i=0;i<nn;++i)scanf("%d",&t);
    }

    memset(vis,0,sizeof(vis));
    int ans=0;
    for(i=0;i<n;++i){
      int x=m[i];
      int cnt=0;
      //printf("%d:\n",i);
      for(k=0,nn=(n>>1),t=i/2;nn>0;nn>>=1,++k,t/=2){
        cnt+=vis[k][t];
        rec[k]=t;
        //printf("(%d,%d) ",k,t);
      }
      //putchar(10);
      int needed=p-x-cnt;
      //printf("%d:%d %d %d %d| %d\n",i,p,x,cnt,needed,ans);
      for(k=p-1,nn=1;needed>0 && nn<n;nn<<=1,--k){
        t=rec[k];
        if(vis[k][t]==false){
          needed--;
          vis[k][t]=true;
          ans++;
        }
      }
    }
    printf("Case #%d: %d\n",++ca,ans);
  }
  return 0;
}
