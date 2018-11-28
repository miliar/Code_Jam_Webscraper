#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list>
#include <cassert>
#include <conio.h>
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 

char comb[256][256], opp[256][256];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;	
	cin >> T;
	REP(i, T)
	{
		int C, D, N;
		char b1 = 0, b2 = 0, ch = 0;
		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));
		vector<char> res;

		cin >> C;
		REP(k, C)
		{
			cin >> b1 >> b2 >> ch;
			comb[b2][b1] = comb[b1][b2] = ch;
		}

		cin >> D;
		REP(k, D)
		{
			cin >> b1 >> b2;
			opp[b1][b2] = opp[b2][b1] = 1;
		}

		cin >> N;
		REP(k, N)
		{
			cin >> ch;
			if (res.empty()) 
			{
				res.push_back(ch);
				continue;
			}
			b1 = comb[res.back()][ch]; 
			if (b1 != 0) 
			{
				res.pop_back();
				res.push_back(b1);
				continue;
			}
			FOR(n, 0, res.size())
				if (opp[res[n]][ch] == 1) 
				{
					res.clear(); 
					break;
				}
			if (!res.empty()) res.push_back(ch);
		}


		cout << "Case #" << i+1 << ": [";
		int count = res.size();
		FOR(n, 0, count) 
		{
			cout << res[n];
			if (n < count - 1) cout << ", ";
		}
		cout << "]" << endl;
	}

	//getch();
	return 0;
}