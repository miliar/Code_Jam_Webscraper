#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

double t, tt;
double r, s, x, ls;

typedef pair<double, double> pii;
#define F first
#define S second

vector<pii> vp;

void add(double l, double v)
{
	double tn = l / (v + r);
	if(tn < t)
	{
		t -= tn;
		tt += tn;
	}
	else
	{
		tt += t;
		l -= (v + r)*t;
		t = 0;
		tt += l / (v + s);
	}
}

int main()
{
	cout << fixed << setprecision(8);
	int TC;
	cin >> TC;
	for(int T=1; T<=TC; T++)
	{
		vp.clear();
		int n;
		cin >> x >> s >> r >> t >> n;
		tt = ls = 0;
		while(n--)
		{
			int b, e, w;
			cin >> b >> e >> w;
			vp.push_back(pii(0, b - ls));
			vp.push_back(pii(w, e - b));
			ls = e;
		}
		vp.push_back(pii(0, x - ls));

		sort(vp.begin(), vp.end());
		for(int i=0; i<vp.size(); i++)
			add(vp[i].S, vp[i].F);
		cout << "Case #" << T << ": " << tt << endl;
	}
	return 0;
}

