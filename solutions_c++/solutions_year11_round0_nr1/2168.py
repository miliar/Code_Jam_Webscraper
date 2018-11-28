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

inline int getTime(int dest, int start)
{
	return abs(dest-start)+1;
}

int solve(vector< pair<char, int> >& seq)
{
	int n=sz(seq);
	int *sol = new int[n];
	memset(sol, 0, sizeof(int)*n);

	int posO=1, posB=1, ret=0;
	for(int i=0;i<n;i++)
	{
		int reqTime = getTime(seq[i].second, seq[i].first=='O'?posO:posB);

		int redTime = 0;
		for(int j=i-1;j>=0&&seq[j].first!=seq[i].first;j--)
		{
			redTime += sol[j];
		}

		if(redTime>=reqTime)
		{
			ret++;
			sol[i] = 1;
		}
		else
		{
			ret+= reqTime-redTime;
			sol[i] = reqTime-redTime;
		}

		if(seq[i].first=='O')
		{
			posO = seq[i].second;
		}
		else
		{
			posB = seq[i].second;
		}
	}

	delete[] sol;
	return ret;
}

int main()
{
	ifstream in("A-large_again.in");
	ofstream out("bot_trust_LARGE_AGAIN.out");
	int t,n, b;
	char c;

	in>>t;
	for(int i=1;i<=t;i++)
	{
		in>>n;
		vector< pair<char, int> > seq;
		for(int j=1;j<=n;j++)
		{
			in>>c>>b;
			seq.push_back(make_pair(c, b));
		}

		out<<"Case #"<<i<<": "<<solve(seq)<<endl;
	}

	return 0;
}