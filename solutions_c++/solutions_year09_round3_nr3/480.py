#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <numeric>
#include <fstream>
using namespace std;
#define ALL(c) c.begin(), c.end()
#define pb push_back
#define lg length
#define sz size
#define forn(i,n) for(i=0;i<n;i++)
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int main () {
	int i,j,t,a;
	int N,P,Q;
	int free[10];
	int coins;
	int pris[105];
	ifstream fin("C.in");
	ofstream fout("C.out");
	fin>>N;
	for(t=1;t<=N;t++) {
		fout<<"Case #"<<t<<": ";
		fin>>P;
		fin>>Q;
		for(i=0;i<Q;i++) fin>>free[i];	
		sort(free,free+Q);
		int min = -1;
		do {
			// Simulate:
			coins = 0;
			for(i=1;i<=P;i++) pris[i] = true;
			for(i=0;i<Q;i++) {
				int current = free[i];
				pris[current] = false; // Liberado. 
				// Vecinos a derecha:
				a = current+1;
				while(a<=P && pris[a]) { a++; coins++; }
				// Vecinos a izquierda:
				a = current - 1;
				while(a>0 && pris[a]) {a--; coins++; }
			}
			if(min==-1 || coins<min) min = coins;
		}while(next_permutation(free,free+Q));
		fout<<min<<endl;	
	}
return 0;	
}
