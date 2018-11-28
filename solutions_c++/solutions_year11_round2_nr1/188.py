#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int N;
char tabela[200][200];
double wp[200];
double owp[200];
double oowp[200];
int process() {

	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s", tabela[i]);
	}
	
	int total, wins;
	for (int i = 0; i < N; i++) {
		total = wins = 0;
		for (int j = 0; j < N; j++) {
			if (tabela[i][j] != '.') {
				total++;
				wins += tabela[i][j] - '0';
			}
		}
		wp[i] = ((double)wins)/total;
	}
	
	int total2;
	double sum;
	for (int k = 0; k < N; k++) {
		total2 = 0;
		sum = 0;
		for (int i = 0; i < N; i++) {
			if (tabela[k][i] != '.') {
				// calc
				total2++;
				total = wins = 0;
				for (int j = 0; j < N; j++) {
					if (tabela[i][j] != '.' && j != k) {
						total++;
						wins += tabela[i][j] - '0';
					}
				}
				sum += ((double)wins)/total;
			}
		}
		owp[k] = sum / total2;
	}
	
	for (int i = 0; i < N; i++){
		sum = 0;
		total2=0;
		for (int j = 0; j < N; j++) {
			if (tabela[i][j] != '.') {
				total2++;
				sum += owp[j];
			}
		}
		oowp[i] = sum/total2;
	}
	
	for (int i = 0; i < N; i++){
		printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
}

int main() {
	
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		printf("Case #%d:\n", i+1);
		process();
	}
	
	return 0;
}
