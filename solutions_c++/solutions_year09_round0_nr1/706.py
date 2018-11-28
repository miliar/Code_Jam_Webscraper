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

#define pb push_back

int main() {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A-large.out", "w");
	
	int L, D, N;
	fscanf(fin, "%d %d %d", &L, &D, &N);

	char w[430];
	vector <string> dic;
	for (int i = 0; i < D; i++) {
		fscanf(fin, "%s", w);
		dic.pb(string(w));
	}

	for (int i = 0; i < N; i++) {
		fscanf(fin, "%s", w);
		vector < set <char> > a(L);
		int pos = 0;
		for (int j = 0; j < L; j++) {
			if (w[pos] == '(') {
				pos++;
				while (w[pos] != ')') a[j].insert(w[pos++]);
				pos++;
			}
			else a[j].insert(w[pos++]);
		}
		int res = 0;
		for (int j = 0; j < D; j++) {
			string dw = dic[j];
			bool good = 1;
			for (int k = 0; k < L; k++) {
				if (a[k].count(dw[k]) == 0) {
					good = 0; break;
				}
			}
			if (good) res++;
		}
		fprintf(fout, "Case #%d: %d\n", i+1, res);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}


