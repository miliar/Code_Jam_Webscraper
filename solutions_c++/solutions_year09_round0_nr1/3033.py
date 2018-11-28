#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int main () {
	int li, w, p, i, j, ch, k, co, t = 0;
	scanf("%d%d%d", &li, &w, &p);
	vector<string> maj(w, string(li, ' '));
	for(i = 0; i < w; ++i) {
		for(j = 0, getchar(); j < li; maj[i][j++] = getchar()); }
	vector<vector<bool> > level;
	for(i = 0; i < p; ++i) {
		level.assign(li, vector<bool>(128, false));
		for(co = j = 0, getchar(); j < li; ++j) {
			if((ch = getchar()) == '(') {
				while((ch = getchar()) != ')') { level[j][ch] = true; }
			} else { level[j][ch] = true; } }
		for(j = 0; j < w; ++j) {
			for(k = 0; k < li && level[k][maj[j][k]]; ++k);
			if(k == li) { ++co; } }
		printf ("Case #%d: %d\n", ++t, co); }
	return 0; }