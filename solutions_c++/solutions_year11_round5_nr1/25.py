#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define CLR(x) memset((x), 0, sizeof(x))
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FEACH(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define F first
#define S second
//using namespace std;
typedef long long LL;
inline LL Min(LL a,LL b){
    return a<b?a:b;
}
inline LL Max(LL a,LL b){
    return a>b?a:b;
}
inline LL Abs(LL a){
    return a>0?a:-a;
}
bool cmp(LL a,LL b){
    return a<b;
}
int casN,l,u,n,nsp,run,w,low[1010][2],upp[1010][2];
double spe[2010][2],area,curr,next,ans[2010],L,R,M;
double interpo(double x1,double y1,double x2,double y2,double x3){
    return ((x1-x3)*y2+(x3-x2)*y1)/(x1-x2);
}
double trap(double y1,double y2,double xx){
    return (y1+y2)*xx/2;
}
int main(){
    scanf("%d",&casN);
    for(int III=0;III<casN;III++){
        scanf("%d%d%d%d",&w,&l,&u,&n);
        for(int i=0;i<l;i++){
            scanf("%d%d",&low[i][0],&low[i][1]);
        }
        for(int i=0;i<u;i++){
            scanf("%d%d",&upp[i][0],&upp[i][1]);
        }        
        run=0;
        nsp=0;
        for(int i=0;i<l-1;i++){
            spe[nsp][0]=low[i][0];
            if(run!=0)spe[nsp][1]=interpo(upp[run-1][0],upp[run-1][1],upp[run][0],upp[run][1],low[i][0])-low[i][1];
            else spe[nsp][1]=upp[0][1]-low[i][1];
            nsp++;
            
            while(run<u&&upp[run][0]<=low[i+1][0]){
                spe[nsp][0]=upp[run][0];
                spe[nsp][1]=upp[run][1]-interpo(low[i][0],low[i][1],low[i+1][0],low[i+1][1],upp[run][0]);
                run++;
                nsp++;
            }
        }
        area=0;
        for(int i=0;i<nsp-1;i++){
            area+=trap(spe[i][1],spe[i+1][1],spe[i+1][0]-spe[i][0]);
        }
        curr=0;
        run=1;
        for(int i=0;i<nsp-1;i++){
            next=trap(spe[i][1],spe[i+1][1],spe[i+1][0]-spe[i][0]);
            while(run<n&&curr+next>area*run/n){
                L=spe[i][0];
                R=spe[i+1][0];
                while(R-L>1e-10){
                    M=(R+L)/2;
                    if(curr+trap(spe[i][1],interpo(spe[i][0],spe[i][1],spe[i+1][0],spe[i+1][1],M),M-spe[i][0])>area*run/n)R=M;
                    else L=M;
                }
                ans[run]=(L+R)/2;
                run++;
            }
            curr+=next;
        }
        printf("Case #%d:\n",III+1);
        for(int i=1;i<=n-1;i++)printf("%.8lf\n",ans[i]);
    }
    scanf(" ");
    return 0;
}

