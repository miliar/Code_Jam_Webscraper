#include <iostream>
using namespace std;
typedef __int64 lint;
lint sum[2011];
int a[2011];
int main()
{
	int t, n, k, r, i, j, cas = 0;
	lint K;
	lint res;
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	scanf("%d",&t);
	while(t--)
	{
		res = 0;
		scanf("%d %d %d", &r, &k, &n);
		K = k;
		sum[0] = 0;
		for(i = 1; i <= n; i ++)
		{
			scanf("%d", &a[i]);
			a[n + i]  = a[i];
			sum[i] = sum[i-1] + a[i];
		}
		for(i = n + 1; i <= 2 * n; i ++)
			sum[i] = sum[i-1] + a[i];
		int left = 0, right, index = 0, mid, nindex;
		for(i = 1; i <= r; i ++)
		{
			left = index + 1;
			right = index + n;
			nindex = -1;
			while(left <= right)
			{
				mid = (left + right) >> 1;
				if(sum[mid] - sum[index] <= K)
				{
					nindex = mid;
					left = mid + 1;
				}
				else 
				{
					right = mid - 1;
				}
			}
			if(nindex == -1)
				break;
			res += sum[nindex] - sum[index];
			if(nindex > n)
				index = nindex - n;
			else index = nindex;
		}
		printf("Case #%d: %I64d\n",++cas, res);
	}
}