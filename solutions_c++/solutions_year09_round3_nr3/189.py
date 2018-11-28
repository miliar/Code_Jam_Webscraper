#include <cstdio>
#include <climits>
#include <algorithm>
#define MAX 105

using namespace std;

int ncases, npris, ncells, cells[MAX], memo[MAX][MAX];

int gocomp(int a, int b)
{
	if(memo[a][b]) return memo[a][b];
	if(a>b) return 0;
		
	int mincost=INT_MAX;
	for(int i=a; i<=b; i++)
		mincost=min(mincost, cells[b+1]-cells[a-1]-2 + gocomp(a, i-1) + gocomp(i+1, b));
	
	memo[a][b]=mincost;
	return mincost;
}

int main()
{
	scanf("%d", &ncases);
	for(int i=0; i<ncases; i++)
	{
		memset(memo, 0, sizeof(memo));
		scanf("%d %d", &npris, &ncells);
		cells[0]=0;
		cells[ncells+1]=npris+1;
		for(int j=0; j<ncells; j++)
			scanf("%d", &cells[j+1]);
		
		printf("Case #%d: %d\n", i+1, gocomp(1, ncells));
	}
	return 0;
}