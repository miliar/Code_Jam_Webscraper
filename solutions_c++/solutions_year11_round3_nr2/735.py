#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main ()
{
	int T, L, t, N, C, index = 0, sum, mark, total_journey, time, stations_left;
	scanf("%d", &T);
	
	while (T--)
	{
		index++;
		sum = 0;
		total_journey = 0;
		time = 0;
		scanf("%d", &L);
		scanf("%d", &t);
		scanf("%d", &N);
		scanf("%d", &C);
		
		int dist[N+1];
		int a[C];
		dist[0] = 0;
		for (int i=0; i<C; i++)
		{
			scanf("%d", &a[i]);
		}
		
		for (int i=0; i<C; i++)
		{
			for (int k=0; k*C+i+1<=N; k++)
			{
				dist[k*C+i+1] = a[i];
				total_journey += a[i];
			}
		}
		
		if (L == 0)
		{
			printf("Case #%d: %d\n", index, 2 * total_journey);
			continue;
		}
		
		mark = N;
		for (int i=0; i<=N; i++)
		{
			if (sum >= t/2)
			{
				mark = i - 1;
				break;
			}
			
			else
				sum += dist[i];
		}
		
		if (mark == N)
		{
			if (sum <= t/2)
				time = 2 * total_journey;
			else
				time = t + (total_journey-t/2);
		}
		
		else
		{
			int left[N-mark+1];
			left[0] = sum - t/2;
			for (int i=mark+1; i<=N; i++)
				left[i-mark] = dist[i];
			
			sort (left, left+N-mark+1);
			stations_left = N - mark + 1;
			
			int rest = 0;
			for (int i=0; i<L && stations_left > 0; i++, stations_left--)
				rest += left[N-mark-i];
			
			time = total_journey*2 - rest;
		}
		
		printf("Case #%d: %d\n", index, time);
	}
	
	return 0;
}
