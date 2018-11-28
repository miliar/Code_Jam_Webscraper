#include<iostream>
#include <sstream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>
#include<cctype>
#include<bitset>
#include<queue>
#include<ctime>
using namespace std;

typedef long long int64;
#define pb push_back 
#define inf 1000000000 
#define ll long long
#define INF ((ll)inf*(ll)inf)
#define L(s) (int)(s).size() 
#define rp(i,n) for(int (i)=0;(i)<(n);++(i)) 
#define inc(i,a,b) for (int (i)=a;(i)<=(b);(i)++)
#define dec(i,b,a) for (int (i)=b;(i)>=(a);(i)--)
#define C(a) memset((a),0,sizeof(a)) 
#define CI(a) memset((a),127,sizeof(a))
#define CN(a) memset((a),255,sizeof(a))
#define all(c) (c).begin(), (c).end() 
#define VI vector<int> 
#define mp make_pair 
#define pii pair<int,int> 
#define pdd pair<double,double> 
#define x first 
#define y second

const int maxn=100010;
ll a[100010];
int n=0,t,ans=0;
ll m;

bool prime(int n)
  {
   for (int i=2;i<=sqrt(n);i++)
     if (n%i==0)
       return false;
   return true;
  }
  
int main()
  {
   freopen("c.in","r",stdin);
   freopen("c.out","w",stdout);
   inc(i,2,maxn-1)
     if (prime(i))
       a[n++]=i;
   //rp(i,n) cout<<a[i]<<endl;
   cin>>t;
   for (int tt=1;tt<=t;tt++)
     {
      cin>>m;
      ans=1;if (m==1) ans=0;
      for (int i=0;i<n;i++)
        if (a[i]*a[i]<=m)
          {
           ll k=a[i];
           while (k*a[i]<=m)
             {
              ans++;
              k*=a[i];
             }
          }
        else break;
      printf("Case #%d: %d\n",tt,ans);
     }
   return 0;
  }
