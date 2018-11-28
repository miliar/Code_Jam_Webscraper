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
int code[105][105];
int main()
{
    int cas;
    freopen("in.txt","r", stdin);
    freopen("out.txt","w", stdout);
    cin >> cas;
    int T=0;
    while(cas--)
    {
       int n;
       scanf("%d", &n);
       for(int i=0; i<n; ++i)
          for(int j=0; j<n; ++j)
          {
             char ch;
             cin>>ch;
             if(ch=='.')
               code[i][j] = -1;
             else if(ch=='1')
               code[i][j] = 1;
             else
               code[i][j] = 0;
          }
       double wp[105], owp[105], oowp[105];
       double tx, ty;
       
       for(int i=0; i<n; ++i)
       {
          for(int k=0; k<n; ++k)
          {
             tx = ty = 0;
             for(int j=0; j<n; ++j)
             {
                if(j==i)
                   continue;
             if(code[k][j]>0.5)
               tx += 1;
             if(code[k][j]>-0.5)
               ty += 1;
             }
             wp[k] = tx/ty;
          }
          tx = ty = 0;
          for(int j=0; j<n; ++j)
          {
             if(code[i][j]>-0.5)
               tx += wp[j];
             if(code[i][j]>-0.5)
               ty += 1;
          }
          owp[i] = tx/ty;
       }
       for(int i=0; i<n; ++i)
       {
          tx = ty = 0;
          for(int j=0; j<n; ++j)
          {
             if(code[i][j]>-0.5)
               tx += owp[j];
             if(code[i][j]>-0.5)
               ty += 1;
          }
          oowp[i] = tx/ty;
       }
       for(int k=0; k<n; ++k)
          {
             tx = ty = 0;
             for(int j=0; j<n; ++j)
             {
                
             if(code[k][j]>0.5)
               tx += 1;
             if(code[k][j]>-0.5)
               ty += 1;
             }
             wp[k] = tx/ty;
          }
       printf("Case #%d:\n", ++T);
       for(int i=0; i<n; ++i)
       {
         // cout<<i<<" ";
          //cout<<"\nkirk";
         // cout<<wp[i]<<"  "<<owp[i]<<"  "<<oowp[i]<<endl;
          cout<<wp[i]/4+owp[i]/2+oowp[i]/4;
          cout<<endl;
       }
    }
    //cout<<"\n\nend\n";
   // while(1);
    return 0;
}
