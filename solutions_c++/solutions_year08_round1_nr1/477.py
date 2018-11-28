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
#define eps 1e-10
/////////////////////////////////////////////////////////////////////////////////


int main()
{
	int ncases;
	cin >> ncases;
	int index = 0;
	while(index < ncases)
	{
		index++;
		cout << "Case #" << index << ":";
		/////////////////////////////////
		
		int n;
		cin>>n;
		vector <int> vx(n), vy(n);
		REP(i, n)
		{	cin >> vx[i];}
		REP(i, n)	cin >> vy[i];

		sort(ALL(vx)); sort(ALL(vy));

		int sum=0;
		REP(i, n) sum += vx[i]*vy[n-i-1];

		cout << " " << sum << endl;






	}
	return 0;
}
