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

vi pr;

void gen()
{
  int i,j;
  for(i=3;i<1000;i++)
    {
      for(j=0;j<pr.size();j++)
	if((i%pr[j])==0)
	  break;
      if(j==pr.size())
	{
	  // cout<<i<<" ";
	pr.pb(i);
	}
    }
}
int f(int x, int y,int p)
{
  int i;
  for(i=0;i<pr.size();i++)
    if(pr[i]>=p)
      if(((x%pr[i])==0)&&((y%pr[i])==0))
	return 1;
  return 0;
}



int main()
{
  int T;
  cin>>T;
  pr.pb(2);
  gen();
  for(int X=0;X<T;X++)
    {
      vi a;
      int x,y,p,i,j,ctr=0,tmp;
      cin>>x>>y>>p;
      a.clear();
      FOR(i,y+1)
	a.pb(i);
      while(1)
	{
	  tmp=1;
	  //cout<<f(10,15,3);
	  for(i=x;i<=y;i++)
	    for(j=i+1;j<=y;j++)
	      if(f(i,j,p)&&(a[i]!=a[j]))
		{
		  // cout<<i<<" "<<j<<"\n";
		  if(a[j]>a[i])
		    a[j]=a[i];
		  else
		    a[i]=a[j];
		  tmp=0;
		}
	  if(tmp)
	    break;
	}
      for(i=x;i<=y;i++)
	{
	  if(a[i]==i)
	    ctr++;
	}
      cout<<"Case #"<<X+1<<": "<<ctr<<"\n";
    }
  return 0;
}
