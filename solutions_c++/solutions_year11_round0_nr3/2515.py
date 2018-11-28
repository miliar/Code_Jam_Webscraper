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
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int T;	
	cin >> T;
	REP(i, T)
	{
		int N;
		cin >> N;
		int sum = 0, xsum = 0, min = 1000000, C;
		REP(k, N)
		{
			cin >> C;
			sum += C;
			xsum ^= C;
			if (C < min) min = C;
		}
		cout << "Case #" << i+1 << ": ";
		if (xsum == 0)
			cout << sum - min << endl;
		else 
			cout << "NO" << endl;
	}

	//getch();
	return 0;
}