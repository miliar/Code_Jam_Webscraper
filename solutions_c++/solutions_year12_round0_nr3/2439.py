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

char aux[18];

void teste() {
	int x = 12345;
	int mul = 1;
	int cauda = 0;
	while(x) {
		cauda += mul * (x % 10);
		mul *= 10;
		x /= 10;
		sprintf(aux, "%d%d", cauda, x);
		int valor = atoi(aux);
		printf("%d\n", valor);
	}
}
	
#define N 10000001
int ja[N];

int conta(int x, int fim) {

	int ans = 0;
	//set<int> ja;

	int ini = x;
	int cauda = 0;
	int mul = 1;
	while(x > 9) {
		int dig = x % 10;
		cauda += mul * (x % 10);
		mul *= 10;
		x /= 10;
		if( dig ) {
			sprintf(aux, "%d%d", cauda, x);
			int valor = atoi(aux);
			if(ini < valor && valor <= fim) {
				if(ja[valor] != ini) {
					ans++;
					ja[valor] = ini;
				}
			}
		}
	}
	return ans;
}

void solveCase() {
	memset(ja, -1, sizeof(ja));

	int a,b;
	cin >> a >> b;
	long long ans = 0;
	for(int i = a; i < b; i++) {
		ans += conta(i, b);
	}
	cout << ans << endl;
}

