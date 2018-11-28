#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<vector>
#include<cctype>
using namespace std;
#define inf 0x7ffffff
#define eps 1e-6
template<class T> void chkmax(T&a,T b){if(a<b)a=b;}
template<class T> void chkmin(T&a,T b){if(a>b)a=b;}



int xn=220,yn=220;
int mp[550][550];
int main(){
  int Cas,ca=0;
  scanf("%d",&Cas);
  while(Cas--){
    int n,i,j;
    int xx,yy,x,y;
    scanf("%d",&n);
    int bx=110,by=110;
    int l=1;
    int det=1;
    x=-n+1;
    memset(mp,-1,sizeof(mp));
    for(;l>0;l+=det,x++){
      int y=-l+1;
      for(i=0;i<l;++i,y+=2){
        scanf("%d",mp[bx+x]+by+y);
      }
      if(l==n)det=-det;
    }
    /*
    for(i=17;i<25;++i){
      for(j=17;j<25;++j){
        if(mp[i][j]>=0)printf("%d",mp[i][j]);
        else putchar(32);
      }
      putchar(10);
    }
    */

    int ans=inf;
    for(xx=bx-n+1;xx<bx+n;++xx){
      for(yy=by-n+1;yy<by+n;++yy){
        bool ok=true;
        for(x=bx-n+1;ok && x<bx+n;++x){
          for(y=by-n+1;ok && y<by+n;++y){
            int cx=xx+xx-x,cy=y;
            if(mp[x][y]>=0 && mp[cx][cy]>=0 && mp[x][y]!=mp[cx][cy])ok=false;
          }
        }
        for(x=bx-n+1;ok && x<bx+n;++x){
          for(y=by-n+1;ok && y<by+n;++y){
            int cx=x,cy=yy+yy-y;
            if(mp[x][y]>=0 && mp[cx][cy]>=0 && mp[x][y]!=mp[cx][cy])ok=false;
          }
        }
        if(!ok)continue;
        int mx=0;
        for(x=bx-n+1;x<bx+n;++x){
          for(y=by-n+1;y<by+n;++y){
            if(mp[x][y]>=0){
              chkmax(mx,abs(x-xx)+abs(y-yy)+1);
            }
          }
        }
        chkmin(ans,mx*mx-n*n);
        //printf("%d %d %d\n",xx-bx,yy-by,mx);
      }
    }
    printf("Case #%d: %d\n",++ca,ans);
    fprintf(stderr,"%d\n",ca);
  }
  return 0;
}
