#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream input("input.txt");
ofstream output("output.txt");

int w[1000];
int b[1000];
int e[1000];

double _min(double a, double b) { return (a<b)? a: b; }

struct aaa { double su; int ix; };
bool operator<(aaa &a, aaa &b)
{
	return a.su > b.su;
}

int main()
{
	int t;
	input >> t;
	output.precision(7);
	for (int test=1;test<=t;++test)
	{
		int x, s, r, t, n;
		input >> x >> s >> r >> t >> n;
		double tot = t, v2 = 0;
		vector<aaa> rs;
		for (int i=0;i<n;++i)
		{
			int l;
			input >> b[i] >> e[i] >> w[i];
			l = e[i] - b[i];
			x -= l;
			double su = ((double)(r + w[i])) / (s + w[i]);
			//rs[su] = i;
			aaa val;
			val.su = su;
			val.ix = i;
			rs.push_back(val);
			tot += ((double)l)/(s+w[i]);
			v2 += ((double)l)/(r+w[i]);
		}
		if (x)
		{
			double su = ((double)r) / s;
			aaa val;
			val.su = su;
			val.ix = -1;
			rs.push_back(val);
			//rs[su] = -1;
			tot += ((double)x) / s;
			v2 += ((double)x) / r;
		}
		double tt = t;
		sort(rs.begin(), rs.end());
		for (vector<aaa>::iterator it = rs.begin(); it!=rs.end(); ++it)
			//(map<double, int>::reverse_iterator it = rs.rbegin(); it!=rs.rend(); ++it)
		{
			int id = it->ix;
			int l, q;
			if (id==-1) { l = x; q = r; }
			else { l=e[id]-b[id]; q = r + w[id]; }
			double ta = ((double) l) / q;
			double tc = _min(tt, ta);
			tot -= tc * (it->su);
			tt -= tc;
		}
		output << "Case #" << test << ": " << ((v2<=t+1e-6)?v2:tot) << endl;
	}
	return 0;
}