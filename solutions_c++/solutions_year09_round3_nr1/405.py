#include <stdio.h>
#include <string.h>
  int main()
	{
	long T,I,i,l,a[256],s;
	long long n;
	char st[99];
	scanf("%ld",&T);
	for(I=1;I<=T;I++)
	  {
	  printf("Case #%ld: ",I);
	  scanf("%s",&st);
	  l=strlen(st);
	  memset(a,0,sizeof(a));
	  a[st[0]]=1;
	  s=1;
	  for(i=1;i<l;i++)
		if(!a[st[i]]) {
					  a[st[i]]=99;
					  break;
					  }
	  for(;i<l;i++)
		if(!a[st[i]]) {
					  s++;
					  a[st[i]]=s;
					  }
	  s++;
	  n=0;
	  for(i=0;i<l;i++)
		if(a[st[i]]==99) n=n*s;
					else n=n*s+a[st[i]];
	  printf("%lld\n",n);
	  }
	}
