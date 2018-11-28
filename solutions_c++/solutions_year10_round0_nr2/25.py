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

vi v[1000];
int n;

void imprime(vi x) {
	return;
	reverse(all(x));
	FOR(i, sz(x)) printf("%d", x[i]);
	reverse(all(x));
	printf("\n");
}

int menor(vi a, vi b) {
	if(sz(a) != sz(b)) return sz(a) < sz(b);
	for(int i= sz(a) - 1; i >= 0;  i--) {
		if(a[i] != b[i]) 
			return a[i] < b[i];
	}
	return 0;
}


vi soma(vi a, vi b) {


	while(sz(a) != sz(b)) {
		if(sz(a) < sz(b)) a.pb(0);
		else b.pb(0);
	}


	vi r;
	FOR(i, sz(a))
		r.pb( a[i] + b[i] );

	FOR(i,sz(r)) {
		int vai = r[i] / 10;
		r[i] %= 10;
		if(vai) {
			if( i == sz(r) - 1) {
				r.pb(vai);
			}
			else
				r[i+1] += vai;
		}
	}
//	reverse(all(r));
	while(sz(r) > 1 && r[sz(r) - 1] == 0) r.pop_back();
//	reverse(all(r));

	return r;
}

vi menos(vi a, vi b) {


	while(sz(a) != sz(b)) {
		if(sz(a) < sz(b)) a.pb(0);
		else b.pb(0);
	}


	vi r;
	FOR(i, sz(a))
		r.pb( a[i] - b[i]);


	while(1) {
		int foi = 0;
		for(int i = sz(r) - 1; i >= 0; i--) {
			while(r[i] < 0) {
				foi = 1;
				r[i] += 10;
				r[i+1]--;
			}
		}
		if(!foi) break;
	}

	FOR(i,sz(r)) {
		int vai = r[i] / 10;
		r[i] %= 10;
		if(vai) {
			if( i == sz(r) - 1) {
				r.pb(vai);
			}
			else
				r[i+1] += vai;
		}
	}

	while(sz(r) > 1 && r[sz(r) - 1] == 0) r.pop_back();
//	reverse(all(r));

	return r;

}




vi mult(vi a, vi b) {


	vi r; r.clear();

	FOR(i,sz(a) + sz(b) + 5)
		r.pb(0);


	FOR(i,sz(a))
		FOR(j,sz(b)) {
			r[i+j] += a[i] * b[j];
		}

	FOR(i,sz(r)) {
		int vai = r[i] / 10;
		r[i] %= 10;
		if(vai) {
			if( i == sz(r) - 1) {
				r.pb(vai);
			}
			else
				r[i+1] += vai;
		}
	}


	while(sz(r) > 1 && r[sz(r) - 1] == 0) r.pop_back();
//	reverse(all(r));

	return r;
}

vi div(vi a, vi b) {


	vi r; r.clear(); r.pb(0);

	while(!menor(a,b)) {
		vi bb = b, antBB = b;
		vi prod, antPROD;
		prod.clear(); antPROD.clear();
		prod.pb(1);
		antPROD.pb(1);

		vi dois; dois.clear(); dois.pb(2);

		while(!menor(a,bb)) {
			antBB = bb;
			antPROD = prod;

			prod = mult(prod, dois);
			bb = mult(bb, dois);
		}

		r = soma(r, antPROD);
		a = menos(a,antBB);
	}

	return r;

}

vi mod( vi a, vi b ) {
	
	vi d = div(a, b);

	vi mm = mult(d, b);

	vi r = menos(a, mm );
/*
	if(0) {
	cout << "A div por B da D " << endl;
	imprime(a);
	imprime(b);
	imprime(d);
	cout << "Multiplica B por D da " << endl;
	imprime(mm);
	cout << "Subtrai A - Mult dah " << endl;
	imprime(r);
	} */


	return r;
}

vi mdc(vi a, vi b) {

/*	if(0) {
	cout << "QUERO MDC de " << endl;
	imprime(a);
	imprime(b);
	} */

	if(sz(b) == 1 && b[0] == 0) return a;
	return mdc(b, mod(a,b));
}

vi MDC() {
	vi at = menos(v[1], v[0]);


	for(int i=2; i < n; i++) {
//		printf("Processa o %d\n", i);

//		cout << "AT = " << endl;
//		FOR(j, sz(at)) printf("%d", at[j]); printf("\n");

		vi sub = menos( v[i] , v[i-1] );

//		cout << "SUB == " << endl;
//		FOR(j, sz(sub)) printf("%d", sub[j]); printf("\n");

		at = mdc(at, menos(v[i], v[i-1]));
	}

	return at;
}


int cmp(vi a, vi b) {
	return menor(a,b);
}

int main() {

	/*
	vi vals[1000];
	vals[0].pb(0);
	vals[1].pb(1);
	imprime(vals[0]);
	imprime(vals[1]);
	for(int i = 2; i < 20; i++) {
		vals[i] = soma(vals[i-1] , vals[1]);
		imprime(vals[i]);
	}

	vi mm = mult(vals[15], vals[4]);
	imprime(mm);

	return 0;

	vi nove; nove.pb(9);
	vi s = soma(nove, nove);
	imprime(s);
	s = div(s, nove);
	imprime(s);

	return 0; */


	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		scanf("%d", &n);
		vi mini;
		mini.clear();
		FOR(i, 100) mini.pb(9);

		FOR(i, n) {
			string aux;
			cin >> aux;
			vi novo; novo.clear();
			FOR(j, sz(aux)) novo.pb( aux[ sz(aux) -j-1 ] - '0' );
			v[i] = novo;
			if(menor(v[i], mini))
				mini = v[i];
		}
		sort(v, v+n, cmp);

		vi m = MDC();

//		cout << "MDC = " << endl;
//		imprime(m);

		
//		cout << "MINI == " << endl;
//		imprime(mini);

		vi res; res.clear();

		//busca binaria

		vi um;
		um.clear(); um.pb(1);

		vi ii = div(mini, m);
		
//		cout << "II == " << endl;
//		imprime(ii);


		vi mm = mult(ii,m);
		if(menor(mm, mini))
			ii = soma(ii, um);

		res = mult(ii,m);
		res = menos( res, mini );

		/*
		for(ll i = 0; ; i++) {
			if(i*m - mini >= 0) {
				res = i*m - mini;
				break;
			}
		} */
		
		while(sz(res) > 1 && res[ sz(res) - 1] == 0) res.pop_back();
		reverse(all(res));

		FOR(i, sz(res))
			printf("%d", res[i]);
		printf("\n");
	}

    return 0;
}

