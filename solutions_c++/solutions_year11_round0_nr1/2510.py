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


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;	
	cin >> T;
	REP(i, T)
	{
		int N;
		cin >> N;
		int pos1 = 1, pos2 = 1, sum1 = 0, sum2 = 0, diff, p;
		char r;
		REP(k, N)
		{
			cin >> r >> p;
			if (r == 'O')
			{
				diff = abs(pos1 - p) + 1;
				sum1 = (sum1 + diff > sum2) ? sum1 + diff : sum2 + 1;
				pos1 = p;
			}
			else
			{
				diff = abs(pos2 - p) + 1;
				sum2 = (sum2 + diff > sum1) ? sum2 + diff : sum1 + 1;
				pos2 = p;
			}
		}
		cout << "Case #" << i+1 << ": ";
		if (sum1 > sum2) cout << sum1; else cout << sum2;
		cout << endl;
	}

	//getch();
	return 0;
}