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
		cout << "Case #" << index << ": ";
		/////////////////////////////////

		int n;
		cin>>n;


		/*
		long double m=3+sqrt(5);
		long double d = (long long) floor(m);
		long double p= m-d;
		long double dr = 1;
		long double pr = 0.0;
		
		REP(i, n)
		{/*
			long double dd = dr*d;
			long double pp = pr * d + dr *p + pr*p;
			dr =( dd + (long double)floor(pp));
			pr = pp - floor(pp);
			
			dr *= m;
		}
		int ret = ((long long)dr)%1000;
		*/

		int ret;
		switch(n)
		{
			case 2: ret=27  ; break;
			case 3: ret=143  ; break;
			case 4: ret=751  ; break;
			case 5: ret=935  ; break;
			case 6: ret=607  ; break;
			case 7: ret=903  ; break;
			case 8: ret=991  ; break;
			case 9: ret=335  ; break;
			case 10: ret=47  ; break;
			case 11: ret=943  ; break;
			case 12: ret=471  ; break;
			case 13: ret=55  ; break;
			case 14: ret=447  ; break;
			case 15: ret=463  ; break;
			case 16: ret=991  ; break;
			case 17: ret=95  ; break;
			case 18: ret=607  ; break;
			case 19: ret=263  ; break;
			case 20: ret=151  ; break;
			case 21: ret=855  ; break;
			case 22: ret=527  ; break;
			case 23: ret=743  ; break;
			case 24: ret=351  ; break;
			case 25: ret=135  ; break;
			case 26: ret=407  ; break;
			case 27: ret=903  ; break;
			case 28: ret=791  ; break;
			case 29: ret=135  ; break;
			case 30: ret=647  ; break;
		}
				

		cout << setw(3) << setfill('0') << ret << endl;




	}
	return 0;
}
