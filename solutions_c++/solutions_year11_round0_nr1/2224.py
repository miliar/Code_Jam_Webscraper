#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

int ax[110];
int bx[110];
int x[110];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int T,n,i,k,j,ca=1,la,lb,t;
	char s[10];
	scanf("%d",&T);
	while(T--)
	{
	   scanf("%d",&n);
       la=0,lb=0;
	   for(i=1;i<=n;i++)
	   {
          scanf("%s %d",s,&k);
		  if(s[0]=='O')
		  {
			  ax[++la]=k;
			  x[i]=0;
		  }
		  if(s[0]=='B')
		  {
			  bx[++lb]=k;
			  x[i]=1;
		  }
	   }

	   int pa=1,pb=1;
	   int pur_a=1,pur_b=1;
	   int lx=1;
	   int ok_a=0,ok_b=0;

	   if(x[lx]==0 && ax[pa]==1)
		   ok_a=1;
	   if(x[lx]==1 && bx[pb]==1)
		   ok_b=1;

	   for(t=1; ;t++)
	   {
	      if(pa>=la+1 && pb>=lb+1)
			  break;
          if(x[lx]==0)
		  {
            
		     if(bx[pb]==pur_b)
				 ok_b=1;

			 if(bx[pb]>pur_b)
				 pur_b+=1;
			 else if(bx[pb]<pur_b)
				 pur_b-=1;

			 if(bx[pb]==pur_b)
				 ok_b=1;


			 if(ok_a==1)
			 {
				 int temp1=ax[pa];
				 lx+=1;
				 pa+=1;
				 if(pa<=la && ax[pa]!=temp1)
				    ok_a=0;
				 if(lx>n)
					 break;
				 continue;
			 }
			 
			 if(ax[pa]==pur_a)
				 ok_a=1;

			 if(ax[pa]>pur_a)
				 pur_a+=1;
			 else if(ax[pa]<pur_a)
				 pur_a-=1;
             
			 if(ax[pa]==pur_a)
				 ok_a=1;

		  }

		  if(x[lx]==1)
		  {
            
		     if(ax[pa]==pur_a)
				 ok_a=1;
			 if(ax[pa]>pur_a)
				 pur_a+=1;
			 else if(ax[pa]<pur_a)
				 pur_a-=1;
			 if(ax[pa]==pur_a)
				 ok_a=1;

			 if(ok_b==1)
			 {
				 int temp2=bx[pb];
				 lx+=1;
				 pb+=1;
				 if(pb<=lb && bx[pb]!=temp2)
				    ok_b=0;
				 if(lx>n)
					 break;
				 continue;
			 }

			 if(bx[pb]==pur_b)
			     ok_b=1; 
			 if(bx[pb]>pur_b)
				 pur_b+=1;
			 else if(bx[pb]<pur_b)
				 pur_b-=1;
			 if(bx[pb]==pur_b)
				 ok_b=1;

		  }
	   }
	   printf("Case #%d: %d\n",ca++,t);
	}
	return 0;
}