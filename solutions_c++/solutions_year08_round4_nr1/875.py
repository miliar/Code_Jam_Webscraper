#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <assert.h>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

typedef string resulttype;

void skipEOL() { string foo; getline(cin,foo); }

#define MAXN	10000
int gates;
int Gate[MAXN], Chg[MAXN], Val[MAXN];
int cost[MAXN];

#define BIG 10000000

int getcost(int P) {
	cerr << "P=" << P << endl;
	assert(P<MAXN);
	assert(P>=0);
	if (!cost[P]) {
		if (P>=gates) return cost[P] = BIG;
		int S1 = 2*P+1;
		int S2 = S1+1;
		assert(S2<MAXN);
		if (Gate[P]) {
			if (Val[P]) {
				int a = getcost(S1);
				int b = getcost(S1+1);
				cost[P] = a<b? a:b;
			} else {
				int a = 0;
				if (!Val[S1]) a+= getcost(S1);
				if (!Val[S2]) a+= getcost(S2);
				if (a>BIG) a=BIG;
				cost[P]=a;
			}
		} else {
			if (!Val[P]) {
				int a = getcost(S1);
				int b = getcost(S1+1);
				cost[P] = a<b? a:b;
			} else {
				int a = 0;
				if (Val[S1]) a+= getcost(S1);
				if (Val[S2]) a+= getcost(S2);
				if (a>BIG) a=BIG;
				cost[P]=a;
			}
		}
		if (Chg[P]) {
			int alt = 1;
			if ((Val[S1] & Val[S2]) != (Val[S1] | Val[S2])) {
				cost[P] = 1;
			} else {
				if (!Gate[P]) {
					if (Val[P]) {
						int a = getcost(S1);
						int b = getcost(S1+1);
						alt = a<b? a:b;
					} else {
						int a = 0;
						if (!Val[S1]) a+= getcost(S1);
						if (!Val[S2]) a+= getcost(S2);
						if (a>BIG) a=BIG;
						alt=a;
					}
				} else {
					if (!Val[P]) {
						int a = getcost(S1);
						int b = getcost(S1+1);
						alt = a<b? a:b;
					} else {
						int a = 0;
						if (Val[S1]) a+= getcost(S1);
						if (Val[S2]) a+= getcost(S2);
						if (a>BIG) a=BIG;
						alt=a;
					}
				}
				alt++;
				if (alt < cost[P]) cost[P] = alt;
			}
			
		}
	}
	return cost[P];
}

resulttype OneCase() {
	cerr << "ONE CASE" << endl;

	resulttype result;

	int M, V;

	cin >> M >> V;

	gates = (M-1)/2;

	for (int L=0; L<gates; ++L) {
		int G, C;
		cin >> G >> C;
		Gate[L] = G;
		Chg[L] = C;
	}
	for (int L=gates; L<M; ++L) {
		int I;
		cin >> I;
		Chg[L] = 0;
		Val[L] = I;
	}
	
	for (int i=gates-1; i>=0; --i) {
		int S1 = 2*i+1;
		if (Gate[i]) 
			Val[i] = Val[S1] & Val[S1+1];
		else 
			Val[i] = Val[S1] | Val[S1+1];
	}
	cerr << "is " << Val[0] << endl;
	for (int i=0; i<M; ++i) {
		assert(i<MAXN);
		cost[i] = 0;
	}
	cerr << ":)" << endl;
	if (Val[0] == V) {
		cout << 0;
	} else	if ( getcost(0) < BIG ) {
		cout << getcost(0);
	} else
	cout << "IMPOSSIBLE";
	
	return "";
}

int main() {
	int Anz;
	cin >> Anz;
	skipEOL();
	for (int run=1; run<=Anz; ++run) {
		cout << "Case #" << run << ": ";
		resulttype result = OneCase();

		cout  << result << endl;
	}
	return 0;
};
