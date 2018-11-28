#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;
int hi[2010];
int n;
int to[2010];
const int INF=1000000000;
inline int mh(int l,long long lh,int r,long long rh,int x,bool d1=0){
    long long q=lh*(r-x)+rh*(x-l);
    long long w=r-l;
    long long s=q/w;
    if(q%w==0&&d1)s--;
    return s;
}
int tmp[2010];
inline void run(int x,int y){
    if(x+1==y)return;
    int lh=hi[x],rh=hi[y];
    int np=x+1,tc=0;
    while(np<y){
        tmp[tc++]=np;
        if(to[np]>y)throw 514;
        np=to[np];
    }
    hi[tmp[tc-1]]=mh(x,lh,y,rh,tmp[tc-1],1);
    for(int i=tc-2;i>=0;i--){
        hi[tmp[i]]=mh(tmp[i+1],hi[tmp[i+1]],y,rh,tmp[i],0);
    }
    np=x+1;
    while(np<y){
        run(np,to[np]);
        np=to[np];
    }
}
inline bool solve(){
    scanf("%d",&n);
    int i,j;
    for(i=1;i<n;i++)scanf("%d",&to[i]);
    int np=1;
    while(np<n){
        hi[np]=INF;
        np=to[np];
    }
    hi[n]=INF;
    np=1;
    try{
        while(np<n){
            run(np,to[np]);
            np=to[np];
        }
    }catch(...){
        return 0;
    }
    return 1;
}
int main(){
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        printf("Case #%d: ",cas++);
        if(solve()){
            for(int i=1;i<=n;i++)printf("%d%c",hi[i],(i==n?'\n':' '));
        }else puts("Impossible");
    }
}

