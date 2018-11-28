
#include <cmath>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

#define INF 0x7FFFFFFF

typedef unsigned long long int ull;
typedef long double ld;

int prices[2000][2000];
bool purchased[2000][2000];
int T,P;
int M[2000];

int have(int num) {
	int cnt = 0;
	FOR(i,P) {
		if (purchased[i][ num / (1 << P)]) {
			cnt++;
		}
	}
	return cnt;
}

int main() {
	cin >> T;
	FOR(t,T) {
		cin >> P;
		//cerr << (1 << (P-1)) << endl;

		FOR(i,1 << P) {
			cin >> M[i];
			//cerr << M[i] << " ";
		}
		//cerr << endl;


		for (int i = P-1; i >= 0; i--) {
			FOR(j,1 << i) {
				cin >> prices[P-i][j];
				//cerr << P-i << "," << j << ":"<<  prices[P-i][j] << " ";
			}
			//cerr << endl;
		}
		
		int cost = 0;

		CLR(purchased,0);

		FOR(i,1<<P) {
			int need = P - M[i];	
			for (int j = P; j > 0; j--) {
				if (need == 0) break;
				if (!purchased[j][i / (1 << j)]) {
					cost += prices[j][i / (1 << j)];
					//cost++;
					purchased[j][i / (1 << j)] = true;
					/*
					printf("Purchased ticket for team %d in round %d (game %d)\n",
						i,j, i / (1 << j)
					);
					*/
				} 
				need--;
			}
		}

		printf("Case #%d: %d\n", t+1, cost);
	}
	return 0;
}
