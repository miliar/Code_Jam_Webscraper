#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

__int64 i,j,z,q,T,ts,k,n;
int b[1000],a[1000];
char s[1000];

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%I64d",&T);
	while(T--)
	{
		scanf("%s",&s);
		k=0;
		for(i=0;s[i];i++)
			if(s[i]=='?')
				a[k++]=i;
			else
				b[i]=s[i]-'0';
		n=i;
		for(i=0;i<(1<<k);i++)
		{
			for(j=0;j<k;j++)
				if(i&(1<<j))
					b[a[j]]=1;
				else
					b[a[j]]=0;
			z=0;
			for(j=0;j<n;j++)
				z=z*2+b[j];
			q=sqrt(1.0*z);
			for(j=q-5>0?q-5:1;j<q+5;j++)
				if(j*j==z)
					break;
			if(j<q+5)
				break;
		}
		printf("Case #%d: ",++ts);
		for(i=0;i<n;i++)
			printf("%d",b[i]);
		printf("\n");
	}
	return 0;
}