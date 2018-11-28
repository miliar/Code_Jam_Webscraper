#include <iostream>
#include <string>

using namespace std;

int main()
{
	int i, j, k;
	int tc, t, n, m;
	int ans;
	int a[10000], b[1000];
	//freopen("D:\\VC2005\\google\\2010\\R1C\\A-small.in","r",stdin);
	//freopen("D:\\VC2005\\google\\2010\\R1C\\A-small.out","w",stdout);
	freopen("D:\\VC2005\\google\\2010\\R1C\\A-large.in","r",stdin);
	freopen("D:\\VC2005\\google\\2010\\R1C\\A-large.out","w",stdout);

	scanf("%d\n", &tc);
	for(t=1;t<=tc;t++)
	{
		scanf("%d\n", &n);
		for(i=0;i<n;i++) scanf("%d %d\n", &a[i], &b[i]);

		ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(a[i]>a[j] && b[i]<b[j]) ans++;
				else if(a[i]<a[j] && b[i]>b[j]) ans++;
			}
		}

		printf("Case #%d: %d\n", t, ans);
	}

	fclose(stdout);
	return 0;
}
