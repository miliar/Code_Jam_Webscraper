#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

int N, n;
int S, s;
int Q, q;

char str[200];

vector <string> engine;
vector <string> query;

int dp[100][1000];
int j, i;

int main() {

	//FILE *in = fopen("A-small.in", "rt");
	//FILE *out = fopen("A-small.out", "wt");

	FILE *in = fopen("A-large.in", "rt");
	FILE *out = fopen("A-large.out", "wt");


	fgets(str, 199, in);
	sscanf(str, "%d", &N);

	for (n = 1; n <= N; n++) {

		engine.clear();
		query.clear();

		fgets(str, 199, in);
		sscanf(str, "%d", &S);

		for (s = 0; s < S; s++) {
			fgets(str, 199, in);
			string en = str;
			engine.push_back(en);
		}

		fgets(str, 199, in);
		sscanf(str, "%d", &Q);

		if (Q == 0) {
			fprintf(out, "Case #%d: %d\n", n, 0);
			continue;
		}

		for (q = 0; q < Q; q++) {
			fgets(str, 199, in);
			string en = str;
			query.push_back(en);
		}

		for (s = 0; s < engine.size(); s++) {
			if (engine[s].compare(query[Q-1]) == 0)
				dp[s][0] = 1;
			else
				dp[s][0] = 0;
		}		
		
		int pmin = 1000000;
		for (q = Q - 2; q >= 0; q--) {
			j = Q - 1 - q;
			for (s = 0; s < engine.size(); s++) {
				if (engine[s].compare(query[q]) == 0) {
					int pmin = 10000000;
					for (i = 0; i < S; i++) {
						if (i == s) continue;
						if (dp[i][j-1] < pmin) pmin = dp[i][j-1];
					}
					dp[s][j] = pmin + 1;
				} else {
					dp[s][j] = dp[s][j-1];
				}
			}
		}
		
		pmin = dp[0][Q-1];
		for (s = 1; s < S; s++) {
			if (dp[s][Q-1] < pmin) pmin = dp[s][Q-1];
		}			

		fprintf(out, "Case #%d: %d\n", n, pmin);
	}
	
	fclose(in);
	fclose(out);

	return 0;
}