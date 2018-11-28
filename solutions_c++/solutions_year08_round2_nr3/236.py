#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <queue>
using namespace std;

#define FOR(i,n) for(int i = 0 ; i < n ; i++)
#define PB push_back

typedef vector<vector< int> > vvi;
typedef vector<int> vi;

int main()
{
  int T;
  cin>>T;
  for(int X=0;X<T;X++)
    {
      int i,j,K,ctr,n,x;
      cin>>K>>n;
      vi a(K+1);
      FOR(i,K+1)
	a[i]=-1;
      a[0]=0;
      x=1;
      for(i=1;i<=K;i++)
	{
	  ctr=0;
	  while(ctr<i)
	    {
	      if(a[x]==-1)
		ctr++;
	      if(ctr==i)
		break;
	      x++;
	      if(x>K)
		{
		  while(ctr<i)
		    ctr+=K+1-i;
		  ctr-=K+1-i;
		  x=1;
		}
	    }
	  a[x]=i;
	}
      // FOR(i,K+1)
      //	cout<<a[i]<<" ";
      cout<<"Case #"<<X+1<<": ";
      FOR(i,n)
	{
	  cin>>x;
	  cout<<a[x]<<" ";
	}
      cout<<"\n";
    }
  return 0;
}
