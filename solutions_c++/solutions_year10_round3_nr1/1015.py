#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef pair<int,int> pp;

int x[1010];
int y[1010];


int main()
{
	int nn;
	scanf("%d",&nn);
	for (int ii=1;ii<=nn;ii++)
	{
		int n;
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf("%d%d",x+i,y+i);
		int ans=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				if (x[i]<x[j] && y[i]>y[j])
					ans++;
		printf("Case #%d: %d\n",ii,ans);		
	}
	return 0;
}