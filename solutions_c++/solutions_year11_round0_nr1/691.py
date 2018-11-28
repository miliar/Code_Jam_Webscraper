#include<iostream>
#include<math.h>
using namespace std;
int main()
{
 int t,n,m=0,i,l,s,d,j,c[2],f[2];
 char a;
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 while(t--)
	  {
	   scanf("%d",&n);
	   c[0]=c[1]=1;
	   f[0]=f[1]=s=0;
	   for(i=0;i<n;i++)
		  {
	       scanf("\n%c%d",&a,&l);
	       if(a=='O') j=0;
		   else if(a=='B') j=1;
	       d=abs(c[j]-l)+1;
	       c[j]=l;
		   if(f[j]>=d-1)
			 {
              s++;
			  f[j]=0;
			  f[1-j]++;	  
			 }
	       else
			 {
			  s+=d-f[j];
			  f[1-j]+=d-f[j];
			  f[j]=0;
			 }
		 }
	 printf("Case #%d: %d\n",++m,s);
   }
 return 0;
}

