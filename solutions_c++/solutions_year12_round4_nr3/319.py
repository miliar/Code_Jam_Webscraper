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

bool fit(vector<int> &hst, vector<int> &v)
{
	int n = v.size();
	for(int i = 0; i < n-1; i++)
	{
		for(int j = i+1; j < hst[i]; j++)
			if((v[j]-v[i]) * (hst[i]-i) >= (v[hst[i]]-v[i]) * (j-i))
				return false;
		for(int j = hst[i]+1; j < n; j++)
			if((v[j]-v[i]) * (hst[i]-i) > (v[hst[i]]-v[i]) * (j-i))
				return false;
	}

	return true;
}

vector<int> solve(vector<int> &hst)
{
	int n = hst.size();
	for(int T = 0; T < 100; T++)
	{
		vector<int> v(n);
		for(int i = 0; i < n; i++)
		{
			v[i] = rand()%1000;
			if(T==0)v[i]=i;
		}
		sort(v.begin(), v.end());

		vector<int> res(v);
		while(true)
		{
			if(fit(hst, v))
				return v;
			if(!next_permutation(v.begin(), v.end())) break;
		}
	}

	return vector<int> ();
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

		int n;
		cin >> n;
		vector<int> hst(n, -1);
		for(int i = 0; i < n-1; i++)
		{
			cin >> hst[i];
			hst[i]--;
		}

		vector<int> res = solve(hst);
		

		cout << "Case #" << test << ":";
		if(res.empty())
		{
			cout << " Impossible";
		}
		else
		{
			for(int i = 0; i < n; i++)
				cout << " " << res[i];
		}
		cout << endl;
	}

	return 0;
}