#include <cstdio>
#include <map>
#include <vector>
#include <string>
#include <limits.h>
#include <cstring>

using namespace std;
vector<int> queries;
map<string,int> id2int;
char engines[100][120];
char engine[120];
int S;
int cache[100][1000];

int solve (int current_engine, int current_query) {
	if (cache[current_engine][current_query] != -1)
		return cache[current_engine][current_query];
	if (current_query == -1) return 0;

	int local_min = INT_MAX;

	for (int i = 0; i < S; i++) {
		if (i == queries[current_query]) continue;
		
		local_min = min(local_min, solve (i, current_query-1) + (current_engine==i?0:1));

	}
	return cache[current_engine][current_query] = local_min;
}

int main () {
	int N;

	scanf ("%d",&N);

	for (int k = 0; k < N; k++) {
		int Q;
		id2int.clear();
		queries.clear ();
		memset (cache, -1, sizeof(cache));
		scanf ("%d\n",&S);
		for (int i = 0; i < S; i++) {
			fgets (engines[i], sizeof(engines[i]), stdin);
			id2int[engines[i]] = i;
		}
		scanf ("%d\n",&Q);
		for (int i = 0; i < Q; i++) {
			fgets (engine, sizeof(engines[i]), stdin);
			queries.push_back (id2int[engine]);
		}
		int local_min = INT_MAX;
		if (S != 0 && Q != 0)
		for (int i = 0; i < S; i++)
		{
			if (i != queries[Q-1])
				local_min = min (local_min, solve(i, Q-1));
		}
		else local_min = 0;
		printf ("Case #%d: %d\n",k+1,local_min);
	}
	return 0;
}
