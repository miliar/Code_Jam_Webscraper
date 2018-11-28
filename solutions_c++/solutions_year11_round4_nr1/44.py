#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


int TRIALS;



void trial(int T)
{
	int dist[101];
	memset(dist, 0, sizeof(dist));
	printf("Case #%d: ", T);
	int X; int S; int R; int t; int N;
	scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);
	for (int i = 0; i < N; i++)
	{
		int B; int E; int w;
		scanf("%d %d %d", &B, &E, &w);
		X -= (E-B);
		dist[w] += (E-B);
	}
	dist[0] += X;
	double run = (double)t;
	double time = 0.0;
	for (int i = 0; i <= 100; i++)
	{
		double runtime = (double) dist[i] / (i + R);
		if (runtime > run) runtime = run;
		time += runtime + (dist[i] - runtime*(i+R)) / (i+S);
		run -= runtime;
	}
	printf("%f\n", time);
}

int main(int argc, char* argv[])
{
	scanf("%d", &TRIALS);
	for (int T = 1; T <= TRIALS; T++)
	{
		trial(T);
	}
	
	return 0;
}