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
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;	
	cin >> T;
	REP(i, T)
	{
		int N, S, p;
		cin >> N;
		cin >> S;
		cin >> p;

		int a = 0, b = 0;
		REP(j, N)
		{
			int t;
			cin >> t;

			int t_c, t_d;
			t_c = t / 3;
			t_d = t % 3;
			
			if (t_d == 0)
			{
				if (t_c >= p) ++a;
				else if ((t_c > 0)&(t_c + 1 >=p)) ++b;
			}
			else if (t_d == 1)
			{
				if (t_c + 1 >= p) ++a;
			}
			else
			{
				if (t_c + 1 >= p) ++a;
				else if (t_c + 2 >= p) ++b;
			}
		}
		int res;
		if (S < b) res = S; else res = b;
		res += a;
		cout << "Case #" << i+1 << ": " << res << endl;
	}

	//getch();
	return 0;
}