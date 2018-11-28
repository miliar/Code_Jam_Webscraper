//BEGIN_CUT
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <numeric>
#include <bitset>
#include <cstring>
#include <sstream>
#include <utility>
#include <queue>
#include <cassert>
using namespace std;

#define X first
#define Y second
#define FI first
#define SE second
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef double D;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }
//END_CUT

char comb[128][128];

bool opposed[128][128];

char s[1005];
int z;

void alg() {
	CLR(comb, 0);
	CLR(opposed, 0);
	z = 0;
	int c;
	scanf("%d", &c);
	while (c--) {
		char buf[4];
		scanf("%s", buf);
		comb[buf[0]][buf[1]] = buf[2];
		comb[buf[1]][buf[0]] = buf[2];
	}
	scanf("%d", &c);
	while (c--) {
		char buf[3];
		scanf("%s", buf);
		opposed[buf[0]][buf[1]] = true;
		opposed[buf[1]][buf[0]] = true;
	}
	int len;
	scanf("%d", &len);
	char in[len + 1];
	scanf("%s", in);
	for (int i = 0; i < len; ++i) {
		if (z > 0 && comb[s[z - 1]][in[i]]) {
			s[z - 1] = comb[s[z - 1]][in[i]];
		} else {
			s[z++] = in[i];
			REP (j, z - 1)
				if (opposed[s[j]][in[i]]) {
					z = 0;
					break;
				}
		}
	}
	printf("[");
	for (int i = 0; i < z - 1; ++i)
		printf("%c, ", s[i]);
	if (z > 0)
		printf("%c", s[z - 1]);
	printf("]\n");
}

int main() {
	
	int d;
	scanf("%d", &d);

	for (int caseNo = 1; caseNo <= d; ++caseNo) {
		printf("Case #%d: ", caseNo);
		alg();
	}

    return 0;
}
