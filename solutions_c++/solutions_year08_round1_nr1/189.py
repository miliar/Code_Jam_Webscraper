#include <vector>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <queue>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FO(i,j,n) for(int i=j;i<n;i++)
#define FOX(i,x) for(int i=0;i<x.size();i++)
#define VI vector<ll>
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

typedef long long ll;
typedef long double ld;

int main()
{
  int t;
  cin>>t;
  int cnt=1;
  while(t--)
    {
      int n;
      cin>>n;
      VI x(n),y(n);
      FOR(i,n)
	cin>>x[i];
      FOR(i,n)
	cin>>y[i];
      S(x);
      S(y);
      ll ret=0;
      FOR(i,n)
	ret+=x[i]*y[n-i-1];
      cout<<"Case #"<<cnt++<<": "<<ret<<endl;
    }
  return 0;
}
