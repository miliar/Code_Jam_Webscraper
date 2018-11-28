#include <cstdio>
#include <algorithm>
using namespace std;

const int maxN = 2000;

int testCases;
int R, K, N;
int num[maxN];

long long ans;

int next[maxN], value[maxN];
int road[maxN], numRoad;
bool visit[maxN];

FILE *fin, *fou;
char name[] = "E:\\Tdownload\\c1";
//char name[] = "a";

void calc( int cases)
{
	fscanf(fin, "%d %d %d", &R, &K, &N);
	for (int i = 0; i < N; i++) fscanf(fin, "%d", &num[i]);

	ans = 0;
	memset(visit, 0, sizeof visit);
    
	numRoad = 0;

    for (int r = 0; r < N; r++)
	{
		int sum = 0;
	
		int k = r;
		while (k < N && sum + num[k] <= K) sum += num[k++];

		if ( k == N)
		{
			k = 0;
			while (k < r && sum + num[k] <= K) sum += num[k++];
		}
		
		next[r] = k;
		value[r] = sum;
	}

	numRoad = 1;
	road[0] = 0;
	visit[0] = true;

	int numTour = 0;
	int now = 0;

	while (numTour < R)
	{
		++numTour;
		road[numRoad++] = next[now];
		ans = ans + value[now];
		now = next[now];
		if (visit[now]) break; else visit[now] = true;
	}

    if ( numTour < R)
	{
		int id = 0;
		while (road[id] != now) ++id;

		int circle = numRoad - 1 - id;
		long long circleSum = 0;
		for (int r = id; r < numRoad -1; r++) circleSum += value[road[r]];

		ans = ans + (long long)(( R - numTour) / circle) * circleSum;
		R = (R - numTour) % circle;
		for (int r = id; r < id + R; r++) ans = ans + value[road[r]];  // note value[road[r]] not value[r]
	}

	fprintf(fou, "Case #%d: %lld\n", cases, ans);
}

int main()
{
	char input[100];
	strcpy(input, name);
	strcat(input, ".in");
	
	char output[100];
	strcpy(output, name);
	strcat(output, ".out");

	fin = fopen(input, "r");
	fou = fopen(output, "w");

    fscanf(fin, "%d", &testCases);
	for (int cases = 0; cases < testCases; cases++) calc(cases + 1);

	fclose(fin);
	fclose(fou);
	return 0;
}
