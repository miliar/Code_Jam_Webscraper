#include<iostream>

using namespace std;

int d[64];
char buf[128];

int main()
{
	freopen("G:\\source\\oi_acm\\google\\gcj2009\\round 2\\A\\A-large.in","r",stdin);
	freopen("G:\\source\\oi_acm\\google\\gcj2009\\round 2\\A\\A-large.out","w",stdout);
	int T,tt,n;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&n);getchar();
		for(int i=0;i<n;i++)
		{
			scanf("%s",buf);getchar();
			d[i]=n;
			while(d[i]>0&&buf[d[i]-1]=='0')
				d[i]--;
		}
		int ans = 0;
		for(int i=0;i<n;i++)
		{
			if (d[i]<=i+1) continue;
			int j = i+1;
			while(d[j]>i+1) j++;
			for(int k=j;k>=i+1;k--)
			{
				int t = d[k];
				d[k]=d[k-1];
				d[k-1]=t;
				ans++;
			}
		}

		printf("Case #%d: %d\n",tt,ans);
	}

	return 0;
}
