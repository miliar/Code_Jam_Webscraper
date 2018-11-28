#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define iss istringstream
#define oss ostringstream
#define prv(vec) {for(int zz = 0; zz < vec.size(); ++zz) cout << vec[zz] << " "; cout << endl;}
#define sz(a) ((a).size())
#define len(a) ((a).length())
#define all(c) (c).begin(),(c).end() 
#define forn(i,a,n) for(int i = (int) a; i < (int)n; i++) 

int a[100];
string s;

int main()
{
	freopen("b4.in","rt",stdin);
    freopen("b4.out","wt",stdout); 
	int T;
	cin >> T;
	forn(t,0,T)
	{
		cin >> s;
		int n = s.length(), tmax = 1, res = 0;
		long long ts;
		forn(i,0,n) s[i] -= '0';
		forn(i,0,n-1) tmax *= 3;
		// 0 - 
		// 1 +
		// 2 sp
		forn(i,0,tmax)
		{
			int k = i, zn, r = 0;
			long long last = 0;
			forn(j,0,n-1) a[j] = 0;
			while ( k > 0 ) { a[r] = k%3; k /= 3; r++; }
			ts = 0;
			last = s[0];
			zn = 1;
			forn(j,0,n-1)
			{
				if ( a[j] == 0 ) { ts += last * zn; zn = -1; last = s[j+1]; }
				else if ( a[j] == 1 ) { ts += last * zn; zn = 1;  last = s[j+1]; }
				else last = last * 10 + s[j+1];
			}
			ts += last * zn;
		//	cout <<"x" << ts <<" ";
			if ( ts%2 == 0 ) res++;
			else if ( ts%3 == 0 ) res++;
			else if ( ts%5 == 0 ) res++;
			else if ( ts%7 == 0 ) res++;
		}		
		cout << "Case #" << t+1 <<": " << res << endl;
		//printf("Case #%d: %lld\n",t+1,ts);
	}
    return 0;
}