#include<iostream>
#include<cstring>
#include<vector>
using namespace std;
int zz[2][320][320];
int main()
{
   int cas;

   int cc=0;
   int i,j,k,t,a,b,c,d;
   freopen("C:\\ee.txt","r",stdin);
   freopen("C:\\out.txt","w",stdout);
   cin>>cas;
   while(cas--)
   {cc++;
	   memset(zz,0,sizeof(zz));
	    cin>>t;
	
	   int down=-1;
	   for(i=1;i<=t;i++)
	   {
		   scanf("%d %d %d %d",&a,&b,&c,&d);
		 
		   for(j=a;j<=c;j++)
			   for(k=b;k<=d;k++)
		   {
              zz[0][j][k]=1;
		   }
		 
	   }
	   int tim=0;
	   int now,ori;
	   now=0;
	   ori=1;
	   while(1)
	   {
		   bool ok=0;
		   swap(now,ori);
		   for(i=1;i<=320;i++)
		   {
			   for(j=1;j<=320;j++)
			   {
				   if(zz[ori][i][j]==0)
				   {
					   if(zz[ori][i][j-1]&&zz[ori][i-1][j])
					   {
						   
                            ok=1;
							zz[now][i][j]=1;
					   }
					   else
						   zz[now][i][j]=0;
				   }
				   else
				   {
                      if(zz[ori][i][j-1]||zz[ori][i-1][j])
					   {
						   
                            ok=1;
							zz[now][i][j]=1;
					   } 
					  else
						  zz[now][i][j]=0;
				   }
			   }
		   }
		   if(ok==0)
			   break;
		   tim++;
	   }
	  printf("Case #%d: %d\n",cc,tim+1);
	  }
   return 0;
}