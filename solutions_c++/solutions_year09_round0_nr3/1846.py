//Q2009 pC
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define wlen 19
template <class T> void swap ( T& a, T& b )
{
  T c(a); a=b; b=c;
}
int main()
{
	bool p[128]={0};
	char t[]="welcome to code jam";
	char str[505];
	int dp1[505],dp2[505],*d1=dp1,*d2=dp2;
	int x,y,l,a,n,loc,s,m;
	FILE *fin=fopen("C-small.in","r"), *fout=fopen("C-small.out","w");
	for(x=0;x<wlen;++x)
		p[t[x]]=1;
	fscanf(fin,"%d",&n);
	fgets(str,504,fin);
	for(a=1;a<=n;++a)
	{
		memset(dp1,0,sizeof(dp1));
		memset(dp2,0,sizeof(dp2));
		fgets(str,504,fin);
		l=strlen(str);
		for(x=loc=0;x<l;++x)
		{
			if(p[str[x]])
				str[loc++]=str[x];
		}
		str[loc]='\0';
		l=strlen(str);
		for(x=0;x<l;++x)
		{
			if(str[x]==t[0])
				d1[x]=1;
			else
				d1[x]=0;
		}
		m=0;
		for(y=1;y<wlen;++y)
		{
			s=m=0;
			for(x=y;x<l;++x)
			{
				if(d1[x-1])
					s=(s+d1[x-1])%10000;
				if(str[x]==t[y])
				{
					d2[x]=s;
					m=(m+s)%10000;
				}
				else
					d2[x]=0;
			}
			swap(d1,d2);
		}
		fprintf(fout,"Case #%d: %04d\n",a,m);
	}
	return 0;
}
