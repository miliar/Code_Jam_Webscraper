#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

int n, w, l;
vector< pair<int,int> > v;
vector< int > r;
vector< pair<double,double> > ret;

bool go()
{
	int x = -v[0].first, y = 0, nextY = v[0].first;
	for (int i = 0; i < v.size(); ++i)
	{
		if (x + v[i].first <= w)
		{
			ret[ v[i].second ] = make_pair(x+v[i].first, y);
			x += 2*v[i].first;
		}
		else
		{
			x = -v[i].first;
			y = nextY + v[i].first;
			nextY = y + v[i].first;
			ret[ v[i].second ] = make_pair(x+v[i].first, y);
			x += 2*v[i].first;
		}
	}
	if (ret[v[n-1].second].second > l)
	{
		cout << "OPS" << endl;
		return false;
	}
	return true;
}

bool verify()
{
	for (int i = 0; i < n; ++i)
		for (int j = i+1; j < n; ++j)
		{
			double dist = sqrt((ret[i].first-ret[j].first)*(ret[i].first-ret[j].first) + 
			                   (ret[i].second-ret[j].second)*(ret[i].second-ret[j].second));
			double vdist = r[i]+r[j];
			if (dist < vdist)
			{
				cout << "PROBLEMA: " << i << " " << j << endl;
				cout << "\t" << ret[i].first << "," << ret[i].second << " " << r[i] << endl;
				cout << "\t" << ret[j].first << "," << ret[j].second << " " << r[j] << endl;
				return 0;
			}
		}
	return 1;
}

int main()
{
	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cin >> n >> w >> l;
		v.resize(n);
		r.resize(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i].first;
			v[i].second = i;
			r[i] = v[i].first;
		}
		sort(v.rbegin(), v.rend());
		
		ret.resize(n);
		go();
		
		verify();
		
		cout << "Case #" << t << ": ";
		for (int i = 0; i < ret.size(); ++i)
		{
			if (i != 0) cout << " ";
			cout << (int)ret[i].first << " " << (int)ret[i].second;
		}
		cout << endl;
	}
}

