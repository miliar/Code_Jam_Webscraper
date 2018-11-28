#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)

#define ll long long
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}



int main()
{
	int i,j ,k;
	int casos;
	cin >> casos;
	double WP[111], OWP[111], OOWP[111];
	for( int h = 0 ; h < casos ;h ++ )
	{
		vector<string> vec;
		int N;
		cin >> N;

		for( i = 0 ; i < N ; i ++ ) { string s; cin >> s; vec.PB(s); }
		// WP...
		for( i = 0 ; i < N ;i  ++ )
		{
			int tot = 0;
			int cant = 0;
			for( j = 0 ; j < N ; j ++ )	
			{
				if( vec[i][j] != '.' ) tot += (vec[i][j]-'0'), cant++;
			}
			WP[i] = tot / (double) cant;
		}
		// OWP...
		double tot = 0.;
		double cant = 0.;
		for( i = 0 ; i < N ;i ++ )
		{
			tot = cant = 0.;
			for( j = 0 ; j < N ; j ++ )
			{
				if( vec[i][j] == '.' ) continue;
				double tot2, cant2; tot2 = cant2 = 0.;
				for( k = 0 ; k < N ; k ++ )
				{
					if( k == i ) continue;
					if( vec[j][k] != '.' )
					tot2 +=(vec[j][k]-'0'), cant2+=1.;
				}

				double prom = tot2/cant2;
					//			if( i == 2 ) cout << "            " << prom << "  " << j << endl;
				tot += prom, cant += 1.;
			}
//			if( i == 2 )cout << "            " << tot << " " << cant  << "  " << j << endl;
			OWP[i] = tot/cant;

		}

		// OOWP
		
		for( i = 0 ; i < N ; i ++ )
		{
			tot = 0., cant = 0.;
			for( j = 0 ; j < N ; j ++ )
			{
				if( vec[i][j] != '.' )
				tot += OWP[j],
				cant+= 1.;
			}
			OOWP[i] = tot  / cant;
		}
		
		
		
		cout << "Case #" << h+1 << ": " << endl;
		cout << setprecision(10);
		for( i = 0 ; i < N ; i ++ )
		{
			cout << 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] << endl;
		}
//		cout << "WP " << endl;
//		for( i = 0 ;i  < N ; i ++ )
//		{
//			cout << OOWP[i] << endl;
//		} cout << 7./12. << endl;
	}return 0;
}

