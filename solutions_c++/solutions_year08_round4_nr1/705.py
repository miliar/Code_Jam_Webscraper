#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <cmath> 
#include <queue>
#include <fstream>
#include <map>

using namespace std;

#define FOR(i,a) for(int i=0; i<a.size(); i++) 
#define FR(i,n) for(int i=0; i<n; i++)
#define FR2(i,start,n) for(int i=start; i<n; i++)
#define VI vector <int>
#define VS vector <string>
#define SZ(a)  (int)((a).size())
#define SORT(a) sort(a.begin(),a.end())    
#define PB(a,b) ((a).push_back(b))

int vValue(VI values, vector <bool> isAnd, int M)
{
	// int ret = -1;
	for(int i=(M-1)/2 - 1; i>=0; i--)
	{
		int a = values[2*i + 1]; int b = values[2*(i+1)];
		if(isAnd[i]) { values[i] = min(a,b); }
		else { values[i] = max(a,b); }
		//cout << i << " " << values[i] << endl;
	}
	return values[0];
}

void main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int testCases; string temporary; getline(in,temporary); stringstream sinple(temporary); sinple>>testCases;
	for(int tst=0; tst<testCases; tst++)
	{	
		int M, V; in >> M >> V; vector <int> twoPows; int tem = 1; while(tem<=10000) { PB(twoPows,tem); tem*=2; }
		VI values(M,0); vector <bool> isAnd(M,false); vector <bool> canChange(M,false);
		for(int i=0; i<(M-1)/2; i++)
		{
			int G, C; in >> G >> C;
			if(G==1) isAnd[i] = true;
			if(C==1) canChange[i] = true;
		}
		for(int i=0; i<(M+1)/2; i++)
		{
			int l; in >> l; values[(M-1)/2 + i]=l;
		}
		
		VI bla(2,1000000); vector<VI> dp(M,bla); 

		for(int i=(M-1)/2; i<M; i++)
		{
			dp[i][values[i]] = 0;
		}
		
		// cout << vValue(values,isAnd,M) << endl;
		for(int i=(M-1)/2 - 1; i>=0; i--)
		{
			
			    int d = dp[2*i+1][1]+dp[2*(i+1)][1];
				int a = dp[2*i+1][1] + dp[2*i+2][0]; int b = dp[2*i+1][0]+dp[2*i+2][1]; int c = dp[2*i+1][0]+dp[2*i+2][0];
				int g0and = min(a,min(b,c));
				int g1and = d;
				int g0or = c;
				int g1or = min(a,min(b,d));
			if(isAnd[i]&&!canChange[i])
			{
				dp[i][1] = min(dp[i][1],g1and);
				dp[i][0] = min(dp[i][0],g0and);
			}
			
			if(isAnd[i]&&canChange[i])
			{
				dp[i][1] = min(dp[i][1],min(g1and,1+g1or));
				dp[i][0] = min(dp[i][0],min(g0and,1+g0or));
			}
			
			if(!isAnd[i]&&!canChange[i])
			{
				dp[i][1] = min(dp[i][1],g1or);
				dp[i][0] = min(dp[i][0],g0or);
			}
			
			if(!isAnd[i]&&canChange[i])
			{
				dp[i][1] = min(dp[i][1],min(g1or,1+g1and));
				dp[i][0] = min(dp[i][0],min(g0or,1+g0and));
			}
		}
		
		out << "Case #" << tst+1 << ": ";
		if(dp[0][V]==1000000) out << "IMPOSSIBLE" << endl;
		else out << dp[0][V] << endl;
		
		
	}
}
