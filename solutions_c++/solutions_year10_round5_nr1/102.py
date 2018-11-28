#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)
#define ll long long
#define clr(A,x) memset(A,x,sizeof(A))
#define oo 1<<30
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()

using namespace std;

int T,d,n,mod;

ll modpow(ll a, ll b){
    if(b == 0) return 1;
    ll c = modpow(a, b / 2);
    c = (c * c) % mod;
    if(b % 2 == 1) c = (c * a) % mod;
    return c;
}

ll modinverse(ll a){
    ll res = modpow(a, mod - 2);    
    return res;
}
int pr[1000010], p[100010];
int dz[7];
ll a[10];
string zz="I don't know.";

int main()
{
   dz[0]=1;
   int i,j,cnt=0;
   for(i=1;i<7;i++) dz[i]=10*dz[i-1];
   for(i=0;i<1000000;i++) pr[i]=1;
   pr[0]=pr[1]=0;
   for(i=2;i<1000000;i++) if(pr[i])
   {
      p[cnt]=i; cnt++;
      for(j=i+i;j<=1000000;j+=i) pr[j]=0;
   }
   
   cin>>T;
   f(t,0,T){
      cin>>d>>n;
      f(i,0,n) cin>>a[n-1-i];
      printf("Case #%d: ",t+1);
      if(n==1){
         cout<<zz<<endl;
         continue;
      }
      if(a[0]==a[1]){
         printf("%d\n",a[0]);
         continue;
      }
      if(n==2){
         cout<<zz<<endl;
         continue;
      }
      int *q=upper_bound(p,p+cnt,*max_element(a,a+n) );
      vector<int> A;

      while(q<p+cnt){
         if(*q>dz[d]) break;
         bool ok=1;
         f(i,0,n-3){
            if( ((a[i+2]-a[i+1])*(a[i+2]-a[i+1])-(a[i+1]-a[i])*(a[i+3]-a[i+2]) )%(*q))
             {ok=0;  break;}
         }
         if(ok==0){q++; continue;}
         if((a[0]-a[1])%(*q)==0) continue;
         mod=*q;
         ll _y,y=modinverse(a[1]-a[2]); _y=y;
         _y*=a[0]-a[1], _y%=mod;
         _y*=a[0]-a[1], _y%=mod;
         _y+=a[0], _y%=mod;
         if(_y<0) _y+=mod;
         A.push_back(_y);
         //cout<<_y<<endl;
         if( A.size()>1) break;

         q++;
      }
      if(A.size()>1){ 
         if(A[0]!=A[1]) cout<<zz<<endl;
         else printf("%d\n",*A.begin());
      }
      else printf("%d\n",*A.begin());
   }
}
