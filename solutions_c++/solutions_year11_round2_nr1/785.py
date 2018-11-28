/****** String Library */
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>

/****** Containers */
#include <bitset>
#include <deque>
#include <stack>
//#include <queue> //queue - priority_queue
#include <vector>
#include <list>
#include <set> //set - multiset
#include <map> //map - multimap
//#include <iterator> //iterators for !need
//#include <valarray> ???

/****** Algorithms finds... sorts... merges... */
#include <algorithm>

/****** Functions' Adaptors and Objects */
#include <functional>

/****** Mth and Numeric Ops */
#include <cmath>
#include <complex>
#include <numeric>
#include <limits>

/****** Memory Utils */
#include <memory> 

/****** var */
#include <utility> 
#include <iomanip> 
#include <ctime> 

#define FOR(i, m, n) for (int i(m), _n(n); i<_n; ++i)
#define FORd(i, m, n) for (int i(m), _n(n); i>_n; --i)
#define FORc(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define FORr(it,c) for (__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define ALL(c) (c).begin(),(c).end()
#define ALLr(c) (c).rbegin(),(c).rend()

using namespace std;

vector <long double> P[3];
int tt[100][100];
int tc[100], wc[100];

int main()
{
	int N;
	int k;
	int n;

	string s;
	vector <string> st;
	cout << setprecision(16);

	cin >> N;
	FOR(c,1,N+1)
	{
		cin >> n;
		P[0].clear();
		P[1].clear();
		P[2].clear();
		st.clear();

		P[0].resize(n,0.0L);
		P[1].resize(n,0.0L);
		P[2].resize(n,0.0L);

		FOR(i,0,n)
		{
			cin >> s;
			st.push_back(s);
		}
		FOR(i,0,n)
		{
			wc[i] = tc[i] = 0;
			FOR(j,0,n)
			{
				if(st[i][j]=='1')
					++wc[i];
				if(st[i][j] != '.')
					++tc[i];
			}
			FOR(j,0,n)
			{
				if(st[i][j]=='1')
					tt[i][j] = wc[i] - 1;
				if(st[i][j]=='0')
					tt[i][j] = wc[i];
				//cout << " " << tt[i][j];
			}
			//cout << " " << tc[i] << endl;
			P[0][i] = (long double)(wc[i])/(long double)(tc[i]);
		}
		FOR(i,0,n)
		{
			P[1][i]=0.0L;
			FOR(j,0,n)
			{
				if(st[i][j] != '.')
					P[1][i] += (long double)(tt[j][i])/(long double)(tc[j]-1);
			}
			P[1][i] /= tc[i];
			//cout << P[1][i] << endl;
		}
		FOR(i,0,n)
		{
			P[2][i]=0.0L;
			FOR(j,0,n)
			{
				if(st[i][j] != '.')
					P[2][i] += P[1][j];
			}
			P[2][i] /= tc[i];
			//cout << P[2][i] << endl;
		}
		//cout << endl;

		cout << "Case #" << c << ": "<< endl;
		FOR(i,0,n)
			cout << ((P[0][i]+P[2][i])/4 + P[1][i]/2)<< endl;
	}
	return 0;
}
