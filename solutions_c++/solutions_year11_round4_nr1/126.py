#include <iostream>
#include <map>
#include <iomanip>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;

#define double long double

typedef double answer_type;




#define mp make_pair

const double EPS = 1e-6;

map<int, int> M;

answer_type solve()
{
	int x, s, r, n;
	double t;
	cin >> x >> s >> r >> t >> n;
	int b, e, w;
	r = r - s;
	
	M.clear();
	
	M[s] = x;
	for (int i = 0; i < n; i++)
	{
		cin >> b >> e >> w;
		M[s] -= e - b;
		M[w + s] += e - b;
	}
	
	double T = 0;
	
	for (map<int, int>::iterator it = M.begin(); it != M.end(); it++)
	{
		double len = it->second;
		double sp = it->first;	
		here:
		if (fabs(t) < EPS)
		{
			T += len / sp;
		}
		else
		{
			if (len / (sp + r) < t)
				T += len / (sp + r), t -= len / (sp + r);
			else
			{
				T += t, len -= t * (r + sp), t = 0;
				goto here;
			}
		}
	}
	return T;
}

int main()
{
	int T;
	cin >> T;
	cout << fixed << setprecision(12);
	cerr << fixed << setprecision(12);
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
