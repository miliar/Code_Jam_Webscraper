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
#define FO(i,j,n) for(int i=j;i<n;i++)
#define FOX(i,x) for(int i=0;i<x.size();i++)
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

typedef long long ll;
typedef long double ld;

int memo[100][1000];

int s,q;
string names[200];
string queries[1100];

int ans(int a, int b)
{
  int& res=memo[a][b];
  if(res!=-1)
    return res;
  if(names[a]==queries[b])
    return res=q;
  if(b==q-1)
    return res=0;
  res=ans(a,b+1);
  FOR(i,s)
    res=min(res,1+ans(i,b+1));
  return res;
}

int main()
{
  int t;
  cin>>t;
  int cnt=1;
  while(t--)
    {
      memset(memo,-1,sizeof(memo));
      cin>>s;
      getline(cin,names[0]);
      FOR(i,s)
	getline(cin,names[i]);
      cin>>q;
      getline(cin,queries[0]);
      FOR(i,q)
	getline(cin,queries[i]);
      int ret=q;
      if(q)
	FOR(i,s)
	  ret=min(ret,ans(i,0));
      printf("Case #%d: %d\n",cnt++,ret);
    }
  return 0;
}
