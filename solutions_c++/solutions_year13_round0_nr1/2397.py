#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
#include <cstring>
using namespace std;


#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair


typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;

map<char,int> line[10];

void init() {
	forn(i,10) line[i].clear();
}

int main() {
        #ifdef LOCAL
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
        #endif

		int ncas; cin >> ncas;
        forn(cas,ncas) {
        	cout << "Case #" << cas+1 << ": ";
        	init();

        	int empty = 0;
        	forn(i,4) forn(j,4) {
        		char c; cin >> c;
        		if (c == '.') {
        			empty++;
        			continue;
        		}
        		line[i][c]++;
        		line[j+4][c]++;
        		if (i == j) line[8][c]++;
        		if (i + j == 3) line[9][c]++;
        	}

        	char winner = ' ';
        	forn(i,10) {
        		if (line[i]['X'] + line[i]['T'] == 4) {
        			winner = 'X'; break;
        		}
        		else if (line[i]['O'] + line[i]['T'] == 4) {
        			winner = 'O'; break;
        		}
        	}
        	if (winner == ' ')
        		winner = (empty ? 'N' : 'D');

        	if (winner == 'N')
        		cout << "Game has not completed" << endl;
        	else if (winner == 'D')
        		cout << "Draw" << endl;
        	else
        		cout << winner << " won" << endl;
		}

        return 0;
}
