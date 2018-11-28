#include <cstdio>
#include <cstring>
#include <iostream>

int T;
int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t ++)
	{
		int R, K, N;
		scanf("%d %d %d", &R, &K, &N);
		int g[N];
		for(int i = 0; i < N; i ++)
			scanf("%d", &g[i]);
		for(int i = 0; i < N; i ++)
			fprintf(stderr, "%d ", g[i]);
		fprintf(stderr, "\n");
		long long to[N + 1];
		int first = 0;
		int round = 1;
		int pos[N];
		memset(to, 0, sizeof(to));
		memset(pos, -1, sizeof(pos));
		while(true)
		{
			fprintf(stderr, "%d\n", first);
			if( pos[first] != -1 )
				break;
			pos[first] = round;
			long long cur = 0;
			int j = first;
			while( true )
			{
				if( cur + g[j] > K )
					break;
				cur += g[j];
				j ++;
				if(j == N)
					j = 0;
				if(j == first)
					break;
			}
			to[round] = to[round - 1] + cur;
			round ++;
			first = j;
		}
		for(int i = 0; i < round; i ++)
			fprintf(stderr, "%d ", to[i]);
		fprintf(stderr, "\n");
		for(int i = 0; i < round; i ++)
			fprintf(stderr, "%d ", pos[i]);
		fprintf(stderr, "\n");
		
		int before = pos[first] - 1;
		int cycle = round - 1 - before;
		fprintf(stderr, "cycle length: %d\n", cycle);
		long long all = 0;
//		all = to[before];
		fprintf(stderr, "add before: %d\n", all);
		int times = (R - before) / cycle;
		all += times * (to[round - 1] - to[before]);
		fprintf(stderr, "%d %d\n", to[round - 1], to[before]);
		R -= times * cycle;
		all += to[R];
		std :: cout << "Case #" << t << ": " << all << "\n";
	}
}
