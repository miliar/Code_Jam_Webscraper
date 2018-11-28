#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iostream>
using namespace std;

int pos[100],cant[1000];


bool posible(double t, int n,int d)
{
  double beg=-(1LL<<61);
  for(int r=0;r<n;r++)
  {
      for(int c=0;c<cant[r];c++)
      {
	double nex=beg+d;
	if( nex<=pos[r] )
	{
	  beg=max(nex,pos[r]-t);
	}else
	{
	  if(  nex>pos[r]+t ) return false;
	  beg=nex;
	}
      }
  }
  return true;
}

int main()
{
 freopen("in.txt","r",stdin);
   int N;
   scanf("%d",&N);
  for(int _r=0;_r<N;_r++)
  {
    int n,d;
    scanf("%d%d",&n,&d) ;
    for(int r=0;r<n;r++)
       scanf("%d%d",&pos[r],&cant[r]);
    double ini=0.0,fin=(1LL<<50);
    for(int r=0;r<200;r++)
    {
      double piv=(ini+fin)/2.0;
      if( posible(piv,n,d) ) fin=piv;
      else ini=piv;
    }
    printf("Case #%d: %lf\n",_r+1,(ini+fin)/2.0);
  }
 return 0;
}