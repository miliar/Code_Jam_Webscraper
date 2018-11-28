#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define dist(x1,y1,x2,y2) sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
#define lim 4

int cs,c,n,i;
double res;
int X[lim],Y[lim],R[lim];

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d",&n);
	for(i=0;i<n;i++)
	  scanf("%d%d%d",&X[i],&Y[i],&R[i]);
	if(n==1)
	  res=R[0];
	else if(n==2)
	  res=max(R[0],R[1]);
	else
	{
	  res=max((double)R[0],(dist(X[1],Y[1],X[2],Y[2])+R[1]+R[2])/2);
	  res=min(res,max((double)R[1],(dist(X[0],Y[0],X[2],Y[2])+R[0]+R[2])/2));
	  res=min(res,max((double)R[2],(dist(X[1],Y[1],X[0],Y[0])+R[1]+R[0])/2));
	}
	printf("Case #%d: %.10lf\n",c,res);
  }  
  return 0;
}


