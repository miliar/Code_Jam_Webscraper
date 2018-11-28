#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <iomanip>
#include <ctime>

using namespace std;

typedef vector <int> VI;
typedef vector <VI> VVI;
typedef long long LL;
typedef long double LD;
typedef vector <LL> VLL;
typedef vector <double> VD;
typedef vector <bool> VB;
typedef vector <string> VS;
typedef vector <VS> VVS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(var,pocz,koniec) for(int var=(pocz);var<=(koniec);var++)
#define FORD(var,pocz,koniec) for(int var=(pocz);var>=(koniec>;var--)
#define FOREACH(it,X) for(__typeof((X).begin()) it=(X).begin();it!=(X).end();it++)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

/////////////////////////////////////////////////////////////////////////////////


int main()
{
	int ncases;
	cin >> ncases;
	string line;
	getline(cin, line);
	int index = 0;
	while(index < ncases)
	{
		index++;
		cout << "Case #" << index << ":";
		/////////////////////////////////

		int m, n;
		
		getline(cin, line);
		SS ss(line);
		ss >> m;
		vector <string> v(m);
		REP(i, m)	getline(cin, v[i]);

		getline(cin, line);
		SS ss1(line);
		ss1 >> n;

		vector <string> q(n);
		REP(i, n) getline(cin, q[i]);

		vector <int> vv(n);
		REP(i, n) REP(j, m) {
			if(q[i] == v[j]) 
				vv[i] = j;
		}

		int num=0;

		vector <bool> sign(m, false);

		int cur=0;
		
		REP(i, n) {
			int j = vv[i];
			
				if(sign[j]==false)
				{
					sign[j]=true;
					cur++;
					if(cur==m)
					{
						num++;
						REP(k, m) sign[k] = false;
						
						sign[j] = true;
						cur = 1;
						//break;
					}
				}
		}
		cout << " " << num << endl;
	}
	return 0;
}
