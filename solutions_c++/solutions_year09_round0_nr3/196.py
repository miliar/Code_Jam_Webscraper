#include  <cstdio>
#include  <cstdlib>
#include  <string>
#include  <cmath>
#include  <inttypes.h>
#include  <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <vector>

using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

#define tr(it,s) for(typeof(s.begin())it=s.begin();it!=s.end();++it)
#define rep(i,n) for(int i=0; i<n; ++i)

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }


string pattern = " welcome to code jam";
int total[20];
string line;

main() {
	int N;
	cin >> N;
	getline(cin, line);
	rep(t,N) {
		getline(cin, line);
		//cout << line<< endl;
		rep(i,20) total[i] = 0;
		total[0] = 1;

		rep(i, line.size()) {
			for (int j = 1; j < 20; ++j) {
				if (pattern[j] == line[i])
					total[j] = (total[j] + total[j-1])%10000;
			}
		}

		printf("Case #%d: %04d\n", t+1, total[19]);
	}
}
