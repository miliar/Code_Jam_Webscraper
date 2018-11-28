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

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define pii pair<int,int>
#define inf (1<<25)
#define infL 10000000000000000LL
#define F first
#define S second
#define all(x) x.begin() , x.end()

queue< pii > fila;
int vezes, tam, n;

int pos[1000];
ll lucro[2000];

ll calc(int ant, int at) {
	ll val = lucro[at-1];
	ll menos = 0;
	if(ant - 1 >= 0) menos = lucro[ant-1];
	val -= menos;

	ll ciclo = at - ant;
	ll qtdCiclo = (vezes - ant) / ciclo;

	ll res = 0;
	res = (ll) (qtdCiclo-1) * val;

	ll sobra = vezes - ((qtdCiclo * ciclo) + ant);

	ll soma = 0;
	if(ant + sobra - 1 >= 0)
		soma = lucro[ant + sobra - 1];
	soma -= menos;

	return res + soma;
}

ll res(int at, int pai) {
	
	ll ant = 0;
	if(pai != -1) ant = lucro[pai];


	if(at == vezes) {
		return ant;
	}

	pii aux = fila.front();

//	cout << "na it " << at  << " pai tem lucro " << ant <<  " e prim da fila é o " << aux.second << endl;

	if( pos[ aux.second ] != - 1) {
//		cout << "repetiu na it " << at << " volta pro cara " << pos[aux.second] << endl;
		return calc( pos[ aux.second ], at  ) + ant;
	}
	pos[ aux.second ] = at;


	ll acu = 0;
	while(1) {
		pii p = fila.front();
		if(acu + p.first > tam) break;
		acu += p.first;
		fila.pop();
		fila.push(p);
	}


	lucro[at] = ant + acu;
	return res(at+1, at);
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		scanf("%d %d %d", &vezes, &tam, &n);
		while(!fila.empty()) fila.pop();
		pii aux;
		ll sum = 0;
		FOR(i, n) {
			scanf("%d", &aux.first);
			aux.second = i;
			fila.push(aux);
			sum += aux.first;
		}

		if(sum <= tam) {
			cout << (ll) vezes * sum << endl;
		}

		else {
			memset(pos, -1, sizeof(pos));
			memset(lucro, 0, sizeof(lucro));
			cout << res(0, -1) << endl;
		}
	}

    return 0;
}

