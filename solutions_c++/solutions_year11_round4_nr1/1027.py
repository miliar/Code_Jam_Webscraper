#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>
#include <cstdlib>

using namespace std;

const int MaxN = 3000;

const double eps = 1e-7;

struct Corr
{
	int l, r, v;
};
vector<Corr> corr;

int N, X, R, S;
double t;

bool cmp1(Corr a, Corr b)
{
	if (a.l < b.l - eps) return true;
	return false;
}

bool cmp2(Corr a, Corr b)
{
	//double tmpa = (0.0 + a.r - a.l) / (a.v * (a.v + R));
	//double tmpb = (0.0 + b.r - b.l) / (b.v * (b.v + R));
	//if (tmpa > tmpb + eps) return true;
	return a.v < b.v;
}

int main()
{
	int Ncase;
	freopen("a_large.in", "r", stdin);
	freopen("a_large.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		cin >> X >> S >> R >> t >> N;
		corr.clear();
		for (int i = 0; i < N; ++i)
		{
			int l, r, v;
			cin >> l >> r >> v;
			corr.push_back((Corr){l, r, v + S});
		}

		int tmp = 0;
		for (int i = 0; i < N; ++i)
		{
			if (tmp < corr[i].l)
				corr.push_back((Corr){tmp, corr[i].l, S});
			tmp = corr[i].r;
		}
		if (tmp < X)
			corr.push_back((Corr){tmp, X, S});
		R -= S;
		sort(corr.begin(), corr.end(), cmp2);

/*
		cout << R << endl;
		for (int i = 0; i < corr.size(); ++i)
			cout << corr[i].l << " " << corr[i].r << " " << corr[i].v << " " << 
			(0.0 + corr[i].r - corr[i].l) / (corr[i].v * (corr[i].v + R))
			<< endl;
*/
		double sum = 0;
		for (int i = 0; i < corr.size(); ++i)
		{
			double tmp;
			double remains = corr[i].r - corr[i].l;
			if (t > eps)
			{
				tmp = remains / (corr[i].v + R);
				if (tmp > t) tmp = t;
				sum += tmp;
				remains -= tmp * (corr[i].v + R);
				t -= tmp;
			}
			if (remains > eps)
			{
				tmp = remains / (corr[i].v);
				sum += tmp;
			}
		}
		printf("Case #%d: %.7lf\n", run+1, sum);
//		cout << "Case #" << run+1 << ": " << sum << endl;
	}
}
