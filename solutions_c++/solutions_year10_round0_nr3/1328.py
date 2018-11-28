#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t,r,k,n,g[20];

int main()
{
	FILE *input=fopen("c.in","r");
	FILE *output=fopen("c.out","w");
	fscanf(input,"%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		fscanf(input,"%d%d%d",&r,&k,&n);
		int p=1,ans=0;
		for (int i=1;i<=n;i++)
		{
			fscanf(input,"%d",&g[i]);
			ans+=g[i];
		}
		if (ans<=k)
			fprintf(output,"Case #%d: %d\n",tt,ans*r);
		else
		{
			ans=0;
			for (int i=1;i<=r;i++)
			{
				int x=0;
				while (x+g[p]<=k)
				{
					x+=g[p];
					p++;
					if (p>n) p=1;
				}
				ans+=x;
			}
			fprintf(output,"Case #%d: %d\n",tt,ans);
		}
	}
	fclose(input);
	fclose(output);
	return 0;
}