#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int dynamic[10001][2], N, V, iLimit;
bool isVisit[10001][2];

typedef struct _data
{
	bool bValue, op, isCAble;
} Dat;

Dat data[10001];

int getDynamic(int cur, int target);

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int q=1;q<=T;q++)
	{
		for(int i=0;i<10001;i++) dynamic[i][0]=dynamic[i][1]=10000;
		memset(isVisit, false, sizeof(isVisit));

		scanf("%d %d", &N, &V);
		iLimit=(N-1)/2;
		for(int i=1;i<=(N-1)/2;i++)
		{
			int temp[2];
			scanf("%d %d", temp, temp+1);
			data[i].op=temp[0], data[i].isCAble=temp[1];
		}

		for(int i=(N-1)/2+1;i<=N;i++)
		{
			int temp;
			scanf("%d", &temp);
			data[i].bValue=temp;
		}

		int ans=getDynamic(1, V);
		
		printf("Case #%d: ", q);
		if(ans>=10000) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}

	return 0;
}
		
int getDynamic(int cur, int target)
{
	int &ret=dynamic[cur][target];
	if(isVisit[cur][target]) return ret;
	isVisit[cur][target]=true;

	if(cur>iLimit)
	{
		if(data[cur].bValue==target) ret=0;
		else ret=10000;
	}
	else
	{
		ret=10000;
		if(target==0)
		{
			if(data[cur].op)
			{
				ret=getDynamic(cur*2, 0);
				ret=min(ret, getDynamic(cur*2+1, 0));
			}
			else 
			{
				ret=getDynamic(cur*2, 0) + getDynamic(cur*2+1, 0);
				if(data[cur].isCAble)
				{
					ret=min(ret, getDynamic(cur*2, 0)+1);
					ret=min(ret, getDynamic(cur*2+1, 0)+1);
				}
			}
		}
		else
		{
			if(data[cur].op)
			{
				ret=getDynamic(cur*2, 1)+getDynamic(cur*2+1, 1);
				if(data[cur].isCAble)
				{
					ret=min(ret, getDynamic(cur*2, 1)+1);
					ret=min(ret, getDynamic(cur*2+1, 1)+1);
				}
			}
			else
			{
				ret=getDynamic(cur*2, 1);
				ret=min(ret, getDynamic(cur*2+1, 1));
			}
		}
	}

	return ret;
}
				