#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <cmath>
using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-12; 
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

template <class T> inline string tostring(T x){stringstream ss; ss << x; return ss.str();}
template <class T> inline T stringto(const string &x){T r; stringstream ss(x); ss >> r; return r;}
template <class FROM, class TO> inline TO cast(FROM x){return stringto<TO>(tostring(x));}
template <class T> inline int size(const T &x){return x.size();}
template <class T> void print(const T &M, int n){cout<<'{';for(int i=0;i<n;++i){cout<<M[i];if(i+1<n)cout<<',';}cout<<"}\n";}
template <class T> void print(const T &M, int n, int m){for(int i=0;i<n;++i)print(M[i], m);cout<<'\n';}
template <class T> void print(const vector<T> &M){print(M,M.size());}
template <class T> void split_pb(vector<T> &res, const string &C){res.push_back(stringto<T>(C));}
template <> void split_pb<string>(vector<string> &res, const string &C){res.push_back(C);}
template <class T> vector<T> split(const string &S, const string &D = " ,{}")
{
	vector<T> res;
	int i = 0;
	for(;;)
	{
		for(;i < S.size() && find(D.begin(), D.end(), S[i]) != D.end();i ++);
		if (i >= S.size()) break;
		string C;
		for (;i < S.size() && find(D.begin(), D.end(), S[i]) == D.end(); i ++) C.push_back(S[i]);
		split_pb<T>(res, C);
	}
	return res;
}

int n;
double f, R, t, r, g;
double w, Rm, SS, qrm;
inline double Q(double x)
{
	return x * x;
}
struct point
{
	double x, y;
	point(double x = 0, double y = 0): x(x), y(y) {};
};
double length(const point& a)
{
	return sqrt(Q(a.x) + Q(a.y));
}
double _F(double x, double c2)
{
	double rx = sqrt(qrm - Q(x));
	return (x * rx + qrm * atan2(x, rx)) * 0.5 - c2 * x;
}
double F(double c0, double c1, double c2)
{
	return _F(c1, c2) - _F(c0, c2);
}
double Square(int x, int y)
{
	static point Corners[4];
	static double C[4];
	C[0] = w * x + r + f;
	C[1] = w * (x + 1) - r - f;
	C[2] = w * y + r + f;
	C[3] = w * (y + 1) - r - f;
	if (C[1] <= C[0] || C[3] <= C[2])
	{
		return 0;
	}
	Corners[0] = point(C[0], C[2]);
	Corners[1] = point(C[1], C[2]);
	Corners[2] = point(C[0], C[3]);
	Corners[3] = point(C[1], C[3]);
	int cn = 0;
	for (int i = 0; i < 4; i++)
	{
		double l = length(Corners[i]);
		if (l < Rm)
		{
			cn++;
		}
	}
	if (cn == 4)
	{
		return SS;
	}
	if (cn == 0)
	{
		return 0;
	}
	if (cn == 1)
	{
		double x = sqrt(qrm - Q(C[2]));
		return F(C[0], x, C[2]);
	}
	if (cn == 2)
	{
		return F(C[0], C[1], C[2]);
	}
	if (cn == 3)
	{
		double x = sqrt(qrm - Q(C[3]));
		return (x - C[0]) * (C[3] - C[2]) + F(x, C[1], C[2]);
	}
}
double calc()
{
	double all = PI * Q(R);
	double good = PI * Q(R);
	Rm = R - t - f;
	qrm = Q(Rm);
	w = g + r * 2;
	SS = Q(g - f * 2);
	double an = 0;
	{
		int mmin = R / (w) + 100;
		for (int y = 0; y <= mmin && Square(0, y) > EPS; y++)
		{
			good -= 4 * Square(y, y);
			an = 1;
			for (int x = 0; x < y && abs(an) > EPS; x++)
			{
				an = Square(x, y);
				good -= 8 * an;
			}
		}
	}
	return good / all;
}

void main()
{
	const string file_name = "C-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
	cin >> n;
	for (int jj = 0; jj < n; jj++)
	{
		cin >> f >> R >> t >> r >> g;
		double ans = calc();
		cout << "Case #" << jj + 1 << ": ";
		cout.precision(7);
		cout << fixed << ans;
		cout << '\n';
	}
}
