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

int N;
vector<vector<int>> wins;

void readCase()
{
	scanf("%d\n", &N);
	wins.clear();
	wins.resize(N);
	for(int i = 0; i < N; i++) 
	{
		char buf[200];
		gets(buf);
		for(int j = 0; j < N; j++) 
		{
			int win = -1;
			if(buf[j] == '1') win = 1; else if(buf[j] == '0') win = 0;
			wins[i].push_back(win);
		}
	}
}

void solve()
{
	vector<double> WPsum;
	vector<int> WPcnt;
	vector<double> WP;
	vector<double> OWP;
	double OWPsum = 0;
	vector<double> OOWP;

	for(int i = 0; i < N; i++)
	{
		double sum = 0;
		int cnt = 0;
		for(int j = 0; j < N; j++) 
		{
			if(j == i) continue;
			if(wins[i][j] >= 0) sum += wins[i][j], cnt++;
		}
		WPsum.push_back(sum);
		WPcnt.push_back(cnt);
		WP.push_back(sum/cnt);
	}
	
	for(int i = 0; i < N; i++)
	{
		double sum = 0;
		for(int j = 0; j < N; j++) 
		{
			if(j == i || wins[i][j] < 0 ) continue;
			sum += ( WPsum[j] - wins[j][i] ) / ( WPcnt[j] - 1 );
		}
		OWP.push_back( sum / WPcnt[i] );
	}

	for(int i = 0; i < N; i++)
	{
		double sum = 0;
		for(int j = 0; j < N; j++) 
		{
			if(j == i || wins[i][j] < 0 ) continue;
			sum += OWP[j];
		}
		OOWP.push_back( sum / WPcnt[i] );
	}

	for(int i = 0; i < N; i++)
	{
		printf( "\n%.12f", 0.25 * ( WP[i] + OOWP[i] ) + 0.5 * OWP[i] );
	}
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
	}
	return 0;
}

