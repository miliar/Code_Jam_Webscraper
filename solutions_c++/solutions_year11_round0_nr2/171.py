#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <vector>

using std::vector;

vector<char> ans;
int c, d, n;
char comb[100][4], oppo[100][3], str[101];
int appear[26];

void append(char ch) {
	if (ans.empty()) {
		ans.push_back(ch);
		++appear[ch - 'A'];
		return;
	}
	for (int i = 0; i < c; ++i)
		if ((ch == comb[i][0] && ans.back() == comb[i][1]) || (ch == comb[i][1] && ans.back() == comb[i][0])) {
			--appear[ans.back() - 'A'];
			ans.pop_back();
			ans.push_back(comb[i][2]);
			++appear[ans.back() + 'A'];
			return;
		}
	for (int i = 0; i < d; ++i)
		if ((ch == oppo[i][0] && appear[oppo[i][1] - 'A'] > 0) || (ch == oppo[i][1] && appear[oppo[i][0] - 'A'] > 0)) {
			ans.clear();
			for (int j = 0; j < 26; ++j) appear[j] = 0;
			return;
		}
	ans.push_back(ch);
	++appear[ch - 'A'];
}

int main() {
	FILE *fin = fopen("B-small-attempt0.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int t;
	fscanf(fin, "%d", &t);
	for (int i = 1; i <= t; ++i) {
		fprintf(fout, "Case #%d: [", i);
		ans.clear();
		for (int j = 0; j < 26; ++j) appear[j] = 0;
		fscanf(fin, "%d", &c);
		for (int j = 0; j < c; ++j) fscanf(fin, "%s", comb[j]);
		fscanf(fin, "%d", &d);
		for (int j = 0; j < d; ++j) fscanf(fin, "%s", oppo[j]);
		fscanf(fin, "%d", &n);
		fscanf(fin, "%s", str);
		for (int j = 0; j < n; ++j) append(str[j]);
		for (int j = 0; j < (int) (ans.size() - 1); ++j) fprintf(fout, "%c, ", ans[j]);
		if (!ans.empty())
			fprintf(fout, "%c", ans.back());
		fprintf(fout, "]\n");
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
