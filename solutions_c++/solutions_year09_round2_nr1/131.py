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
#include <cassert>
#include <set>
using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-9; 
const double PI = acos(-1.0);

int L;
string ss;

vector<vector<int> > G;
vector<double> weights;
vector<string> features;
set<string> need_features;

int Build(int& p)
{
	int res = weights.size();
	weights.push_back(0);
	features.push_back("");
	G.push_back(vector<int>());
	while (ss[p] != '(')
	{
		p++;
	}
	p++;
	int pp = p;
	while (!(ss[pp] >= '0' && ss[pp] <= '9' || ss[pp] == '.'))
	{
		pp++;
	}
	while (ss[pp] != ' ' && ss[pp] != ')' && ss[pp] != '\n')
	{
		pp++;
	}
	stringstream sstr(ss.substr(p, pp - p));
	double w;
	sstr >> w;
	weights[res] = w;
	p = pp;
	while (ss[p] == ' ' || ss[p] == '\n')
	{
		p++;
	}
	if (ss[p] == ')')
	{
		p++;
		return res;
	}
	else
	{
		string ff;
		while(ss[p] != ' ' && ss[p] != '\n')
		{
			ff += ss[p];
			p++;
		}
		features[res] = ff;
		G[res].push_back(Build(p));
		G[res].push_back(Build(p));
	}
	return res;
}
double Solve(int id)
{

	double res = weights[id];
	if (G[id].size() > 0)
	{
		if (need_features.count(features[id]) > 0)
		{
			res *= Solve(G[id][0]);
		}
		else
		{
			res *= Solve(G[id][1]);
		}
	}
	return res;
}

void Go()
{
	ss.clear();
	features.clear();
	G.clear();
	weights.clear();

	cin >> L;
	getchar();
	for (int i = 0; i < L; i++)
	{
		string ts;
		getline(cin, ts);
		ss += ts;
		ss += ' ';
	}


	int ppppp = 0;
	int root = Build(ppppp);

	string res;

	int A;
	cin >> A;
	for (int i = 0; i < A; i++)
	{
		string animal;
		cin >> animal;
		int k;
		cin >> k;
		need_features.clear();
		for (int j = 0; j < k; j++)
		{
			string feature;
			cin >> feature;
			need_features.insert(feature);
		}
		cout.precision(8);
		cout << fixed << Solve(root) << endl;
	}
}

void main()
{
	const string A = "A";
	//const string B = "small";
	const string B = "large";
	freopen((A + "-" + B + ".in").c_str(), "r", stdin);
#ifndef _DEBUG
	freopen((A + "-" + B + ".out").c_str(), "w", stdout);
#endif

	int nn;
	cin >> nn;
	for (int jj = 1; jj <= nn; jj++)
	{
		cout << "Case #" << jj << ": " << endl;
		Go();
	}
}
