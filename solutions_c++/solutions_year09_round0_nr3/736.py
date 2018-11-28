#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

char pat[] = "welcome to code jam";
char text[550];

int memo[505][20];

int go(int i, int j) {
	if (j > i) return memo[i][j] = 0;
	if (memo[i][j] != -1) return memo[i][j];
	int res = 0;
	if (text[i] == pat[j]) res = (res+go(i-1, j-1))%10000;
	res = (res+go(i-1, j))%10000;
	return memo[i][j] = res;
}

int main() {
	FILE *fin = fopen("C-large.in", "r");
	FILE *fout = fopen("C-large.out", "w");
	
	int numtests;
	fscanf(fin, "%d\n", &numtests);
	for (int i = 0; i < numtests; i++) {
		fgets(text, 550, fin);
		if (text[strlen(text)-1] == '\n') text[strlen(text)-1] = '\0';

		memset(memo, -1, sizeof(memo));

		int cnt = 0;
		for (int j = 0; j < strlen(text); j++) {
			if (text[j] == pat[0]) cnt++;
			memo[j][0] = cnt;
		}
		for (int j = 1; j < strlen(pat); j++) memo[0][j] = 0;

		int res = go(strlen(text)-1, strlen(pat)-1);
		fprintf(fout, "Case #%d: %04d\n", i+1, res);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}


