#include <stdio.h>
#include <iostream.h>
#include <string.h>
  int main()
	{
	long T,I,i,a[10],l,j,p,m,q;
	char st[25];
	scanf("%ld",&T);
	gets(st);
	for(I=1;I<=T;I++)
	  {
	  printf("Case #%ld: ",I);
	  gets(st);
	  memset(a,0,sizeof(a));
	  l=strlen(st);
	  for(i=0;i<l;i++)
		a[st[i]-48]++;
	  for(i=l-1;i>0;i--)
		if(st[i]>st[i-1]) {
						  p=i;
						  break;
						  }
	  if(!i) {
			 j=57;
			 for(i=0;i<l;i++)
			   if((st[i]<j)&&(st[i]>48)) {
										 j=st[i];
										 p=i;
										 }
			 printf("%c0",j);
			 st[p]=58;
			 for(i=0;i<l-1;i++)
			   for(j=i+1;j<l;j++)
				 if(st[i]>st[j]) swap(st[i],st[j]);
			 for(i=0;i<l-1;i++)
			   printf("%c",st[i]);
			 printf("\n");
			 continue;
			 }
	  m=58;
	  p--;
	  for(i=l-1;i>p;i--)
		if((st[i]<m)&&(st[i]>st[p])) {
									 m=st[i];
									 q=i;
									 }
	  swap(st[p],st[q]);
	  for(i=p+1;i<l-1;i++)
		for(j=i+1;j<l;j++)
		  if(st[i]>st[j]) swap(st[i],st[j]);
	  for(i=0;i<l;i++)
		printf("%c",st[i]);
	  printf("\n");
	  }
	}
