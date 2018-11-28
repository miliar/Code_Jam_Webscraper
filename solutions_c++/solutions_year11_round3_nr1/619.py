#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
#define pb push_back

vector<string> B;

int main() {
	int T;
	//freopen("c:\\in.txt", "r", stdin);
	freopen("c:\\A-large (2).in", "r", stdin);
	freopen("c:\\A-large (2).out", "w", stdout);

	scanf("%d", &T);


	for (int testCase = 1; testCase <= T; ++testCase) {
		int n;
		//scanf("%d", &n);

		int a, b;
		scanf("%d%d", &a, &b);


		B = vector<string>();
		char s[105][105];
		memset(s, 0, sizeof(s));
		for (int i = 0; i < a; ++i) {
			scanf("%s", s[i]);
			//B.pb(s);
		}

		bool ok = true;

		for (int i = 0; i < a; ++i) {
			for (int j = 0; j < b; ++j) {
				if (s[i][j] == '#' && s[i+1][j] == '#' && 
					s[i][j+1] == '#' && s[i+1][j+1] == '#') {
					s[i][j] = '/';
					s[i][j+1] = '\\';
					s[i+1][j] = '\\';
					s[i+1][j+1] = '/';
				}
			}
		}
		for (int i = 0; i < a; ++i) {
			for (int j = 0; j < b; ++j) {
				if (s[i][j] == '#') {
					ok = false;
				}
			}
		}


		printf("Case #%d:\n", testCase);
		if (ok) {
			for (int i = 0; i < a; ++i) {
				printf ("%s\n", s[i]);
			}
		}
		else {
			printf ("Impossible\n");
		}
	}

	return 0;
}