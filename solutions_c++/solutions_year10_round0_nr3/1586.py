#include <cstdio>
using namespace std;
typedef long long INT;
const int N = 1010;
int r, k, n;
int gr[N];
int next[N];
int nsum[N];		//sum we get moving this groups
int last[N];		//last step we were here
INT sum_last[N];	//sum we had on last step we were here

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
		
	int numt;
	scanf("%d", &numt);
	for(int it=0;it<numt;it++)
	{
		//input
		scanf("%d%d%d", &r, &k, &n);
		for(int i=0;i<n;i++)
		{
			scanf("%d", &gr[i]);
		}
		//precalc next
		for(int i=0;i<n;i++)
		{
			int sum = gr[i];
			int j = (i+1)%n;
			while(j!=i && sum+gr[j]<=k)
			{
				sum += gr[j];
				j = (j+1)%n;
			}
			next[i] = j;
			nsum[i] = sum;
		}
	
		for(int i=0;i<n;i++) last[i] = -1;
		
		int step = 0;
		int pos = 0;
		INT sum = 0;
		int rs = r;
		while(rs>0)
		{
			if( last[pos]!=-1 )
			{
				int dist = step-last[pos];
				INT delta_sum = sum-sum_last[pos];
				int rtimes = rs/dist;
				rs = rs%dist;
				sum += delta_sum*rtimes;
				for(int i=0;i<n;i++) last[i] = -1;
			}
			else
			{
				sum_last[pos] = sum;
				last[pos] = step;
				sum += nsum[pos];
				pos = next[pos];
				rs--;
				step++;
			}
		}
		printf("Case #%d: %lld\n", it+1, sum);
	}

	fclose(stdout);
	return 0;
}