#include <cstdio>
#include <vector>
#include <algorithm>
//#include <map>
//#include <set>

#define FOR(i,s,e) for (int i=(s);i<(e);i++)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define PB push_back

using namespace std;

typedef long double ld;

int n;
char str[500][500];
int ones[500], zeros[500];
ld RPI[5000], OWP[5000];

void test(int cid) {
	printf("Case #%d:\n", cid);
	scanf("%d", &n);
	fill(ones,ones+n,0);
	fill(zeros,zeros+n,0);
	REP(i,n) {
		scanf("%s", str[i]);
		for (char*q = str[i]; *q; q++) {
			if (*q == '1') ones[i]++;
			else if (*q == '0') zeros[i]++;
		}
		RPI[i] = ((ld)0.25) * ((ld)ones[i]) / ((ld)(ones[i]+zeros[i]));
	}
	REP(i,n) {
		ld cnt = 0;
		int cc = 0;
		REP(j,n) if (str[i][j] != '.') {
			int os = ones[j], total = ones[j] + zeros[j] - 1;
			if (str[j][i] == '1') os--;
			cnt += ((ld)os) / ((ld)total);
			cc++;
		}
		OWP[i] = cnt / ((ld)cc);
		RPI[i] += ((ld)0.5) * OWP[i];
	}
	REP(i,n) {
		ld sum = 0;
		int cnt = 0;
		REP(j,n) if (str[i][j] != '.') {
			sum += OWP[j];
			cnt ++;
		}
		RPI[i] += ((ld)0.25) * (sum / ((ld)cnt));
	}
	REP(i,n) printf("%.12Lf\n", RPI[i]);
}

main() {
	int t;
	scanf("%d", &t);
	REP(i,t) test(i+1);
}

