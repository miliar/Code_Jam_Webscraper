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
        int n,s,p;
        int sc[200];
        scanf("%d%d%d",&n,&s,&p);
        For(i,n)
            scanf("%d",&sc[i]);
        sort(sc,sc+n);
        reverse(sc,sc+n);
        int ans = 0;
        For(i,n){
            int bs = (sc[i]+2)/3;
            if(sc[i]==0)
                bs = 0;
            if(bs>=p) ans++;
            else if(s){
                if(sc[i]>=2)
                    bs = (sc[i]+4)/3;
                if(bs>=p)
                    s--,ans++;
            }
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
    return 0;
}
