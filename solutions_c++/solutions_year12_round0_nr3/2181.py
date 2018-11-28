#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <map>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <string>
#include <set>
#include <cstring>
using namespace std;
#define For(i,n) for(int i=0;i<n;i++)
#define sFor(i,j,n) for(int i=j;i<n;i++)
#define sz(i) int(i.size())
#define mst(i,n) memset(i,n,sizeof(i))
#define eps 1e-9
#define INF 1e20
#define MOD 1000000007
#define LL long long
#define pi acos(-1)
LL gcd(LL a,LL b){if(a==0)return b;return gcd(b%a,a);}
int main()
{
    int t;
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    scanf("%d",&t);
    int ca = 0;
    while(t--){
        int ans = 0;
        int A,B;
        scanf("%d %d",&A,&B);
        for(int i=A;i<=B;i++){
            int tmp=i;
            int dig[10];
            int tot=0;
            while(tmp)
                dig[tot++]=tmp%10,tmp/=10;
            reverse(dig,dig+tot);
            set<int>st;
            for(int j=0;j<tot;j++){
                int fg=-1;
                int newnum=0;
                For(k,tot){
                    if(dig[(j+k+tot)%tot]>dig[k]){if(fg==-1)fg=1;}
                    else if(dig[(j+k+tot)%tot]<dig[k]){if(fg==-1)fg=0;}
                    newnum=newnum*10+dig[(j+k+tot)%tot];
                }
                if(st.find(newnum)!=st.end())continue;
                st.insert(newnum);
                if(fg==1&&newnum<=B) ans++;
                //if(fg==1&&newnum<=B) printf("### %d %d\n",i,newnum);
            }
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
    return 0;
}
