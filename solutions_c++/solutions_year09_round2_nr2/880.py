#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <queue>
#include <sstream>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define ROF(i,n) for(int i=n;i>=0;i--)
#define FO(i,j,n) for(int i=j;i<n;i++)
#define RO(i,j,n) for(int i=j;i>=n;i--)
#define FOX(i,x) for(int i=0;i<x.size();i++)
#define ROX(i,n) for(int i=x.size()-1;i>=0;i--)
#define FX(i,j,x) for(int i=j;i<x.size();i++)
#define VI vector<int>
#define VB vector<bool>
#define VVI vector<vector <int> >
#define VS vector<string>
#define S(x) sort(x.begin(),x.end());
#define R(x) reverse(x.begin(),x.end());
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define MP make_pair
#define sma(a,b) a=min(a,b);
#define sb(a,b) if(a>b)swap(a,b);
#define bs(a,b) if(a<b)swap(a,b);

typedef long long ll;
typedef long double ld;

string ans(string a)
{
 S(a);
 a='0'+a;
 FOX(i,a)
 {
  if(a[i]!='0')
  {
   swap(a[0],a[i]);
   return a;
  }
 }
}

int main()
{
    int t;
    string n;
    cin>>t;
    FOR(i,t)
    {
     cin>>n;
     if(next_permutation(n.begin(),n.end()))
      printf("Case #%d: %s\n", i+1, n.c_str());
     else
      printf("Case #%d: %s\n", i+1, ans(n).c_str());     
    }
    return 0;
}
