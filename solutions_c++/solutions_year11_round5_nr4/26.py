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
int casN,n,len;
long long ori,bit[30],ans,tmp;
char inp[65];
inline bool squr(LL xx){
    LL L=0,R=(1ll<<30)+1,M;
    while(L<R-1){
        M=(L+R)/2;
        if(M*M<=xx)L=M;
        else R=M;
    }
    return xx==L*L;
}
int main(){
    scanf("%d",&casN);
    for(int III=0;III<casN;III++){
        scanf("%s",inp);
        n=0;
        ori=0;
        len=strlen(inp);
        for(int i=0;i<len;i++){
            if(inp[i]=='?'){
                bit[n++]=1ll<<len-1-i;
                
            }else if(inp[i]=='1'){
                ori+=1ll<<len-1-i;
            }
        }
        ans=ori;
        for(int i=0;i<(1<<n);i++){
            tmp=0;
            for(int j=0;j<n;j++){
                if(i&(1<<j))tmp+=bit[j];
            }
            //printf("%I64d\n",ori+tmp);
            if(squr(ori+tmp)){
                ans=ori+tmp;
                break;
            }
        }
        printf("Case #%d: ",III+1);
        for(int i=0;i<len;i++){
            printf("%d",(ans&(1ll<<len-1-i))>0ll);
        }
        printf("\n");
    }
    scanf(" ");
    return 0;
}

