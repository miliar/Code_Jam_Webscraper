#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define   max(a,b)    ((a)>(b)?(a):(b))
#define   min(a,b)    ((a)<(b)?(a):(b))
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(i=(a);i<(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   inf         1000000000
FILE *fin;
FILE *fout;
__int64 n,A,B,C,D,x00,y00,M;
typedef struct  point  
{
	__int64 x;
	__int64 y;
}point;
point  pt[100010];
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int N;
	fscanf(fin,"%d",&N);
    int round;
	for (round=1;round<=N;round++)
	{
		if (round==5)
		{
			int haha=0;
		}
          fscanf(fin,"%I64d%I64d%lld%I64d%I64d%I64d%I64d%I64d",&n,&A,&B,&C,&D,&x00,&y00,&M);
		  pt[0].x=x00;
		  pt[0].y=y00;
		   
		  __int64 x=x00,y=y00;
//		  __int64 x1=0,x2=0,x3=0;
//		  __int64 y1=0,y2=0,y3=0;
		  __int64 mxy[3][3];
		 
		  for (i=0;i<3;i++)
		  {
			  for (j=0;j<3;j++)
			  {
				  mxy[i][j]=0;
			  }
		  }
		   mxy[pt[0].x%3][pt[0].y%3]++;
		  for (i=1;i<=n-1;i++)
		  {
               x=((__int64)A*x+B)%M;
			   y=((__int64)C*y+D)%M;
			   pt[i].x=x;
			   pt[i].y=y;
			   mxy[pt[i].x%3][pt[i].y%3]++;
		  }
		  __int64 ret=0;
          for (i=0;i<9;i++)
          {
			  for (j=i;j<9;j++)
			  {
				  for (k=j;k<9;k++)
				  {
                      int x1=i/3;int y1=i%3;
					  int x2=j/3;int y2=j%3;
					  int x3=k/3;int y3=k%3;
					  if ((x1+x2+x3)%3==0&&(y1+y2+y3)%3==0)
					  {
						 if (i==j&&j==k)
						 {
                             if (mxy[x1][y1]>=3)
                             {
								 __int64 mm=mxy[x1][y1];
								 ret+=(mm*(mm-1)*(mm-2))/6;
                             }
						 }
                         else if (i==j)
                         {
                              if (mxy[x1][y1]>=2)
                             {
								__int64 mm=mxy[x1][y1];
								ret+=mxy[x3][y3]*(mm*(mm-1))/2;
                             }
                         }
						 else if (j==k)
						 {
							 if (mxy[x2][y2]>=2)
                             {
								 __int64 mm=mxy[x2][y2];
								 ret+=mxy[x1][y1]*(mm*(mm-1))/2;
                             }
						 }
						 else if (i==k)
						 {
							 if (mxy[x1][y1]>=2)
                             {
								__int64 mm=mxy[x1][y1];
								 ret+=mxy[x2][y2]*(mm*(mm-1))/2;
                             }
						 }
						 else
						 {
							 ret+=mxy[x1][y1]*mxy[x2][y2]*mxy[x3][y3];
						 }
					  }
				  }
			  }
          }
		  printf("Case #%d: %I64d\n",round,ret);
          fprintf(fout,"Case #%d: %I64d\n",round,ret);
	}
}