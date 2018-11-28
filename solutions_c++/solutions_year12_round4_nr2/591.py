#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
#include<sstream>
#include<ctime>
#include<cmath>
#include<set>
#include<queue>
#include<map>
#include<cstdio>
#include<map>
using namespace std;
typedef unsigned long long u64;
typedef long long i64;
typedef unsigned long long u32;
typedef long long i32;
const double EPS = 1e-9;
const double PI = 3.1415926535897932384626433832795;
i64 i64INF = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;
i32 i32INF = 1000 * 1000 * 1000;
const u64 H = 127;
double INF = 1e10;
double mINF = INF + 100.0;

double getRand(double max)
{
	return (double)(rand()) / (double)(RAND_MAX) * max;
}

double norminate(double val, double min, double max)
{
	if(val < min) return min;
	if(val > max) return max;
	return val;
}

double dist(pair<double, double> &a, pair<double, double> &b)
{
	return sqrt((a.first-b.first)*(a.first-b.first) + (a.second-b.second)*(a.second-b.second));
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int t;
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		cerr << test << endl;
		int n, w, l;
		cin >> n >> w >> l;
		vector<pair<double, double> > v(n);
		vector<double> rs(n);
		for(int i = 0; i < n; i++)
			cin >> rs[i];
		for(int i = 0; i < n; i++)
		{
			v[i].first  = getRand(w);
			v[i].second = getRand(l);
		}

		bool bad = true;
		double iter = 1.0;
		while(bad)
		{
			iter += 0.000001;
			bad = false;
			for(int i = 0; i < n; i++)
			{
				for(int j = i+1; j < n; j++)
				{
					if(rs[i]+rs[j] - dist(v[i], v[j]) > EPS)
					{
						bad = true;
						double diff = (rs[i]+rs[j] - dist(v[i], v[j]))/iter;
						if(v[i].first > v[j].first) 
						{
							v[i].first  += getRand(diff); 
							v[j].first  -= getRand(diff); 
						}
						else
						{
							v[i].first  -= getRand(diff); 
							v[j].first  += getRand(diff); 
						}

						if(v[i].second > v[j].second) 
						{
							v[i].second += getRand(diff); 
							v[j].second -= getRand(diff); 
						}
						else
						{
							v[i].second -= getRand(diff); 
							v[j].second += getRand(diff); 
						}



						v[i].first  = norminate(v[i].first,  0.0, w);
						v[i].second = norminate(v[i].second, 0.0, l);
						v[j].first  = norminate(v[j].first,  0.0, w);
						v[j].second = norminate(v[j].second, 0.0, l);
						goto end;
					}
				}
			}
end:		;
		}

		/*for(int i = 0; i < n; i++)
		{
			for(int j = i+1; j < n; j++)
			{
				if(rs[i]+rs[j] - dist(v[i], v[j]) > EPS)
				{
					cerr << "AAAAAAAAAAAA";
				}
			}
		}*/ 


		cout << "Case #" << test << ":";
		for(int i = 0; i < n; i++)
			printf(" %0.12lf %0.12lf", v[i].first, v[i].second);
		cout << endl;
	}

	return 0;
}