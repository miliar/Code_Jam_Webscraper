/*
ID:ibraaaa2
PROG: ttwo
LANG: C++
*/
#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;

#include <time.h>

#define sz(a) a.size()
#define vi vector<int>
#define vs vector<string>
#define vii vector< pair<int,int> >
#define all(a) a.begin(),a.end()
#define pb push_back
#define LL long long
#define LD long double

LD getWP(vector<int>& games, int skip=-1)
{
	int c=0, w =0;
	for(int i=0;i<sz(games);i++)
	{
		if(games[i]==-1 || (skip>-1&&i==skip))
			continue;

		if(games[i]==1)
			w++;
		c++;
	}

	return w*1.0/c;
}

void calc(vector< vector<int> >&  games, LD rpi[], int n)
{
	LD wp[100], owpT[100][100], owp[100], oowp[100];
	//memset(owp, 0.0, sizeof(owp));

	for(int i=0;i<n;i++)
	{
		wp[i] = getWP(games[i]);
		for(int j=0;j<n;j++)
		{
			if(i==j)
				continue;
			owpT[i][j] = getWP(games[i], j);
		}

		//cout<<wp[i]<<endl;
	}

	for(int i=0;i<n;i++)
	{
		owp[i] = 0.0;
		int c=0;
		for(int j=0;j<n;j++)
		{
			if(i==j || games[i][j]==-1)
				continue;
			owp[i]+=owpT[j][i];
			c++;
		}

		owp[i]/=c;
		//cout<<owp[i]<<endl;
	}

	for(int i=0;i<n;i++)
	{
		oowp[i]=0.0;
		int c =0;
		for(int j=0;j<n;j++)
		{
			if(i==j||games[i][j]==-1)
				continue;
			c++;
			oowp[i]+=owp[j];
		}
		oowp[i]/=c;

		//cout<<oowp[i]<<endl;
	}

	for(int i=0;i<n;i++)
	{
		rpi[i] = wp[i]*0.25 + 0.5*owp[i]+ 0.25*oowp[i];
	}
}

int main()
{
	ifstream in("A-large.in");
	//ofstream out("A-out.out");

	FILE* out = fopen("A-Large-out.out", "w");
	int t,n;
	char c;
	in>>t;

	for(int i=1;i<=t;i++)
	{
		in>>n;
		vector< vector<int> > games(n);
		for(int j=0;j<n;j++)
		{
			games[j].resize(n);
			for(int k=0;k<n;k++)
			{
				in>>c;
				games[j][k] = c=='.'?-1:c-'0';
			}
		}

		LD rpi[100];
		memset(rpi, 0.0, sizeof(rpi));

		calc(games, rpi,n);
		//out<<"Case #"<<i<<":"<<endl;
		fprintf(out, "Case #%d:\n",i);
		for(int k=0;k<n;k++)
			fprintf(out, "%.7f\n",rpi[k]);
			//out<<rpi[k]<<endl;
	}
	return 0;
}