#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int f[111][258],t,D,I,n,m,a[111],minn[111],g[258],ans;

int main()
{
 int i,j,ll,k,tmp,jj;
 freopen("02.txt","w",stdout);
 scanf("%d",&t);
   for (ll=1;ll<=t;ll++)
    {	
	 scanf("%d%d%d%d",&D,&I,&m,&n);
	 memset(f,0,sizeof(f));
	 minn[0]=1111111111;
	 for (i=1;i<=n;i++)
	 {
	  scanf("%d",&a[i]);
	  minn[i]=1111111111;
	 }
	 for (i=1;i<=n;i++)
	  {
	   for (j=0;j<256;j++)
	    {
	     f[i][j]=f[i-1][j]+D;
	     g[j]=0;
	    }
	   for (j=0;j<256;j++)
	    {
		 tmp=f[i-1][j];
		  for (k=j;k>=0&&k>=j-m;k--)
		   if (f[i][k]>tmp+abs(a[i]-k))
		    f[i][k]=tmp+abs(a[i]-k);	
		  for (k=j;k<256&&k<=j+m;k++)
		   if (f[i][k]>tmp+abs(a[i]-k))
		    f[i][k]=tmp+abs(a[i]-k);	
	    }
	  
	   do
	   {
		 minn[i]=1111111111; 	
		jj=-1;	
	   for (j=0;j<256;j++)
	     if (f[i][j]<minn[i]&&!g[j])
		 {
		  minn[i]=f[i][j];
		  jj=j;		
		 } 
	    if (jj>=0)
	     {
		  g[jj]=1;		
		  for (k=jj;k>=0&&k>=jj-m;k--)
		   if (f[i][k]>f[i][jj]+I)
		    f[i][k]=f[i][jj]+I;	
		  for (k=jj;k<256&&k<=jj+m;k++)
		   if (f[i][k]>f[i][jj]+I)
		    f[i][k]=f[i][jj]+I;		
		 }
	   }while (jj>=0); 
	  }
	 ans=1111111111; 
	 for (i=0;i<256;i++)
	   if (ans>f[n][i]) ans=f[n][i];
	 printf("Case #%d: %d\n",ll,ans);

	
    }
 return 0;	
}
