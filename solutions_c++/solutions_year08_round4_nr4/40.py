#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <boost/foreach.hpp> // www.boost.org
#define foreach BOOST_FOREACH
using namespace std;
typedef long long LL;

vector< vector<int> > d;
int minCost;
void rec(int a, vector<int>& p, int b, int i, int curCost)
{
	if( i==p.size() ) {
		minCost = min(minCost, curCost+d[p.back()][b]);
		return;
	}

	for(int j=i; j!=p.size(); ++j) {
		swap(p[i], p[j]);
		{
			int cc = curCost + d[i==0 ? a : p[i-1]][p[i]];
			if( cc < minCost )
				rec(a, p, b, i+1, cc);
		}
		swap(p[i], p[j]);
	}
}

vector<int> memo;
int rec2(int PrevSym, vector<int>& p, int LEFT, int b)
{
	if( LEFT == 0 )
		return d[PrevSym][b];

	if( memo[LEFT * 16 + PrevSym] >= 0 )
		return memo[LEFT * 16 + PrevSym];

	int minc = 0x7fffffff;
	for(int m=1,i=0; m<=LEFT; m<<=1,++i)
		if( LEFT & m )
		{
			int cc = d[PrevSym][p[i]] + rec2( p[i], p, LEFT & ~m, b );
			minc = min(minc, cc);
		}
	memo[LEFT * 16 + PrevSym] = minc;
	return minc;
}

int solve(int k, const string& S)
{
	d = vector< vector<int> >(k, vector<int>(k));
	for(int i=0; i<k; ++i)
	for(int j=0; j<k; ++j) if(i!=j)
	{
		int cost = 0;
		for(int Z=0; Z<S.size(); Z+=k)
			if( S[Z+i] != S[Z+j] )
				++cost;
		d[i][j] = cost;
		//cout << i << " --> " << j << " : " << cost << endl;
	}

	minCost = 0x7fffffff;
	for(int a=0; a<k; ++a)
	for(int b=0; b<k; ++b) if(b!=a)
	{
		// {a, ...., b}
		int basecost = 1;
		for(int Z=k; Z<S.size(); Z+=k)
			if( S[Z-k+b] != S[Z+a] )
				++basecost;

		if( k == 2 )
			minCost = min(minCost, basecost+d[a][b]);
		else {
			vector<int> p;
			for(int i=0; i<k; ++i) if(i!=a && i!=b)
				p.push_back(i);

			// slow
			//rec(a, p, b, 0, basecost);

			// fast
			int MASK = (1<<p.size())-1;
			memo = vector<int>(MASK*16+16, -1);
			minCost = min(minCost, basecost + rec2(a,p,MASK,b));
		}
	}
	return minCost;
}

int main()
{
	int nCase; cin >> nCase;
	for(int caseNo=1; caseNo<=nCase; ++caseNo)
	{
		int k; cin >> k;
		string S; cin >> S;

		cout << "Case #" << caseNo << ": " << solve(k,S) << endl;
	}
}
