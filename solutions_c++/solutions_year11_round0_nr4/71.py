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

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define sz(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define all(x) x.begin() , x.end()

#define N 1024
int v[N];
int ja[N];

double solve(int t) {
	if(t == 1) return 0;
	return t;
}

int main() {
	int TESTES; scanf("%d", &TESTES);
	for(int TESTE = 1; TESTE <= TESTES; TESTE++) {
		printf("Case #%d: ", TESTE);
		int n;
		cin >> n;
		FOR(i, n) {
			int aux;
			cin >> aux;
			aux--;
			v[i] = aux;
		}
		memset(ja, 0, sizeof(ja));
		double ans = 0;
		FOR(i, n) {
			if(!ja[i]) {
				int tam = 0;
				int at = i;
				while(!ja[at]) {
					ja[at] = 1;
					tam++;
					at = v[at];
				}
				ans += solve(tam);
			}
		}
		printf("%.10f\n", ans);
	}

    return 0;
}

