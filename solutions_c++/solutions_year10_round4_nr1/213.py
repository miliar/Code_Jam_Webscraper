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
#define rall(v) (v).rbegin(),(v).rend()
#define clr(B,x) memset(B,x,sizeof(B));

using namespace std;
long long toi(string s){istringstream is(s);long long x;is>>x;return x;}
string tos(long long t){stringstream st; st<<t;return st.str();}
long long gcd(long long a, long long b){return __gcd(a,b);}long long lcm(long long a,long long b){return a*(b/gcd(a,b));}

int Tests;
int a[51][51];
int b[51][51];
int diag(int k){
   f(d,0,k){
      bool sim=1;
      f(i,0,k-d-1)f(j,0,k-d-1-i){
         int tt=k-d-1-i-j;
         if(a[i][j]!=a[i+tt][j+tt]){ sim=0; break;}
      }
      if(sim) return d;
   }
}

int main()
{
   cin>>Tests;
   f(t,0,Tests){
      int res;
      int k; cin>>k;
      f(i,0,2*k-1){
         f(j,0,min(i+1,2*k-1-i)){
            int x=min(i,k-1); int y=max(0,i-k+1);
            cin>>a[x-j][y+j];
         }
      }
      
      int a1,a2,b1,b2;
      a1=diag(k);
      f(i,0,k-1)f(j,0,k-1-i){
         int tt=k-1-i-j;
         swap(a[i][j],a[i+tt][j+tt]);
      }
      //f(i,0,k){f(j,0,k)cout<<a[i][j]; cout<<endl;}
      a2=min(diag(k),a1);
      f(i,0,k)f(j,0,k){
         b[i][j]=a[j][k-1-i];
      }
      f(i,0,k)f(j,0,k) a[i][j]=b[i][j];
      //f(i,0,k){f(j,0,k)cout<<a[i][j]; cout<<endl;}
      b1=diag(k);
      f(i,0,k-1)f(j,0,k-1-i){
         int tt=k-1-i-j;
         swap(a[i][j],a[i+tt][j+tt]);
      }
      b2=min(diag(k),b1);
      
      cout<<"Case #"<<t+1<<": ";
      int z=a2+b2+k;
      cout<<z*z-k*k<<endl;
   }
}
