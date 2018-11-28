#include "iostream.h"
  int main()
    {
    int d,T,i,j,k,l,o,s,ii,len,a[5001];
	char t[999],st[5001][999],b[5001][999];
	scanf("%ld%ld%ld",&len,&d,&T);
	gets(t);
	for(i=0;i<d;i++)
	  gets(st[i]);
	for(ii=1;ii<=T;ii++)
	  {
	  printf("Case #%ld: ",ii);
	  gets(t);
	  l=strlen(t);
	  j=-1;
	  o=1;
	  for(i=0;i<l;i++)
		if(t[i]=='(') {
					  j++;
					  s=0;
					  o=0;
					  }
				 else if(t[i]==')') {
									a[j]=s;
									o=1;
									}
							   else if(o) {
										  j++;
										  a[j]=1;
										  b[j][0]=t[i];
										  }
									 else {
										  b[j][s]=t[i];
										  s++;
										  }
	  s=0;
	  for(i=0;i<d;i++)
		{
		for(j=0;j<len;j++)
		  {
		  o=0;
		  for(k=0;k<a[j];k++)
			if(st[i][j]==b[j][k]) {
								  o=1;
								  break;
								  }
		  if(!o) break;
		  }
		if(j==len) s++;
		}
	  printf("%ld\n",s);
      }
    }
