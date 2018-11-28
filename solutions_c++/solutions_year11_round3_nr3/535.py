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
ll gcd(ll a, ll b)
{
   if(a%b==0)
     return b;
   return gcd(b, a%b);
}
int mat[5500];
int main()
{
    int cas;
    freopen("in.txt","r", stdin);
    freopen("out.txt","w", stdout);
    cin >> cas;
    int T=0;
    while(cas--)
    {
       ll n, l, h;
       cin>>n>>l>>h;
       for(int i=0; i<n; ++i)
         cin>>mat[i];
       res = 1;
       printf("Case #%d: ", ++T);
       bool flag = true;
       for(ll i=l; i<=h; ++i)
       {
          flag = true;
          for(int j=0; j<n; ++j)
          {
             if(i%mat[j]!=0&&mat[j]%i!=0)
             {
               flag = false;
               break;
             }
          }
          res = i;
          if(flag)
            break;
       }
       if(flag)
          cout<<res<<endl;
       else
          cout<<"NO\n";
    }
    clog<<"\n\nend\n";
    while(1);
    return 0;
}
