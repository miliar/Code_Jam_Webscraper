//Code by Patcas Csaba
//Time complexity:
//Space complexity:
//Method:
//Implementation time: 

#include <vector>
#include <string> 
#include <set> 
#include <map> 
#include <queue> 
#include <bitset> 
#include <stack>
#include <list>

#include <numeric> 
#include <algorithm> 

#include <cstdio>
#include <fstream>
#include <iostream> 
#include <sstream> 
#include <iomanip>

#include <cctype>
#include <cmath> 
#include <ctime>
#include <cassert>

using namespace std;

#define LL long long
#define PII pair <int, int>
#define VB vector <bool>
#define VI vector <int>
#define VD vector <double>
#define VS vector <string>
#define VPII vector <pair <int, int> >
#define VVI vector < VI >
#define VVB vector < VB >

#define FORN(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, a, b) for(int i = (a); i <= (b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define FORI(it, X) for(__typeof((X).begin()) it = (X).begin(); it !=(X).end(); ++it) 
#define REPEAT do{ 
#define UNTIL(x) }while(!(x)); 

#define SZ size()
#define BG begin() 
#define EN end() 
#define CL clear()
#define X first
#define Y second
#define RS resize
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(), x.end()

ofstream fout("output.txt");

int m, d, n;
vector <PII> a;
VI b;
VD c;

//double Time(double start)
//{
//	double ans = 0;
//	FORN(i, n) 
//	{
//		double newPlace = start + i * d;
//		double t = abs(b[i] - newPlace);
//		ans = max(ans, t);
//	}
//	return ans;
//}

bool Done()
{
	FORN(i, n - 1)
		if ((c[i + 1] - c[i]) < d) return false;
	return true;
}

bool Possible(double time)
{
	c[0] = b[0] - time;
	FOR(i, 1, n - 1)
	{
		if (c[i - 1] + d < b[i] - time) c[i] = b[i] - time;
		else
			if (c[i - 1] + d < b[i] + time) c[i] = c[i - 1] + d;
			else return false;
	}
	return true;
}

double Solve()
{
	//double down = a[0].X - n * d,
	//	   up = a[m - 1].X + n * d;
	//double ans = Time(down);
	//while (down < up)
	//{
	//	double aux = Time(down);
	//	if (ans > aux) ans = aux;
	//	down += 0.1;
	//}
	//return ans;
	//FORN(i, 1000)
	//{
	//	double mid1 = down + (up - down) / 3,
	//		   mid2 = down + (up - down) / 3 * 2;
	//	double ans1 = Time(mid1),
	//		   ans2 = Time(mid2);
	//	if (ans1 < ans2) up = mid2;
	//	else down = mid1;
	//}
	//if (abs(down - a[0].X + n * d) < 0.00001) fout << "!!!!!!!!";
	//if (abs(down - a[m - 1].X - n * d) < 0.00001) fout << "!!!!!!!!";
	//fout << down << " " << a[0].X - n * d << " " << a[m - 1].X + n * d << endl;

	c.CL, c.RS(n);
	double down = 0, up = a[m - 1].X - a[0].X + double (n) * d;
	FORN(i, 500)
	{
		double mid = (down + up) / 2;
		if (Possible(mid)) up = mid;
		else down = mid;
	}
	return down;
}


int main()
{
	freopen("input.txt", "r", stdin);
	int test;
	cin >> test;
	FOR(t, 1, test)
	{
		cout << t << " / " << test << endl;
		cin >> m >> d;
		a.CL, a.RS(m);
		b.CL;
		n = 0;
		FORN(i, m)
		{
			cin >> a[i].X >> a[i].Y;
			FORN(j, a[i].Y) b.PB(a[i].X);
			n += a[i].Y;
		}
		fout << "Case #" << t << ": " << fixed << setprecision(8) << Solve() << endl;
	}
	return 0;
}