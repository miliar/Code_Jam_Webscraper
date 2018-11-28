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
#define MAX 1000010
struct sor{
    double dur;
    double spe;
}cel[MAX];
bool cmp(sor a,sor b){
    return a.spe<b.spe;
}
int casN,n;
double beg,end,spe,las;
double s,r,t,l,ans;

int main(){
    scanf("%d",&casN);
    for(int III=0;III<casN;III++){
        scanf("%lf%lf%lf%lf%d",&l,&s,&r,&t,&n);
        for(int i=0;i<n;i++){
            scanf("%lf%lf%lf",&beg,&end,&spe);
            cel[i].dur=end-beg;
            cel[i].spe=spe;
            l-=end-beg;
        }
        cel[n].dur=l;
        cel[n].spe=0;
        std::sort(cel,cel+n+1,cmp);
        ans=0;
        for(int i=0;i<=n;i++){
            if(t*(r+cel[i].spe)<cel[i].dur){
                ans+=t+(cel[i].dur-t*(r+cel[i].spe))/(s+cel[i].spe);
                t=0;
            }else{
                ans+=cel[i].dur/(r+cel[i].spe);
                t-=cel[i].dur/(r+cel[i].spe);
            }
        }
        printf("Case #%d: %.8lf\n",III+1,ans);
    }
    scanf(" ");
    return 0;
}

