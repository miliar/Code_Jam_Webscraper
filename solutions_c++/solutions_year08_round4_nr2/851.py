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
	int index = 0;
	while(index < ncases)
	{
		index++;
		cout << "Case #" << index << ":";
		/////////////////////////////////

		LL N,M,A;
		cin>>N>>M>>A;

		if(A>N*M)
		{	cout << " IMPOSSIBLE" << endl; continue; }
		
		bool sign=false;
		REP(i,N+1) REP(j, M+1)
			REP(jj, j+1) REP(ii,i+1)
				if( j*ii + i*jj + (i-ii)*(j-jj)+A==2*i*j)
				{cout << " 0 0 " << i << " " << jj << " " << ii << " " << j << endl; sign=true;goto HERE; }
HERE:
		if(sign==false)
		{
			cout << " IMPOSSIBLE" << endl;
		}









	}
	return 0;
}
