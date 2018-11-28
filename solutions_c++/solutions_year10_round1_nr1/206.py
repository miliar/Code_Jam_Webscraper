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

int T,n,k;
char A[50][50];
vector<char> v[50];
bool check(char x){
   int cnt=0;
   f(i,0,n){
      cnt=0;
      f(j,0,n){
         if(A[i][j]==x) cnt++; else cnt=0;
         if(cnt==k) return 1;
      }
   }
   f(j,0,n){
      cnt=0;
      f(i,0,n){
         if(A[i][j]==x) cnt++; else cnt=0;
         if(cnt==k) return 1;
      }
   }
   f(d,-n+1,n){
      cnt=0;
      f(i,max(0,-d),min(n-d,n) ){
         if(A[i][i+d]==x) cnt++; else cnt=0;
         if(cnt==k) return 1;
      }
   }
   f(d,0,2*n-1){
      cnt=0;
      f(i,max(0,d-n+1),min(d+1,n) ){
         if(A[i][d-i]==x) cnt++; else cnt=0;
         if(cnt==k) return 1;
      }
   }
   return 0;
}

int main()
{
   cin>>T;
   f(t,0,T){
      f(i,0,50)v[i].clear();
      cin>>n>>k;
      f(i,0,n)f(j,0,n){ cin>>A[i][j]; if(A[i][j]!='.')v[i].push_back(A[i][j]);}
      fd(i,n-1,0){
         int k=v[i].size();
         f(j,0,n-k)A[i][j]='.';
         f(j,0,k)A[i][j+n-k]=v[i][j];
      }
      
      bool red,blue;
      red=check('R'); blue=check('B');
      cout<<"Case #"<<t+1<<": ";
      if(red && blue)cout<<"Both";
      if(red && !blue)cout<<"Red";
      if(!red && blue)cout<<"Blue";
      if(!red && !blue)cout<<"Neither";
      cout<<endl;
   }
}
