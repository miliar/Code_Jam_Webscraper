#include <cstdio>

int T, L, t, N, C;

int dist[1000010];
int acc[1000010];

int main()
{
	scanf("%d ", &T);
	for(int _42 = 1; _42 <= T; ++_42) {
		scanf("%d %d %d %d ", &L, &t, &N, &C);

		for(int i = 0; i < C; ++i) {
			scanf("%d ", &dist[i]);
		}

		int time = 0;
		acc[0] = 0;
		for(int i = 0; i < N; ++i) {
			time += 2*dist[i%C];	
			acc[i+1] = time;
		}

		int mintime = time;
		if(L > 0) {
			for(int i = 0; i < N; ++i) {
//				printf("acc[%d]:%d\n", i, acc[i]);
				int newtime1 = time;
				if(acc[i] >= t)	newtime1 -= dist[i%C];
				else if(acc[i+1] >= t) newtime1 -= (acc[i+1]-t)/2;
				if(newtime1 < mintime) mintime = newtime1;
				if(L > 1) {
					for(int j = i+1; j < N; ++j) {
						int newtime2 = newtime1;
						if(acc[j] >= t) newtime2 -= dist[j%C];
						else if(acc[j+1] >= t) newtime2 -= (acc[i+1]-t)/2;
						if(newtime2 < mintime) mintime = newtime2;
					}
				}
			}
		}

		printf("Case #%d: %d\n", _42, mintime);
	}
	return 0;
}
