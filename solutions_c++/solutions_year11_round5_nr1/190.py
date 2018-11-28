#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <memory.h>
#include <map>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <cstdio>
using namespace std;

#define mp make_pair

template <typename T>
string str(T x)
{
	stringstream s;
	s << fixed << setprecision(20);
	s << x;
	return s.str();
}

typedef string answer_type;

void precalc()
{
	cerr << "Precalc finished" << endl;
}

#define double long double

map<double, double> ML, MU;

#define X first
#define Y second

double get(double m, map<double, double>& M)
{
	double sum = 0;
	for (map<double, double>::iterator it2 = M.begin(), it1 = it2++; it2 != M.end(); it1++, it2++)
	{
		if (it2->X < m)
			sum += (it2->X - it1->X) * (it2->Y + it1->Y) / 2;
		else
		{
			double y = ((m - it1->X) * it2->Y + (it2->X - m) * it1->Y) / (it2->X - it1->X);		
			sum += (m - it1->X) * (y + it1->Y) / 2;
			break;
		}
	}
	return sum;
}

double get(double m)
{
	double u = get(m, MU);
	double l = get(m, ML);
	return u - l;
}

answer_type solve()
{	
	double W;
	int l, u;
	cin >> W >> l >> u;
	double x, y;
	
	int g;
	cin >> g;
	ML.clear(), MU.clear();
	for (int i = 0; i < l; i++)
	{
		cin >> x >> y;
		ML[x] = y;
	}	
	for (int i = 0; i < u; i++)
	{
		cin >> x >> y;
		MU[x] = y;
	}	
	double S = 0;	
	for (map<double, double>::iterator it2 = MU.begin(), it = it2++; it2 != MU.end(); it++, it2++)
		S += (it2->first - it->first) * (it2->second + it->second) / 2;

	for (map<double, double>::iterator it2 = ML.begin(), it = it2++; it2 != ML.end(); it++, it2++)
	{
		//cerr << it->X << ' ' << it->Y << ' ' << it2->X << ' ' << it2->Y << endl;
		S -= (it2->first - it->first) * (it2->second + it->second) / 2;
	}

	double s;
	double m;
	
	string ans = "";
	
	for (int i = 0; i < g - 1; i++)
	{
		s = S * (i + 1) / g;
		double a = 0, b = W;
		while (b - a > 1e-7)
		{
			m = (a + b) / 2;
			if (get(m) < s)
				a = m;
			else
				b = m;
		}
		ans += "\n" + str((b + a) / 2);
	}
	return ans;
}

int main()
{
	precalc();
	int T;
	cin >> T;
	cout << fixed << setprecision(10);
	cerr << fixed << setprecision(10);
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
