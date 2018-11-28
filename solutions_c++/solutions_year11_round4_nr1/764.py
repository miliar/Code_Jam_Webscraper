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


#define MAX 2048
long long X, t, N;
double R, S;
struct walk {
	long long ini,fim,w;
};

walk v[MAX];

walk make(int ini, int fim, int w) {
	walk novo;
	novo.ini = ini; novo.fim = fim; novo.w = w;
	return novo;
}

bool cmp(walk a, walk b) {
	return a.ini < b.ini;
}
bool cmp2(walk a, walk b) {
	return a.w < b.w;
}

double meio(double dist, double vel, double atT) {
	double ini = 0, fim = dist;
	FOR(i,100) {
		double m = (ini+fim) / 2.0;
		double demora = m / vel;
		if(demora + atT <= t) ini = m;
		else fim = m;
	}
	return ((ini+fim) / 2.0) / vel;
}

int ja[MAX];

void solveCase() {
	cin >> X >> S >> R >> t >> N;
	//cout << endl << endl;
	//cout << X << " "<< S << " " << R << " " << t << " " << N << endl;
	FOR(i,N) {
		cin >> v[i].ini >> v[i].fim >> v[i].w;
	}

	sort(v, v+N, cmp);
	if(!N) v[N++] = make(0,X,0);
	else {
		int k = N;
		if(v[0].ini != 0) v[k++] = make(0, v[0].ini, 0);
		for(int i  = 1; i < N; i++) {
			if(v[i-1].fim != v[i].ini) v[k++] = make(v[i-1].fim, v[i].ini, 0);
		}
		if(v[N-1].fim != X) v[k++] = make(v[N-1].fim, X, 0);
		N = k;
	}
	sort(v, v+N, cmp2);

	memset(ja, 0, sizeof(ja));
	double atT = 0, atX = 0;
	FOR(i,N) {
		//cout << v[i].ini << "-" << v[i].fim << ", vel = " << v[i].w << endl;
		double d = v[i].fim - v[i].ini;
		double demora = d / (v[i].w + R);
		if(demora + atT <= t) {
			atT += demora;
		//	cout << "COrreu por " << demora << endl;
		} else {
			double m = meio(d, v[i].w + R, atT);
		//	cout << "Correu por>>>>   " << m << endl;
		//	cout << "Tal que atT era " << atT << " e gastou mais "<< m << " onde t = " << t << endl;
			atX = v[i].ini + m*( v[i].w + R);
			atT += m;
			atT += (v[i].fim - atX) / (v[i].w + S);
		}
	}
	printf("%.10f\n", atT);
	//cout << endl;
}

