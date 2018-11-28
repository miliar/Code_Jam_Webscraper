#include <cstdio>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

FILE *fp_r, *fp_w;
int l, d, n;
char word[10000];
vector<string> v;
int p[20][30];
int cnt;

int main() {
	fp_r = fopen("a.in", "r");
	fp_w = fopen("a.out", "w");

	fscanf(fp_r, "%d %d %d", &l, &d, &n);
	v.clear();
	for(int i = 0; i < d; ++i) {
		fscanf(fp_r, "%s", word);
		v.push_back(word);
	}

	for(int i = 0; i < n; ++i) {
		cnt = 0;
		fscanf(fp_r, "%s", word);
		memset(p, 0, sizeof(p));

		int len = strlen(word);
		int idx = 0;
		bool open = false;
		for(int j = 0; j < len; ++j) {
			if (word[j] == '(') {
				open = true;
				continue;
			}
			if (word[j] == ')') {
				open = false;
				++idx;
				continue;
			}
			if (open) {
				p[idx][word[j]-'a'] = 1;
			}
			else {
				p[idx][word[j]-'a'] = 1;
				++idx;
			}
		}

		for(int j = 0; j < d; ++j) {
			bool b = true;
			for(int k = 0; k < l; ++k) {
				if (p[k][v[j][k] - 'a'] == 0) {
					b = false;
					break;
				}
			}

			if (b) ++cnt;
		}

		fprintf(fp_w, "Case #%d: %d\n", i+1, cnt);
	}

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}