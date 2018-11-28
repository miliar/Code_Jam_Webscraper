#pragma comment(linker, "/STACK:64000000")
#include <iostream> 
#include <stdio.h> 
#include <cmath> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <queue> 
#include <sstream> 
#include <utility> 
#include <map> 
#include <set> 
#include <memory.h> 
using namespace std; 
 
#define forn(i, n) for(int i = 0; i < (int) (n); ++i) 
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i) 
 
#define ll long long 
#define ld long double 
#define PLL pair <ld, ld> 
#define PII pair <int, int> 
#define pb push_back 
#define sz size

const ld EPS = 1e-7; 

const int MAXN = 510;

const int MAXS = int(1e6 + 1e-6 + 5);
const ll BASE = int(1e9 + 1e-1 + 9); 
const ld PI = 3.1415926535897932384626433832795; 
const int INF = 1e30;



string solve() {
	string s[4];
	char tmp[10];

	forn(i, 4) {
		scanf("%s", &tmp);
		s[i] = tmp;
	}

	int a[300];
	int x = 'X', o = 'O', t = 'T';
	bool finished = 1;

	forn(i, 4) {
		memset(a, 0, sizeof a);

		forn(j, 4) {
			a[s[i][j]]++;					
		}

		if (a[x] == 4 || a[x] == 3 && a[t] == 1) return "X won";
		if (a[o] == 4 || a[o] == 3 && a[t] == 1) return "O won";
		
		if (a['.']) finished = 0;
	}
	forn(j, 4) {
		memset(a, 0, sizeof a);

		forn(i, 4) {
			a[s[i][j]]++;					
		}

		if (a[x] == 4 || a[x] == 3 && a[t] == 1) return "X won";
		if (a[o] == 4 || a[o] == 3 && a[t] == 1) return "O won";
	}	
	
	memset(a, 0, sizeof a);
	forn(i, 4) {
		a[s[i][i]]++;
	}

	if (a[x] == 4 || a[x] == 3 && a[t] == 1) return "X won";
	if (a[o] == 4 || a[o] == 3 && a[t] == 1) return "O won";

	memset(a, 0, sizeof a);
	forn(i, 4) {
		a[s[3 - i][i]]++;
	}

	if (a[x] == 4 || a[x] == 3 && a[t] == 1) return "X won";
	if (a[o] == 4 || a[o] == 3 && a[t] == 1) return "O won";

	if (finished) return "Draw";
	return "Game has not completed";
}

int main()  { 
     
    freopen("input.txt","rt", stdin); 
    freopen("output.txt", "wt", stdout);     
    
	int tk;
	cin >> tk;

	fore(test, 1, tk + 1) {
		string ans = solve();		
		printf("Case #%d: %s\n", test, ans.c_str());
	}
    return 0; 
}