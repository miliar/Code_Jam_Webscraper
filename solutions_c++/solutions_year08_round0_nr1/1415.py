#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <string.h>
using namespace std;

map<string,int>cot;

int T,N,S,Q,i,ans,j,k,t,a[1020],h[200],len;
char s[200];

int main()
{
	scanf("%d",&T);
	for (N=1;N<=T;N++)
	{
		scanf("%d",&S);
		gets(s);
		cot.clear();
		memset(a,0,sizeof(a));

		for (i=0;i<S;i++)
		{
			gets(s);
			cot[s]=i;
		}
		scanf("%d",&Q);
		gets(s);

		len=0;
		for (i=0;i<Q;i++)
		{
			gets(s);
			k=cot[s];
			if (i==0 || k!=a[len-1])
			{
			    a[len]=k;
				len++;
			}
		}
		
		ans=0;
		memset(h,0,sizeof(h));
		for (i=0;i<len;i++)
		{
			h[a[i]]=1;
			k=1;
			for (j=0;j<S;j++)
				if (h[j]==0) k=0;
		    if (k==1)
			{
				memset(h,0,sizeof(h));
				h[a[i]]=1;
				ans++;
			}
		}
		
		printf("Case #%d: %d\n",N,ans);
	}
	return 0;
}
