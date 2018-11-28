#include <vector>
#include <string>
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

int main()
{
  int t;
  cin>>t;
  int cnt=1;
  while(t--)
    {
      int k;
      string s;
      cin>>k>>s;
      int n=s.size();
      int ret=n;
      VI temp(k);
      FOR(i,k)
	temp[i]=i;
      do
	{
	  int val=1;
	  string tmp=s;
	  FOR(i,n/k)
	    FOR(j,k)
	    tmp[i*k+j]=s[i*k + temp[j]];
	  FO(i,1,s.size())
	    if(tmp[i]!=tmp[i-1])
	      val++;
	  if(val<ret)
	    ret=val;
	}while(next_permutation(temp.begin(),temp.end()));
      printf("Case #%d: %d\n",cnt++,ret);
    }
  return 0;
}
