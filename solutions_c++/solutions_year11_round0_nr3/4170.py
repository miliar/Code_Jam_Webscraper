#include <stdio.h>
#include <stdlib.h>
#include <string.h>
main()
{
freopen("C-large.in","r",stdin);
freopen("C-large.out","w",stdout);
 int t=0,n=0,c=0,m=0,flag=0;
 __int64 sum=0;
 char a[22],b[22],d[22],f[21],str[21];
 int j=0,i=0,Case=0,min=0;
 scanf("%d",&t);
 while (t--)
 {
  Case++;
  flag=0;
  sum=0;
  for (i=0;i<21;i++)
  {
   a[i]='0';
   d[i]='0';
   b[i]='0';
   f[i]='0';
  }
  a[21]=0;d[21]=0;b[21]=0;str[21]=0;f[21]=0;
  scanf("%d",&n);
  min=999999;
    for (i=0;i<n;i++)
  {
   scanf("%d",&c);
   if (min>c)
	   min=c;
   itoa (c,a,2);
   m=strlen(a);
   for (j=21;j>=0;j--,m--)
   {
    if (m<0)
     b[j]='0';
    else
     b[j]=a[m];
   }
   b[21]=0;
   for (j=0;j<21;j++)
    f[j]+=b[j];
   sum+=c;
   
  }
    for (i=0;i<21;i++)
    {
     if(f[i]%2==0)
      d[i]='0';
     else d[i]='1';
    }
    printf ("Case #%d: ",Case);
	flag=0;
    for (i=0;i<21;i++)
     if (d[i]!='0')
      flag=1;
	 if (flag==1)
      printf ("NO\n");
     else
     {
		  printf ("%I64d\n",sum-min);
     }
    
     
     
 }
}