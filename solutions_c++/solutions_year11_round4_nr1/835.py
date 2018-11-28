#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

int X, R, S, t, N;
vector<int> B;
vector<int> E;
vector<int> w;

void readCase()
{
	scanf("%d %d %d %d %d\n", &X, &S, &R, &t, &N);
	B.clear();
	E.clear();
	w.clear();
	for(int i = 0; i < N; i++) 
	{
		int b, e, wc;
		scanf("%d %d %d\n", &b, &e, &wc);
		B.push_back(b);
		E.push_back(e);
		w.push_back(wc);
	}
}

void solve()
{
	vector<pair<int, int>> ways;

	int sLen = 0;

	for(int i = 0; i < N; i++)
	{
		ways.push_back(make_pair(w[i], E[i]-B[i]));
		sLen += E[i]-B[i];
	}
	if(sLen < X) ways.push_back(make_pair(0, X - sLen));

	sort(ways.begin(), ways.end(), greater<pair<int,int>>());

	double t = ::t;
	double time = 0;

	while(ways.size())
	{
		double w = ways.back().first;
		double len = ways.back().second;
		ways.pop_back();

		double rt = len / (w + R);
		rt = min(rt, t);
		double st = ( len - rt*(w + R) ) / (w + S);

		t -= rt;
		time += rt + st;
	}

	printf( "%.10f", time );
}

int main()
{
	//string fname = "./test/A-example.in";
	//string fname = "./test/A-small-attempt0.in";
	string fname = "./test/A-large.in";
	
	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
		fprintf(stderr, "Done %d %%     \r", 100 * tCase / T );
	}
	return 0;
}

