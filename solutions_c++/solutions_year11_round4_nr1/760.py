#	include <cstring>
#include <cstdio>
#include <iostream>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
using namespace std;
const int inf = 1000 * 1000 * 1000;
const long double eps = 1e-9;
const int maxn = 300;
bool m[30][30];
vector < int > ppp ;
vector < pair < pair < int , int > , int > > vp;
long double ans;
int len, speedgo , speedrun;
int n,runtime;
bool prov(vector < int > ppp)
{
	int ff = ppp.size() - 1;
		for (int j = 0; j < ff; j++)
			if (m[ppp[ff]][ppp[j]] == false)
				return false;						
	return true;
}
long double make_ans()
{
	vector <pair <int, pair < int , int >>> v;
	long double go = len;
	for (int i = 0 ; i < ppp.size(); i++)
	{
		v.push_back(make_pair(vp[ppp[i]].second,vp[ppp[i]].first));
		go -= vp[ppp[i]].first.second - vp[ppp[i]].first.first;  
	}
	long double run = runtime;
	long double ret = 0;
	long double buf;
	buf = go / speedrun;
	if (buf > run)
	{
		ret = (go - run * speedrun) / speedgo + run;
		run = 0;
	}
	else
	{
		run -= buf;
		ret = buf;
	}

	sort(v.begin(),v.end());
	for (int i = 0 ; i < v.size(); i++)
	{
		long double clast  = v[i].first;
		long double rast = v[i].second.second - v[i].second.first; 
		if (rast < run * (speedrun+ clast))
		{
			ret += rast / (speedrun+ clast);
			run -= rast / (speedrun+ clast);
		}
		else
		{
			ret += (rast - run * (speedrun + clast)) / (speedgo + clast) + run;
			run = 0;
		}
	}
	return ret;
}
void rec(int i)
{
	ans = min(ans, make_ans());
	for (int k = i; k < n; k++)
	{
		ppp.push_back(k);
		if (prov(ppp))
		{
			rec(k + 1);
		}
		ppp.pop_back();
	}
}
void make_matr()
{
	for (int i = 0; i < n; i++)
		for (int j = 0 ; j < n; j++)
			m[i][j] = (i == j) | (vp[i].first.first >= vp[j].first.second | vp[i].first.second <= vp[j].first.first);
				
}
void test1(int i)
{
	map < pair < int ,int > , int > mp;
	ans = inf;
	mp.clear();
	cin >> len;
	cin >> speedgo;
	cin >> speedrun;
	cin >> runtime;
	cin >> n;
	vp.clear();
	for (int i = 0 ; i < n; i++)
	{
		int a , b , c;
		cin >> a >> b >> c;
		vp.push_back(make_pair (make_pair(a,b),c));
	}
	sort(vp.begin(),vp.end());
	make_matr();
	rec(0);
	cout.fixed;
	cout.precision(10);
	cout << "Case #" << i << ": " << ans << '\n';
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin >> test;
	for (int i = 0 ; i < test; i++)
	{
		test1(i + 1);
		cerr << " : " << i << '\n';
	}

	return 0;
}