#include <iostream>
#include <string>
#include <cstdio>
#include <map>
#include <vector>
using namespace std;

#define PB push_back
#define MP make_pair
#define PII pair<int, int>

#define SZ(x) ((int)((x).size()))
#define OUT(x) printf(#x" %d\n", x)

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define rep(i, a, b) for((i)=(a); (i)<(int)(b); (i)++)
#define foreach(c,itr) \
for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

typedef long long ll;

#define maxn 100010
int a[maxn];
vector<PII > vc[maxn];

ll res = 0;
int i;

ll gcd(ll a, ll b)
{
   if(a%b==0)
     return b;
   return gcd(b, a%b);
}
int main()
{
    int cas;
    freopen("in.txt","r", stdin);
    freopen("out.txt","w", stdout);
    cin >> cas;
    ll n, d, g;
    int T=1;
    while(cas--)
    {
       scanf("%lld%lld%lld", &n, &d, &g);
       printf("Case #%d: ", T++);
       
       bool flag = false;
       
       for(int i=1; i<=n; ++i)      
       {
          if(i*d%100!=0)
             continue;
          else
          {
            flag = true;
            break;
          }    
       }
       if(d < 100 && g==100)
         flag = false;
       if(d==0 && g!=100)
         flag = true;
       if(g==0 && d>0)
         flag = false;
       if(flag)
         printf("Possible\n");
       if(!flag)
         printf("Broken\n");
    }
    //while(1);
    return 0;
}
