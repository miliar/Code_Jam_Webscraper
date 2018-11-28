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

#define N 10000
#define M 100
string palavras[N];
string letras[M];
string ans[M];
int n,m;

int pode_caractere(char c, vector<string> & validas) {
	FOR(i, SZ( validas )) {
		FOR(j , SZ(validas[i])) if( validas[i][j] == c ) return 1;
	}
	return 0;
}

void elimina_caractere(char c, vector<string> & validas) {
	for(int i = SZ( validas ) - 1; i >= 0; i--) {
		int tem = 0;
		FOR(j , SZ(validas[i])) if( validas[i][j] == c ) tem = 1;
		if(tem) {
			swap( validas[i], validas[ SZ(validas) - 1] );
			validas.pop_back();
		}
	}
}

void elimina_caractere_novo(char c, vector<string> & validas, string & chute) {
	for(int i = SZ( validas ) - 1; i >= 0; i--) {
		int tem = 0;
		FOR(j , SZ(validas[i])) if( validas[i][j] == c && chute[j] != c ) tem = 1;
		if(tem) {
			swap( validas[i], validas[ SZ(validas) - 1] );
			validas.pop_back();
		}
	}
}



void elimina_invalidas(vector<string> & validas, string & chute) {
	for(int i = SZ( validas ) - 1; i >= 0; i--) {
		int tem = 0;
		FOR(j , SZ(validas[i])) if( chute[j] != '-' && validas[i][j] != chute[j] ) tem = 1;
		if(tem) {
			swap( validas[i], validas[ SZ(validas) - 1] );
			validas.pop_back();
		}
	}
}



int calc_pontos(string & pal, string & lista) {
	vector<string> validas;
	FOR(i, n) if( SZ( palavras[i] ) == SZ( pal ) ) validas.push_back( palavras[i] );
	string chute( SZ(pal), '-' );
	int pontos = 0;
	//cerr << "PAL = " << pal << " lista = "<< lista << endl;
	FOR(i, SZ(lista)) {

//		cerr << "ATUAL = " << chute << endl;
//		FOR(j, SZ(validas)) cerr << "VAL = " << validas[j] << " ";
//		cerr << endl;

		if(pode_caractere(lista[i], validas)) {
	//		cerr << "CHUTE = " << lista[i] << endl;
			int perde = 1;
			FOR(j, SZ(chute)) {
				if(chute[j] == '-' && pal[j] == lista[i]) {
					perde = 0;
					chute[j] = pal[j];
				}
			}
	//		cerr << "OBTEN = " << chute << endl;
			pontos += perde;
			if(perde) {
				elimina_caractere(lista[i], validas);
			} else {
				elimina_caractere_novo(lista[i], validas, chute);
			}
			elimina_invalidas(validas, chute);
			
		} else {
			//elimina_caractere(lista[i], validas);
		}

		if(chute == pal) break;
	}
//	cerr << "PAl = " << pal << ", chute = " << chute  << ",, pontos = " << pontos << endl;
	return pontos;
}

string calc_best(string & lista) {
	int id_pior = -1, pontos = 0;
	FOR(i,n) {
		int p = calc_pontos(palavras[i], lista);
		if(id_pior == -1 || p > pontos) {
			id_pior = i;
			pontos = p;
		}
	}
	//cerr << "PAL = " << palavras[id_pior] << " pra LISTA " << lista << " dah " << pontos << endl;
	return palavras[id_pior];
}

void solveCase() {
	cin >> n >> m;
	FOR(i,n) cin >> palavras[i];
	FOR(i,m) cin >> letras[i];

	//FOR(i,n) cerr << palavras[i] << endl;

	
	FOR(i,m) {
		ans[i] = calc_best(letras[i]);
	}

	FOR(i,m) {
		if(i) cout << " ";
		cout << ans[i];
	}
	cout << endl;
//	exit(1);
}

