// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 

int main() {
	vector<string> sl;
	int ile,slownik,leng;
	scanf("%d%d%d",&leng,&slownik,&ile);
	REP(i,slownik) {
		char tmp[500];
		scanf("%s",tmp);
		sl.push_back(tmp);
	}

	bool pocz = false;
	FOR(iile,1,ile) {
		bool poss[20][30]; REP(i,20) REP(j,30) poss[i][j]=false;
		char tmp[500];
		scanf("%s",tmp);
		string quest = tmp;
		int poz = (-1);
		REP(i,quest.size()) {
			if (quest[i]=='(') {
				poz++;
				pocz = true;
			} else if (quest[i]==')') {
				pocz = false;
			} else {
				if (!pocz) poz++;
				poss[poz][int(quest[i]-'a')]=true;
			}
		}

		int wynik = 0;
		REP(i,sl.size()) {
			bool niet = false;
			REP(j,leng) if (!poss[j][int(sl[i][j]-'a')]) {
				niet = true;
				j=leng;
			}
			if (!niet) wynik++;
		}
		
/*
		REP(i,leng) {
			cout << "(";
			REP(j,26) if (poss[i][j]) cout << (char(j+'a'));
			cout << ")" << endl;
		}
*/	


		printf("Case #%d: %d\n",iile,wynik);
	}
	return 0;
}

