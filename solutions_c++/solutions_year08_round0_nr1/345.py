#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())

int S;
vector<string> sengine;
int Q;
vector<string> sequence;

int D[200][2000];
char linebuffer[16384];

void input() {
    sengine.clear();
    sequence.clear();
    fgets(linebuffer, 16384, stdin);
    sscanf(linebuffer, "%d", &S);
    REP(i, S) {
	fgets(linebuffer, 16384, stdin);
	string s = linebuffer;
	sengine.pb(s);
    }
    fgets(linebuffer, 16384, stdin);
    sscanf(linebuffer, "%d", &Q);
    REP(i, Q) {
	fgets(linebuffer, 16384, stdin);
	string s = linebuffer;
	sequence.pb(s);
    }
}

const int infty = 2147000000;

int process() {
    CLR(D, 0);
    REP(i, S) {
	D[S][0] = 0;
    }
    FOR(i, 1, Q+1) {
	REP(j, S) {
	    int bi = i - 1;
	    int cand;
	    D[j][i] = infty;
	    if (sequence[bi] == sengine[j]) { // explode
		continue;
	    }
	    REP(k, S) {
		cand = D[k][bi] + ((j == k) ? 0 : 1);
		D[j][i] = min(D[j][i], cand);
	    }
	}
    }
    int result = infty;
    REP(i, S) {
	result = min(result, D[i][Q]);
    }
    return result;
}


int main() {
    int T;
    fgets(linebuffer, 16384, stdin);
    sscanf(linebuffer, "%d", &T);
    FOR(t, 1, T+1) {
	cout << "Case #" << t << ": ";
	input();
	cout << process() << endl;
    }
    return 0;

}
