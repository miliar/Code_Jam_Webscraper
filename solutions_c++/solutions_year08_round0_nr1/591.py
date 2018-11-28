#include <set>
#include <map>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, cnt)			for(int i=0;i<(cnt);++i)
#define repi(i, j, cnt)			for(int i=(j);i<(cnt);++i)
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"

const int S = 1009;
const int Q = 1009;

const int OO = (int)1e8;

int memo[Q][S];
string qs[Q];
string searchE[Q];

int s, q;

int best(int Qidx, int lastS)
{
	if(Qidx == q)	return 0;
	if(memo[Qidx][lastS] != -1)		return memo[Qidx][lastS];
	
	if(searchE[lastS] != qs[Qidx])
		return memo[Qidx][lastS] =best(Qidx+1 , lastS);
	
	int mn = OO;
	rep(i, s) if(searchE[i] != qs[Qidx] )
		mn = min(mn, 1 + best(Qidx+1, i) );
	
	return memo[Qidx][lastS] = mn;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int cases;
	string temp;
	cin>>cases;
	
	for (int k = 1; k <=cases; ++k) {
		clr(memo, -1);
		
		cin>>s;
		getline(cin, temp);
		
		rep(i, s)	getline(cin, searchE[i]);
		
		cin>>q;
		getline(cin, temp);
		
		rep(i, q)	getline(cin, qs[i]);
		
		int mn = OO;
		rep(i, s)
			mn = min(mn, best(0, i) );
		
		cout<<"Case #"<<k<<": "<<mn<<"\n";
		
	}
	return 0;
}
