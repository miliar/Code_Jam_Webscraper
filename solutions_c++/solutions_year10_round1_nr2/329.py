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

int D,I,M,N;
int v[100];

/*
int res(int pos, int last) {
	if(pos >= N+1) return 0;
	int dd = v[pos] - last;
	if(dd < 0) dd = -dd;

	if(dd <= M) 
		return res(pos+1, v[pos]);


}*/

int teto(int a, int b) {
	return (a+b-1) / b;
}

int dif(int a, int b) {
	return max(a-b, b-a);
}

int insere(int a, int b) {
	if(dif(a,b) <= M) return 0;
	if(M == 0) return 10000000;
	if(a > b) swap(a,b);
	return min(dif(a,b)-M, insere(a+M, b) + I);
//	return teto( dif(a,b) - M, M) * I;
}

int insereX(int a, int b) {
	if(a < 0 || b < 0) return 1000000;
	if(dif(a,b) <= M) return 0;
	if(M == 0) return 10000000;
	return teto( dif(a,b) - M, M) * I;
}




int calc(int a, int b) {
	int dd = dif(a, b);
	if(dd <= M) return 0;
	int r = (dd - M);
	r = min(r, D);
	r = min(r, insere(a, b));
	return r;

}

int insercoes() {

	int r = 1000000000;
	int p1 = max(dif(v[0],v[1]) + 1, M+1);
	int p2 = max( max(dif(v[1],v[2]) + 1, dif(v[1],v[0])+ 1) , M+1);
	int p3 = max(dif(v[1],v[2]) + 1, M+1);
	p1 = p2 = p3 = 255;
	FOR(i, p1) {
		if(v[0] + i > 255 && v[0] - i < 0) break;
		FOR(j, p2) {
			if(v[1] + j > 255 && v[1] - j < 0) break;
			FOR(k, p3) {
				if(v[2] + k > 255 && v[2] - k < 0) break;
				FOR(a,2) FOR(b,2) FOR(c,2) {
					int kk = k, ii = i, jj = j;
					if(a) ii = -ii;
					if(b) jj = -jj;
					if(c) kk = -kk;
					r = min(r, i+j+k + insereX(v[0]+ii, v[1]+jj) + insereX(v[1]+jj, v[2]+kk));
				}
			}
		}
	}

	return r;
}

int res(int pos, int last) {
	if(N == 1) return 0;
	if(N == 2) {
		return calc(v[0], v[1]);
	}

	//N = 3.
	
	int r = 2*D;
	r = min(r, D + calc(v[1], v[2]));
	r = min(r, D + calc(v[0], v[1]));
	r = min(r, D + calc(v[0], v[2]));
	int aux1 = 0, aux2 = 0;
	
	aux1 = dif(v[0],v[1]);
	if(aux1 <= M)
		r = min(r, calc(v[1], v[2]));
	aux2 = dif(v[1], v[2]);
	if(aux2 <= M)
		r = min(r, calc(v[0], v[1]));

	if(aux1 > M && aux2 > M) {
		aux1 -= M; aux2 -=M;
		r = min(r, aux1 + aux2);
		r = min(r, aux1 + insere(v[1], v[2]));
		r = min(r, aux2 + insere(v[0], v[1]));

		if(0 && ((v[0] <= v[1] && v[2] <= v[1]) || ( v[0] >= v[1] && v[2] >= v[1])) ) {

			int aux = aux1 + insere( v[1] + min(aux1, dif(v[1],v[2])) , v[2] );
			r = min(r, aux);
			aux = aux1 + insere(v[1] , v[2] + min(aux1, dif(v[1],v[2])));
			r = min(r, aux);

			aux = aux2 + insere( v[0] + min(aux1, dif(v[0],v[1])) , v[1] );
			r = min(r, aux);
			aux = aux2 + insere( v[0]  , v[1]  + min(aux1, dif(v[0],v[1])) );
			r = min(r, aux);

		}


		r = min(r, insercoes());
	}


	return r;
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		cin >> D >> I >> M >> N;

		int caso = -1;
		if(t + 1 == caso) cout << endl << D << " " <<  I << " " <<  M << " "<< N << endl;

		FOR(i,N) {
			cin >> v[i];
			if(t + 1 == caso)	cout << v[i] << " ";
		}
		if(t + 1 == caso) cout << endl;

		cout << res(1, v[0]) << endl;
	}

    return 0;
}

