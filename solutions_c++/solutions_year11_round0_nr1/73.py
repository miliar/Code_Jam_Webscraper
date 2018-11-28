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

#define N 128
int n;
int pd[N][N][N];
pair<int,int> v[N];
const int inf = (1<<30);

struct X {
	int blue,orange,pos,cst;
};

X novo_x(int blue, int orange, int pos, int cst) {
	X novo;
	novo.blue = blue;
	novo.orange = orange;
	novo.pos = pos;
	novo.cst = cst;
	return novo;
}

X fila[N*N*N];
int ini,fim;
const int TAM = N*N*N;

void insere(int blue, int orange, int pos, int cst) {
	if(blue < 1 || blue > 100 || orange < 1 || orange > 100) return;
	int &res = pd[blue][orange][pos];
	if(res == -1 || res > cst) {
		res = cst;
		fila[fim++] = novo_x( blue, orange, pos, cst);
		if(fim >= TAM) cerr << "DEU ERRO!\n";
	}
}

int solve(int blue, int orange, int pos) {

	ini = fim = 0;
	memset(pd, -1, sizeof(pd));
	insere( blue, orange, pos, 0 );

	while(ini < fim) {
		X at = fila[ini++];

		blue = at.blue;
		orange = at.orange;
		pos = at.pos;
		int cst = at.cst;

		if(pos == n) return cst;

		for(int a = -1; a <= 1; a++) {
			for(int b = -1; b <= 1; b++) {
				int sum = 0;
				if(v[pos].second == 0 && v[pos].first == blue && a == 0) {
					sum = 1;
				}
				if(v[pos].second == 1 && v[pos].first == orange && b == 0) {
					sum = 1;
				}
				insere(blue + a, orange + b, pos + sum, cst+1);
			}
		}
	}

	return -1;
}

int main() {
	int CASOS;
	cin >> CASOS;
	FOR(CASO, CASOS) {
		printf("Case #%d: ", CASO+1);
		cin >> n;
		FOR(i,n) {
			int pos; char cor;
			cin >> cor >> pos;
			v[i] = make_pair(pos, cor == 'B' ? 0 : 1 );
		}
		cout << solve(1,1,0) << endl;
	}

	return 0;
}

