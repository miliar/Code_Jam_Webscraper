#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>

using namespace std;

const int N = 1024;

int min(int a, int b)
{
	return a < b ? a : b;
}

int max(int a, int b)
{
	return a > b ? a : b;
}

int r[N];

bool cmp(int a, int b)
{
	return r[a] > r[b];
}

int main()
{
	//freopen("B-small-attempt4.in", "r", stdin);
	//freopen("B-small.out", "w", stdout);
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int i, j, k;
	int cas;
	int T;
	
	int ind[N];
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		int n, w, l;
		scanf("%d %d %d", &n, &w, &l);
		for(i = 0; i < n; i ++)
		{
			scanf("%d", &r[i]);
			ind[i] = i;
		}
		sort(ind, ind+n, cmp);
		int x = 0;
		int y = 0;
		int recx[N], recy[N];
		
		bool flag = false;
		for(i = 0; i < n; i ++)
		{
			if(y > w)y = 0;
			x = 0;
			int recj = -1;
			bool ok = true;
			while(ok)
			{
				x = 0;
				recj = -1;
				for(j = 0; j < i; j ++)
				{
					if(abs(recy[ind[j]] - y) < r[ind[j]]+r[ind[i]] && recx[ind[j]] + r[ind[j]] + r[ind[i]] > x)
					{
						x = recx[ind[j]] + r[ind[j]] + r[ind[i]];
						if(x > l)recj = j;
					}
				}
				if(recj == -1)break;
				y = recy[ind[recj]] + r[ind[recj]] + r[ind[i]];
				if(y > w)ok = false;
			}
			if(!ok)break;
			recx[ind[i]] = x;
			recy[ind[i]] = y;
			y += r[ind[i]];
			if(i+1 < n)y += r[ind[i+1]];
		}
		for(i = 0; i < n; i ++)
		{
			if(recy[i] > w || recx[i] > l)puts("fuck1");
			for(j = 0; j < i; j ++)
			{
				double dx = (recx[i]-recx[j]);
				double dy = (recy[i]-recy[j]);
				double dis = sqrt(dx*dx+dy*dy);
				if(dis < r[i]+r[j])printf("\nfuck2 %d %d %d %d (%d,%d) (%d,%d)\n", i, j, r[i], r[j], recx[i], recy[i], recx[j], recy[j]);
			}
		}
		printf("Case #%d:", cas);
		for(i = 0; i < n; i ++)
		{
			printf(" %d %d", recy[i], recx[i]);
		}
		putchar('\n');
	}
	return 0;
}
