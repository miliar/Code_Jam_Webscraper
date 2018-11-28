
#include <cstdio>
#include <string.h>

using namespace std;

int R, k, N;
int g[1000];
int next[1000];
long long total[1000];
bool visited[1000];

long long solve() {
	for(int i = 0; i < N; i++) {
		total[i] = 0;
		next[i] = i;
		for(int j = 0; j < N; j++) {
			int i2 = (i + j) % N;
			long long t2 = total[i] + g[i2];
			if(t2 > k) {
				next[i] = i2;
				break;
			}
			total[i] = t2;
		}
	}

	memset(visited, 0, sizeof(visited));
	long long res = 0;
	int i = 0;
	int numVisited = 0;
	while(true) {
		if(visited[i])
			break;

		numVisited++;
		res += total[i];
		visited[i] = true;
		if(numVisited == R)
			return res;

		i = next[i];
	}

	int cycleLength = 0;
	long long cycleTotal = 0;
	int j = i;
	while(true) {
		cycleLength++;
		cycleTotal += total[i];
		i = next[i];

		if(i == j)
			break;
	}

	int cycles = (R - numVisited) / cycleLength;
	res += cycleTotal * cycles;
	//printf("%d %d %d %lld\n", j, cycles, cycleLength, cycleTotal);

	for(j = 0; j < ((R - numVisited) % cycleLength); j++) {
		res += total[i];
		i = next[i];
	}

	return res;
}

int main() {
	FILE *fin = fopen("C-large.in", "r");
	FILE *fout = fopen("C-out.txt", "w");

	int T;
	fscanf(fin, "%d", &T);
	for(int t = 1; t <= T; t++) {
		fscanf(fin, "%d%d%d", &R, &k, &N);
		for(int i = 0; i < N; i++)
			fscanf(fin, "%d", &g[i]);

		fprintf(fout, "Case #%d: %lld\n", t, solve());
	}

	return 0;
}
