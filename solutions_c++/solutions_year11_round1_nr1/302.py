/*{{{*/
/*includes e defines*/
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define SZ(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define FOREACH(A,B) for((__typeof (B).begin) A = (B).begin(); A != (B).end(); A++)
#define PB push_back
#define ALL(x) x.begin() , x.end()
#define MP make_pair
/*}}}*/
/*{{{*/
/*main*/
void solveCase();
int main() {
	int TESTES; scanf("%d", &TESTES);
	for(int TESTE = 1; TESTE <= TESTES; TESTE++) {
		printf("Case #%d: ", TESTE);
		solveCase();
	}
    return 0;
}
/*}}}*/

long long n,pd,pg;

long long mdc(long long a, long long b) {
	return b ? mdc(b, a%b) : a;
}

long long x_porcento_de(long long x, long long val) {
	val = x * val;
	if(val % 100) return -1;
	return val / 100;
}

void solveCase() {
	cin >> n >> pd >> pg;
	int ok = 0;
	for(long long i = n; i >= 1; i--) {
		long long total_hoje = i;
		long long vitorias_hoje = x_porcento_de(pd, total_hoje);
		if(vitorias_hoje * 100 != total_hoje * pd /*|| (pd > 0 && pd < 100 && !vitorias_hoje)*/) continue;

		if(pg == 100) {
			if(pd == 100) ok = 1;
		} else if(pg == 0) {
			if(pd == 0) ok = 1;
		} else {
			ok = 1;
		}
		break;

	}
	if(ok) cout << "Possible" << endl;
	else cout << "Broken" << endl;
}

