#include <cstdio>
#include <algorithm>

#define MAX_ENGINES 100
#define INFINITY 99999

using namespace std;

FILE* in;
int noofCases, noofEngines, noofQueries;
char* engines[MAX_ENGINES];
char* tmp;
int dp[2][MAX_ENGINES];
int cur,prev,b1,b2;
int main() {
	tmp = (char*) malloc(102);
	in = fopen("a-in.txt","r");
	fscanf(in,"%d\n",&noofCases);
	for (int caseid = 1; caseid <= noofCases; caseid++) {
		fscanf(in,"%d\n",&noofEngines);
		for (int i = 0; i < noofEngines; i++) {
			fscanf(in,"%[a-zA-Z0-9 ]\n",tmp); 
			engines[i] = (char*) malloc(102);
			strcpy(engines[i],tmp);
		}
		
		cur = 0;
		prev = 1;
		b1 = 0; b2 = 1;
		for (int i = 0; i < noofEngines; i++) {dp[cur][i] = 0;}
		
		fscanf(in,"%d\n",&noofQueries);
		for (int i = 0; i < noofQueries; i++) {
			fscanf(in,"%[a-zA-Z0-9 ]\n",tmp);
			int j, haylookit;
			for (j = 0; j <noofEngines; j++) {
				if (std::strcmp(tmp,engines[j]) == 0) {break;}
			}
			cur = prev;
			prev = 1 - prev;
			for (int k = 0; k < noofEngines; k++) {
				if (j == k) {dp[cur][k] = INFINITY; continue;}
				dp[cur][k] = dp[prev][k];
				haylookit = (k == b1)?  b2 : b1;
				dp[cur][k] = (dp[cur][k] < dp[prev][haylookit] + 1) ?  dp[cur][k] : dp[prev][haylookit] + 1;
			}
			b1 = 0; b2 = 1; if (dp[cur][b2] < dp[cur][b1]) {b2 = 0; b1 = 1;}
			for (int k = 0+2; k < noofEngines; k++) {
				if (dp[cur][k] <= dp[cur][b1]) {
					b2 = b1; b1 = k; continue;
				}
				if (dp[cur][k] <= dp[cur][b2]) {
					b2 = k;
				}
			}
		}
		printf("Case #%d: %d\n",caseid,dp[cur][b1]);
	}
	
	return 0;
}