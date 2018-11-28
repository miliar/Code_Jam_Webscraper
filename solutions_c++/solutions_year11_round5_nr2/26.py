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
int casN,n,inp[1010],cur[1010],curn,ans,cnt[10010];
int main(){
    scanf("%d",&casN);
    for(int III=0;III<casN;III++){
        scanf("%d",&n);
        memset(cnt,0,sizeof(cnt));
        for(int i=0;i<n;i++){
            scanf("%d",&inp[i]);
            cnt[inp[i]]++;
        }
        ans=1000000000;
        curn=0;
        for(int i=0;i<10010;i++){
            for(int j=cnt[i];j<curn;j++){
                ans=Min(ans,cur[j]);
            }
            for(int j=curn;j<cnt[i];j++){
                cur[j]=0;
            }
            curn=cnt[i];
            for(int j=0;j<curn;j++){
                cur[j]++;
            }
            std::sort(cur,cur+curn,cmp);
        }
        printf("Case #%d: %d\n",III+1,n==0?0:ans);
    }
    scanf(" ");
    return 0;
}

