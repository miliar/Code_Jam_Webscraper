#include <iostream>

using namespace std;
struct line
{
	int x;
	int y;
}l[1005];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	int n;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d%d",&l[i].x,&l[i].y);
		int count = 0;
		for(int i=0;i<n-1;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				if((l[i].x-l[j].x)*(l[i].y-l[j].y)<0)
					count++;
			}
		}
		printf("Case #%d: %d\n",cs,count);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}