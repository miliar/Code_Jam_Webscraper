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
const int MAXN = 617;
const int MAXLEN = 21;
const int PR = 10000;
typedef vector<int> VI; 


const string slowo="welcome to code jam";

int main() {
	int ile;
	char ch[MAXN];
	set<char> szukaj;
	REP(i,slowo.size()) szukaj.insert(slowo[i]);

	scanf("%d",&ile); gets(ch);
	LL wynik[MAXN][MAXLEN];
	FOR(iile,1,ile) {
		REP(i,MAXN) REP(j,MAXLEN) wynik[i][j]=0;
		string check;
		string res = "";
		gets(ch);
		check = ch;

		REP(i,check.size()) if (szukaj.find(check[i])!=szukaj.end()) res+=check[i];
//		cout << res << endl;
		
		if (res[0]==slowo[0]) wynik[0][0]=1;

		FOR(i,1,res.size()) {
			REP(j,slowo.size()) wynik[i][j]=wynik[i-1][j];
			if (res[i]==slowo[0]) wynik[i][0]++;

			FOR(j,1,slowo.size()-1) if (res[i]==slowo[j]) {
				wynik[i][j]+=wynik[i-1][j-1];
				wynik[i][j]%=PR;
			}
		}
		int wart=0;

		if (res.size()!=0) wart = wynik[res.size()-1][slowo.size()-1]; else wart =0;
		string zera="";
		if (wart<1000) zera+="0";
		if (wart<100)  zera+="0";
		if (wart<10)   zera+="0";
//		cout << wynik[res.size()-1][slowo.size()-1] << " " << res.size() << endl;
		printf("Case #%d: %s%d\n",iile,zera.c_str(),wart);
	}
	return 0;
}

