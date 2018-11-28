#include <stdio.h>
#include <string.h>
  int main()
	{
	long T,I,i,j,k,l,m,n,s,a[99];
	char st[999];
	scanf("%ld",&T);
	gets(st);
	for(I=1;I<=T;I++)
	  {
	  printf("Case #%ld: ",I);
	  gets(st);
	  l=strlen(st);
	  n=0;
	  s=0;
	  for(i=0;i<l;i++)
		if(st[i]!=' ') n=n*10+st[i]-48;
				  else {
					   a[s]=n;
					   s++;
					   n=0;
					   }
	  a[s]=n;
	  l=1;
	  for(i=2;l;i++)
		{
		l=0;
		for(j=0;j<=s;j++)
		  {
		  k=i;
		  for(m=0;m<99;m++)
			{
			n=k;
			k=0;
			while(n)
			  {
			  k+=(n%a[j])*(n%a[j]);
			  n/=a[j];
			  }
			}
		  if(k>1) l=1;
		  }
		}
	  printf("%ld\n",i-1);
	  }
	}
