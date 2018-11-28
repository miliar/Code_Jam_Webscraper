#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
using namespace std;
#define PB			push_back
#define ALL(v)			(v).begin() , (v).end()
#define SZ(v)			( (int) v.size() )
#define Set(v,x)		memset(  v , x , sizeof(v))
#define two(n)			( 1 << (n) )
#define contain(S,i)		( (S) & two(i) ) 
#define SQR(v)			( (v) * (v) )
#define ABS(x)			( ( (x) >= 0 ) ? (x) : -(x) )
#define foreach(v,it)		for( typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++ )

char res[1000];
int N, D, C;

void solve() {
	int i , j;
	string x, w;
	map<char,set<char> > opp;
	map<string, char >   comb;

	cin >> C;
	for (i = 0 ; i < C ; i++) {
		cin >> x;
		w = x.substr(0,2);
		comb[w] = x[2];
		swap(w[0],w[1]);
		comb[w] = x[2];
	}
	cin >> D;
	for (i = 0 ; i < D ; i++) {
		cin >> x;
		opp[x[0]].insert(x[1]);
		opp[x[1]].insert(x[0]);
	}
	cin >> N >> w;
	j = 0;
	map<char,int> currentChars;
	for (i = 0 ; i < N ; i++) {
		if (j == 0) {
			res[j++] = w[i];
			currentChars[w[i]]++;
		}
		else {
			x = res[j-1];
			x += w[i];
			if (comb.find(x) != comb.end()) {
				currentChars[res[j-1]]--;
				res[j-1] = comb[x];
				currentChars[comb[x]]++;
				continue;
			}
			set<char> &tmp = opp[w[i]];
			bool ok = true;
			foreach( tmp , it) {
				if (currentChars[*it] > 0) {
					ok = false;
					break;
				}
			}
			if (!ok) {
				j = 0;
				currentChars.clear();
			}
			else {
				res[j++] = w[i];
				currentChars[w[i]]++;
			}
		}
	}
	cout << "[";
	if (j > 0 )
		cout << res[0];
	for (i = 1 ; i < j ; i++)
		cout << ", " << res[i];

	cout << "]\n";
}

int main() {
	int C , nc;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cout << "Case #" << nc << ": ";
		solve();
	}	
	return 0;
}
