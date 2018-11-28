#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <functional>
#include <algorithm>

#define sqr(a) ((a) * (a))
#define eps 1.0e-12
#define pi (2.0 * acos(0.0))
#define sz(a) ((int)a.size())
#define clr(a, b) (memset(a, b, sizeof(a)))
#define pb push_back
#define FORS(i, a, b, s) for(int i = (a); i < (b); i+=(s))
#define FOR(i, a, b) FORS(i, a, b, 1)
#define REP(i, a) FOR(i, 0, a)
#define FORI(i, a, b) for(i = (a); i != (b); ++i)

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef set<int> SI;

FILE *fp_r, *fp_w;
int t, n;
int i, j, k;
char str[50010];
VI v;
int minlen, len;
string s1, s2;

int main() {

	fp_r = fopen("D-small.txt", "r");
	fp_w = fopen("D.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%d", &n);
		fscanf(fp_r, "%s", str);
		s1 = str;

		v.clear();
		for(j = 0; j < n; j++)
			v.pb(j);

		minlen = 987654321;
		while(1) {
			s2 = "";
			for(j = 0; j < sz(s1); j++)
				s2 += s1[(j / n) * n + v[j % n]];

			len = 0;
			for(j = 1; j < sz(s2); j++) {
				if (s2[j] != s2[j-1])
					len++;
			}
			len++;
			minlen = min(minlen, len);

			if (!next_permutation(v.begin(), v.end())) break;
		}

		fprintf(fp_w, "Case #%d: %d\n", i+1, minlen);
	}

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}