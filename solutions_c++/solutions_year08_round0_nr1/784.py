/* Peter Zielinski, Jagiellonian University, Poland */

#include <cstdio>
#include <queue>
#include <list>
#include <set>
#include <algorithm>
#include <deque>
#include <utility>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define PRINTF(args...) printf(args)
// #define PRINTF(args...)

int test_nr = 0;

const int max_n = 100;

vector<string> szukacze, pytania;
vector<int> graf[max_n];
vector<int> pozycje;

void testcase() {
	szukacze.clear(); pytania.clear();

	printf("Case #%d: ", ++test_nr);
	int s, q;
	cin >> s;
	REP(i,s) graf[i].clear();
	pozycje.clear();
	string t;
	getline(cin,t);
	REP(i,s) {
		string t;
		getline(cin,t);
		szukacze.push_back(t);
	}
	cin >> q;
	getline(cin,t);
	REP(i,q) {
		string t;
		getline(cin, t);
		pytania.push_back(t);
	}
	
	REP(i,s) REP(j,q) if(szukacze[i] == pytania[j]) graf[i].push_back(j);
	REP(i,s) graf[i].push_back(INT_MAX);
	REP(i,s) pozycje.push_back(0);
	
	int res = 0;
	
	int poprzedni;
	
	REP(i,q)
		if(i == 0 || graf[poprzedni][pozycje[poprzedni]] == i) { // jesli trzeba zmieniac
			++res;
			REP(j,s) while(graf[j][pozycje[j]] < i) ++pozycje[j];
			int max_r = -1;
			REP(j,s) if(graf[j][pozycje[j]] > max_r) {
				max_r = graf[j][pozycje[j]];
				poprzedni = j;
			}
		}
	if(res)
	printf("%d\n", res-1);
	else printf("%d\n", res);
}

int main() {
	int t;
	for(cin >> t;t--;) testcase();
	return 0;
}
