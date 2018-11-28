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
#define oo 1<<30
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()

using namespace std;

int T,r,k,n;
int next[1000], money[1000];
int A[2000];

int main()
{
   cin>>T;
   f(t,1,T+1){
      cin>>r>>k>>n;
      f(i,0,n)cin>>A[i];
      copy(A,A+n,A+n);
      f(i,0,n){
         int s=0; int j=i;
         while(s+A[j]<=k && j<i+n) s+=A[j++];
         money[i]=s;
         next[i]=j%n; //cout<<s<<" "<<j%n<<endl;
      }
      ll res=0; int ini=0;
      f(i,0,r){
         res+=money[ini];
         ini=next[ini];
      }
      cout<<"Case #"<<t<<": "<<res<<endl;
   }
}
