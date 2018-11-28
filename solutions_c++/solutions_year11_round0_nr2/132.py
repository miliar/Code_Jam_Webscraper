#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

bool opt[128][128];
char tp[1000];
char cov[128][128];
int main() {

	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	int bb = 1;
	scanf("%d", &T);
	while (T--) {
		memset(opt, 0, sizeof(opt));
		memset(cov, 0, sizeof(cov));
		int C, D, N;
		scanf("%d", &C);
		for (int i = 0; i < C; ++i) {
			scanf("%s", tp);
			cov[tp[0]][tp[1]] = tp[2];
			cov[tp[1]][tp[0]] = tp[2];
		}
		scanf("%d", &D);
		for (int i = 0; i < D; ++i) {
			scanf("%s", tp);
			opt[tp[0]][tp[1]] = true;
			opt[tp[1]][tp[0]] = true;
		}
		scanf("%d", &N);
		scanf("%s", tp);
		string ret = "";
		for (int i = 0; i < N; ++i) {
			if (ret.size() == 0) {
				ret += tp[i];
				continue;
			}
			char a, b;
			a = ret[ret.size() - 1];
			b = tp[i];
			if (cov[a][b] != 0) {
				ret[ret.size() - 1] = cov[a][b];
			} else {
				bool flag = false;
				for (char aa = 'A'; aa <= 'Z'; ++aa) {
					if (opt[aa][b] && ret.find(aa) != string::npos) {
							ret = "";
							flag = true;
					}
				}
				if (!flag) {
					ret += tp[i];
				}
			}
		}
		printf("Case #%d: ", bb++);
		printf("[");
		for (int i = 0; i < ret.size(); ++i) {
			if (i != 0) {
				printf(", ");
			}
			printf("%c", ret[i]);
		}
		printf("]");
		puts("");
	}

	return 0;
}

