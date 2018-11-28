#include <iostream>

#define minx(a, b) a < b ? a : b

using namespace std;

long t;
long long r, k, n;
long haha;
long long g[1001];
long long sum[1001];
bool mark[1001];
long hah[1001];

void work()
{
	for(long i = 1; i <= t; i++)
	{
		scanf("%ld%ld%ld", &r, &k, &n);
		for(long j = 1; j <= n; j++)
			scanf("%d", &g[j]);
        memset(sum, 0, sizeof(sum));
		memset(mark, 0, sizeof(mark));
		memset(hah, 0, sizeof(hah));
		long beg = 1;
		long j = 1, l = 1;
		while(1)
		{
			if(!mark[beg])
            { 
                mark[beg] = 1;
                hah[beg] = l;
            }
            else 
            {   
                haha = hah[beg];
                break;
            }
            long long  s= 0;
			j = beg;
			while(1)
			{
				if(s + g[j] <= k)
				{
					s += g[j];
					j++;
				    if(j > n) j = 1;
				    if(j == beg)
				    {
                        sum[l] = s;
					    l++;
					    break;
                    }
                }
				else
				{
					sum[l] = s;
					l++;
					beg = j;
					break;
				}
			}
		}
		long long ans = 0;
		l--;
		long xunhuanjie = 0;
		for(j = haha; j <= l; j++)
		  xunhuanjie += sum[j];
        
        int end = minx(r, haha - 1);
		for(j = 1; j <= end; j++)
			ans += sum[j];
        long pos = haha;
		for(; j <= r; j++)
		{
			ans += sum[pos];
			pos++;
			if(pos > l) pos = haha;
		}
		
        printf("Case #%d: %I64d\n", i, ans);
    }
}

int main()
{
	freopen("3.in", "r", stdin);
	freopen("3.out", "w", stdout);
	scanf("%ld", &t);
	work();
	return 0;
}
