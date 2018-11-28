#include<stdio.h>
#include<unordered_set>
#include<algorithm>
#include<math.h>
using namespace std;
int grid[501][501];
char s[1001];
int main()
{
	
	freopen("D:\\Gcj\\B\\input.txt","r",stdin);
	freopen("D:\\Gcj\\B\\output.txt","w",stdout);
   int t;
   gets(s);
   sscanf(s,"%d",&t);
   for(int tt=0;tt<t;tt++)
   {
	   
	   int R,C,D;
	   gets(s);
	   sscanf(s,"%d %d %d",&R,&C,&D);
	   for(int i=0;i<R;i++)
	   {
		   gets(s);
		   for(int j=0;j<C;j++)
		   {
			   grid[i][j]=int(s[j])-int('0')+D;
		   }
	   }
	    int maxA=-1;
	   for(int i=0;i<R-2;i++)
	   {
		   for(int j=0;j<C-2;j++)
		   {
			   //i,j-tostartWith
			   
			   int mnsz=R-i;
			   mnsz=min(mnsz,C-j);
			  
			   for(int sz=3;sz<=mnsz;sz++)
			   {
				   //check 
				double sum1=0,sum2=0;
				   double  centerX=i+sz/2;
				   double centerY=j+sz/2;
				   if(sz%2==1)
				   {
					   centerX+=0.5;
					   centerY+=0.5;
				   }
				   for(int k=i;k<i+sz;k++)
				   {
					   for(int t=j;t<j+sz;t++)
					   {
						   if(k==i && t==j 
							  || k==i && t==j+sz-1
							  || k==i+sz-1 && t==j+sz-1
							  || k==i+sz-1 && t==j)
							  continue;
						   sum1+=(k+0.5-centerX)*grid[k][t];
						   sum2+=(t+0.5-centerY)*grid[k][t];
					   }
				   }
				   if(fabs(sum1)<=1e-8 && fabs(sum2)<=1e-8 && sz>maxA)
				   {
					   maxA=sz;
				   }
				
			   }
		   }
	   }
	   if(maxA==-1)
	   {
		     printf("Case #%d: IMPOSSIBLE\n",tt+1); 
	   }
	   else printf("Case #%d: %d\n",tt+1,maxA); 
   }
		
	
}