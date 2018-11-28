#include <stdio.h>

void process(int Problem)
{
	__int64 cycle = 0;
	__int64 cnt = 0;
	__int64 result = 0;
	__int64 check_cycle[1000] = {0};
	__int64 init_cycle = 0;
	int st_idx;
	int idx = 0;
	int cycle_count = 0;
	int data[1000];
	bool visited[1000] = {0};
	int cycle_cnt[1000] = {0};
	int start_init_cycle = 0;
	int r, k, n;
	
	scanf("%d %d %d", &r, &k, &n);
	for(int i=0; i<n; i++)
	{
		scanf("%d", &data[i]);
	}
	while(!visited[idx])
	{
		visited[idx] = true;
		cycle_cnt[idx] = cycle_count;
		check_cycle[idx] = cycle;
		st_idx = idx;
		cnt += (__int64)data[idx];
		idx = (idx+1)%n;
		for(;st_idx != idx;idx = (idx+1)%n)
		{
			if( cnt+(__int64)data[idx] > (__int64)k )
				break;
			cnt += (__int64)data[idx];
		}
		cycle += cnt;
		cycle_count++;
		cnt = 0;
	}
	
	init_cycle = check_cycle[idx];
	start_init_cycle = cycle_cnt[idx];
	cycle -= init_cycle;
	cycle_count -= start_init_cycle;

	if( r < start_init_cycle ) 
	{
		idx = 0;
	}
	else
	{
		result = (__int64)init_cycle;
		r -= start_init_cycle;

		result += (__int64)(r/cycle_count)*cycle;
		r %= cycle_count;
	}
	
	
	for(;r>0; r--)
	{
		for(;;idx = (idx+1)%n)
		{
			if( cnt+(__int64)data[idx] > (__int64)k )
				break;
			cnt += (__int64)data[idx];
		}
		result += cnt;
		cnt=0;
	}

	printf("Case #%d: %I64d\n", Problem, result);
}
void main()
{
	freopen("input.txt","r", stdin);
	freopen("output.txt","w", stdout);

	int T;
	scanf("%d", &T);
	for(int i=1; i<=T; i++)
	{
		process(i);
	}
}