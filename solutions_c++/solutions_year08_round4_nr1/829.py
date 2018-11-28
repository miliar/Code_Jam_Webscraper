#include <set>
#include <map>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define repa(v)				for(int i=0;i<(sz(v));++i) for(int j=0;j<(sz(v[i]));++j)
#define rep(i, v)			for(int i=0;i<(sz(v));++i)
#define lp(i, cnt)			for(int i=0;i<(cnt);++i)
#define lpi(i, s, cnt)		for(int i=(s);i<(cnt);++i)
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"

typedef long long ll;
const int OO = (int)1e8;	// Note, IF Small may be WRONG, Large may generate OVERFLOW

const int MAX = 20009;

int gate[MAX], change[MAX], leaf[MAX];
int n, v, mxNode;

int AND = 1, OR = 0;

int ANDcase(int v, int x1, int x2, int y1, int y2)
{
	int mn = OO;
	if(v == 1 && x1 >= 0 && y1 >= 0)
		mn = min(mn, x1+y1);
	
	if(v == 0 && x2 >= 0 && (y1 >= 0 || y2 >=0) ) 	mn = min(mn, x2);
	if(v == 0 && y2 >= 0 && (x1 >= 0 || x2 >=0) ) 	mn = min(mn, y2);
	
	return mn;
}

int ORcase(int v, int x1, int x2, int y1, int y2)
{
	int mn = OO;
	if(v == 1 && x1 >= 0 && (y1 >= 0 || y2 >=0) ) 		mn = min(mn, x1);
	if(v == 1 && y1 >= 0 && (x1 >= 0 || x2>=0) ) 		mn = min(mn, y1);
	
	if(v == 0 && x2 >= 0 && y2 >= 0)		mn = min(mn, x2+y2);
	
	return mn;
}

int findMin(int node, int v)
{	
	if(node > mxNode) {
		if(leaf[node] == v)	return 0;
		return -OO;
	}
	
	int x1 = findMin(2*node  , 1);
	int x2 = findMin(2*node  , 0);
	int y1 = findMin(2*node+1, 1);
	int y2 = findMin(2*node+1, 0);
	
	int mn = OO;
	
	if(gate[node] == AND) {
		mn = min(mn, ANDcase(v, x1, x2, y1, y2) );
		
		if( change[node])
			mn = min(mn, 1+ORcase(v, x1, x2, y1, y2) );
	}
	else {
		mn = min(mn, ORcase(v, x1, x2, y1, y2) );
		
		if( change[node])
			mn = min(mn, 1+ANDcase(v, x1, x2, y1, y2) );
	}

	if(mn < 0 || mn > n)	return -OO;
	return mn;
}

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("aa.in", "w", stdout);
	
	int cases;
	cin>>cases;
	
	for (int k = 1; k <= cases; ++k) {
		cin>>n>>v;
		mxNode = (n-1)/2;
		
		lp(i, (n-1)/2)
			cin>>gate[i+1]>>change[i+1];
		
		lp(i, (n+1)/2)
			cin>>leaf[mxNode+i+1];
		
		int f  = findMin(1, v);
		
		cout<<"Case #"<<k<<": ";
		if(f < 0 || f> n)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<f<<"\n";
		
		
	} 
	return 0;
}
