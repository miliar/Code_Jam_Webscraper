#include <cstdio>
#include <algorithm>
using namespace std;

int T, n, na, sum;
int con[200];
int sorted[200];
double level;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &T);
	for(int cnt=1; cnt<=T; ++cnt)
	{
		scanf("%d", &n);
		sum = 0;
		for(int i=0; i<n; ++i)
		{
			scanf("%d", &con[i]);
			sorted[i] = con[i];
			sum += con[i];
		}
		sort(sorted, sorted+n);
		int a = sum, i = 0;
		for(i=0; i<n-1; ++i)
		{
			int now = (sorted[i+1]-sorted[i])*(i+1);
			if(now<=a) a-=now;
			else break;
		}
		level = sorted[i] + (double)a/(i+1);
		printf("Case #%d:", cnt);
		for(int i=0; i<n; ++i) printf(" %.6lf", 100*(max(0.0, (level-con[i])/sum)));
		puts("");
	}
	return 0;
}
