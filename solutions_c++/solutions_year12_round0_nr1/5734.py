#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

#define SMALL 1

int main()
{
#if SMALL
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
#else
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif

    map<char, char> M;
	int T;
	string G;
	scanf("%d\n", &T);
	vector<string> input, output;
	M['y'] = 'a';
	M['e'] = 'o';
	M['q'] = 'z';
	input.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	input.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	input.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
	output.push_back("our language is impossible to understand");
	output.push_back("there are twenty six factorial possibilities");
	output.push_back("so it is okay if you want to just give up");

	REP(i,3) REP(j,SZ(input[i])) {
		assert(SZ(input[i]) == SZ(output[i]));
		M[input[i][j]] = output[i][j];
	}
	M['z'] = 'q';
    //REP(i,26) cout << M[i+'a'] << endl;
	for (int tc = 1; tc <= T; ++tc) {
		getline(cin, G);
		string S;
		REP(i,SZ(G)) {
			if (G[i] >= 'a' && G[i] <= 'z') S += M[G[i]];
			else S += G[i];
		}
		cout << "Case #" << tc << ": " << S << endl;
	}

	return 0;
}
