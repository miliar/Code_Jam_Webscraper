#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)
#define		MP	make_pair
#define		PB	push_back

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;
template<class T> T sqr(T a) { return a * a; }

double dist(double x1, double y1, double x2, double y2)
{
	return sqrt(sqr(x1-x2)+sqr(y1-y2));
}

int main()
{
	ifstream fin("D.in"); ofstream fout("D.out");
	int T;
	fin >> T;
	FOR(tt, T)
	{
		int n;
		fin >> n;

		vector<double> x(n), y(n), r(n);
		FOR(i, n) fin >> x[i] >> y[i] >> r[i];

		while (SZ(x) < 3)
		{
			x.push_back(x[0]);
			y.push_back(y[0]);
			r.push_back(r[0]);
		}

		double R = 1e10;
		R = min( R, max(r[0], 0.5 * (dist(x[1],y[1],x[2],y[2]) + r[1] + r[2])) );
		R = min( R, max(r[1], 0.5 * (dist(x[0],y[0],x[2],y[2]) + r[0] + r[2])) );
		R = min( R, max(r[2], 0.5 * (dist(x[1],y[1],x[0],y[0]) + r[1] + r[0])) );

		fout << fixed << setprecision(10) << "Case #" << tt+1 << ": " << R << endl;
		cout << fixed << setprecision(10) << "Case #" << tt+1 << ": " << R << endl;
	}
	return 0;	
}
