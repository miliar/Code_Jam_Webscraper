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

#define AND 1
#define OR 0

int memo[11000][2];
int m,v;

int gates[11000][2];

int ans(int a, int b)
{
  int &res=memo[a][b];
  if(res!=-1)
    return res;
  if(a>(m-1)/2)
    {
      if(b==gates[a][0])
	return res=0;
      else
	return res=-2;
    }
  int l=2*a,r=2*a+1;
  res=-1;
  FOR(i,2)
    FOR(j,2)
    {
      if((i&j)==b)
	{
	  int t1=ans(l,i);
	  int t2=ans(r,j);
	  if(t1!=-2 && t2!=-2)
	    {
	      int add=0;
	      if(gates[a][0]==AND)
		add=0;
	      else
		add=1;
	      if(add==0 || (add==1 && gates[a][1]==1))
		 if(res==-1 || res>add+t1+t2)
		 res=t1+t2+add;
	    }
	}
      if((i|j)==b)
	{
	  int t1=ans(l,i),t2=ans(r,j);
	  if(t1!=-2 && t2!=-2)
	    {
	      int add=0;
	      if(gates[a][0]==OR)
		add=0;
	      else
		add=1;
	      if(add==0 || (add==1 && gates[a][1]==1))
		if(res==-1 || res>add+t1+t2)
		  res=t1+t2+add;
	    }
	}
    }
  if(res==-1)
    return res=-2;
  return res;
}

int main()
{
  int t;
  cin>>t;
  int cnt=1;
  while(t--)
    {
      cin>>m>>v;
      memset(memo,-1,sizeof(memo));
      FOR(i,m)
	{
	  if(i+1>(m-1)/2)
	    cin>>gates[i+1][0];
	  else
	    cin>>gates[i+1][0]>>gates[i+1][1];
	}
      int ret=ans(1,v);
      if(ret==-2)
	printf("Case #%d: IMPOSSIBLE\n",cnt++);
      else
	printf("Case #%d: %d\n",cnt++,ret);
    }
  return 0;
}
