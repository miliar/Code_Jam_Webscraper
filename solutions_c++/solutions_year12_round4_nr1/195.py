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
	int TESTES; scanf("%d", &TESTES);
	for(int TESTE = 1; TESTE <= TESTES; TESTE++) {
		printf("Case #%d: ", TESTE);
		solveCase();
	}
    return 0;
}
/*}}}*/


#define N 10002
int d[N], l[N];
double h[N];

void solveCase() {
	int n;
	cin >> n;
	FOR(i, n) {
		cin >> d[i] >> l[i];
		h[i] = -1;
		if(i == 0) {
			h[i] = d[i];
		}
	}
	cin >> d[n];
	l[n] = 0;
	h[n] = -1;
	n++;

	FOR(i, n) {
//		cerr << "I = " << i; cerr << " H = " << h[i] << " D = " << d[i] << " L = " << l[i] << endl;

		for(int j = i+1; j < n; j++) {
			double dd = d[j] - d[i];
			if(h[i] < dd) break;
			double novoh;
			novoh = sqrt( h[i] * h[i] - (double) dd * (double) dd );
			novoh = max(novoh, (double) dd);
			novoh = min(novoh, (double) l[j]);
			h[j] = max(h[j], novoh);
		}
	}

	if(h[n-1] >= 0) cout << "YES" << endl;
	else cout << "NO" << endl;
}

