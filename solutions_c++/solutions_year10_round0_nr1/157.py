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

int n,k;

int main()
{
   int T; cin>>T;
   f(t,1,T+1){
      cin>>n>>k;
      int res=~k&((1<<n)-1);
      cout<<"Case #"<<t<<": "<<(!res? "ON":"OFF")<<endl;
   }
}
