#include <map>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

struct Pred
{
	double _p;
	Pred(int P):_p(P/2.0){}
	bool operator()(int l, int r)
	{
		double ld = ((double)l-_p), rd = ((double)r-_p);
		if ( ld < 0) ld = -ld;
		if (rd < 0) rd = -rd;
		return ld < rd;
	}

};

double el(vector<int> &g, int Pi)
{
	g[Pi] = 0;
	double gg = 0;
	for(int i=Pi-1; i >=0; --i)
	{
		if (g[i]) ++gg;
		else break;
	}
	for(int i=Pi+1; i < g.size(); ++i)
	{
		if (g[i]) ++gg;
		else break;
	}
	return gg;
}

double rt(int P, int Q, vector<int> p)
{
	//sort(p.begin(), p.end(), Pred(P));
	sort(p.begin(), p.end());
	double ggs = 0;
	bool first = true;
	do
	{
		vector<int> g;
		g.resize(P);
		for (int i=0; i < P; ++i) g[i] = 1;
		double gs = 0;
		for (int i=0; i < p.size(); ++i) gs += el(g, p[i]);
		if (first) { ggs = gs; first=false;}
		else if (gs < ggs) { ggs = gs; }
	}while (next_permutation( p.begin(), p.end()));
	return ggs;
}

double runTest()
{
	int P, Q;
	cin >> P >> Q;
	vector<int> prs;
	for (int i=0; i < Q; ++i)
	{
		int p;
		cin >> p;
		prs.push_back(p-1);
	}
	return rt(P, Q, prs);
}
int getIntLine()
{
	int v;
	cin >> v;
	string dummy;
	getline(cin, dummy);
	return v;
}
int main()
{
	int T = getIntLine();
	for (int i=0; i < T; ++i)
	{
		double res = runTest();
		printf("Case #%d: %.0f\n", i+1,res);
	}
}
