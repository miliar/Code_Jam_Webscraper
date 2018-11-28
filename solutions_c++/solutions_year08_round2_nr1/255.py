#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <queue>
using namespace std;

#define FOR(i,n) for(i = 0 ; i < n ; i++)
#define pb push_back

typedef vector<vector< int> > vvi;
typedef vector<int> vi;

int main()
{
  int T;
  cin>>T;
  for(int X=0;X<T;X++)
    {
      long long int i,n,A,B,C,D,x,y,M,ctr,j,k;
      cin>>n>>A>>B>>C>>D>>x>>y>>M;
      vvi a;
      vi tmp;
      tmp.pb(x);
      tmp.pb(y);
      a.pb(tmp);
      FOR(i,n-1)
	{
	  x = (A * x + B)%M;
	  y = (C * y + D)%M;
	  tmp.clear();
	  tmp.pb(x);
	  tmp.pb(y);
	  a.pb(tmp);
	}
      ctr=0;
      FOR(i,a.size())
	for(j=i+1;j<a.size();j++)
	  for(k=j+1;k<a.size();k++)
	    {
	      if(((a[i][0]+a[j][0]+a[k][0])%3==0)&&((a[i][1]+a[j][1]+a[k][1])%3==0))
		{
		  ctr++;
		}
	      //cout<<a[i][0]<<" "<<a[j][0]<<" "<<a[k][0]<<"\t";
	      //cout<<a[i][1]<<" "<<a[j][1]<<" "<<a[k][1]<<"\n";
		
	    }
      cout<<"Case #"<<X+1<<": "<<ctr<<"\n";
    }
  return 0;
}
