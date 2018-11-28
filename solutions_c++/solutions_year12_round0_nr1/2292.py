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
#define sz(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define FOREACH(A,B) for((__typeof (B).begin) A = (B).begin(); A != (B).end(); A++)
#define pb push_back
#define all(x) x.begin() , x.end()
#define mp make_pair
/*}}}*/
/*{{{*/
/*main*/
void solveCase();
int main() {
	int TESTES; scanf("%d\n", &TESTES);
	for(int TESTE = 1; TESTE <= TESTES; TESTE++) {
		printf("Case #%d: ", TESTE);
		solveCase();
	}
    return 0;
}
/*}}}*/


#define N 1000002
char IN[N];

void solveCase() {
	vector<string> A;
	A.pb("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	A.pb("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	A.pb("de kr kd eoya kw aej tysr re ujdr lkgc jv");
	vector<string> B;
	B.pb("our language is impossible to understand");
	B.pb("there are twenty six factorial possibilities");
	B.pb("so it is okay if you want to just give up");

	map<char,char> ida, volta;

	FOR(i, sz(A)) {
		FOR(j, sz(A[i])) {
			ida[ B[i][j] ] = A[i][j];
			volta[ A[i][j] ] = B[i][j];
		}
	}

	ida['z'] = 'q';
	volta['q'] = 'z';

	ida['q'] = 'z';
	volta['z'] = 'q';

	ida[' '] = ' ';
	volta[' '] = ' ';

	ida['\n'] = '\n';
	volta['\n'] = '\n';

	fgets(IN, N, stdin);
	int t = strlen(IN);
	FOR(i, t) {
		cout << volta[ IN[i] ];
	}

}

