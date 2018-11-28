#include <iostream>
#include <Cstring>
#include <stdio.h>
using namespace std;
main()
{
	int i,j,k,m,n,s,q,re,f[101],flag,t[1001];
	char a[101][100],b[1001][100];
	cin >>n;
	for(m=0;m<n;m++)
	{
		cin >>s;
		gets(a[0]);
		for(i=0;i<s;i++)
			gets(a[i]);
		cin >>q;
		gets(b[0]);
		for(i=0;i<q;i++)
			gets(b[i]);
		memset(t,0,sizeof(t));
		for(i=0;i<=q;i++)
			for(j=0;j<s;j++)
				if(strcmp(b[i],a[j])==0)t[i]=j;
		re=0;i=0;flag=s;
		memset(f,0,sizeof(f));
		while(i<q)
		{
			if(!f[t[i]])
			{
				flag--;
				f[t[i]]=1;
			}
			if(flag==0)
			{
				flag=s-1;
				memset(f,0,sizeof(f));
				f[t[i]]=1;
				re++;
			}
			i++;
		}
		printf("Case #%i: %i\n",m+1,re);
	}
}

