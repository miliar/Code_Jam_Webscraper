/* a-small.cc
 */
#include <algorithm>
#include <cstdio>
#include <string>
#include <cassert>
#include <iostream>
using namespace std;
int T,R,C;
string P[64];
bool V[64];
int main() {
    cin >> T;
    for (int t=0; t<T; ++t) {
	cin >> R >> C;
	bool ok = true;
	fill(V, V+C, 0);
	for (int i=0; i<R; ++i) {
	    cin >> P[i];
	    if (! ok) continue;
	    if (i > 0) {
		int j=0; for (; j+1<C; ++j) {
		    if (V[j]) {
			assert(P[i-1][j] == '/');
			if (P[i][j] != '#') ok = false;
			else P[i][j] = '\\';
			assert(P[i-1][j+1] == '\\');
			if (P[i][j+1] != '#') ok = false;
			else P[i][j+1] = '/';
		    }
		}
	    }
	    fill(V, V+C, 0);
	    if (i+1 == R && P[i].find('#') != P[i].npos)
		ok = false;
	    int j=0; for (; j+1<C; ++j) {
		if (P[i][j] == '#') {
		    V[j] = true;
		    P[i][j] = '/';
		    if (P[i][j+1] != '#') ok = false;
		    P[i][j+1] = '\\';
		}
	    }
	    if (P[i][j] == '#') ok = false;
	}
	printf("Case #%d:\n", t+1);
	if (ok) 
	    for (int i=0; i<R; ++i) printf("%s\n", P[i].c_str());
	else
	    printf("Impossible\n");
    }
}
