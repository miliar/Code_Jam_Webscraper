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


enum {AND=1, OR=0, LEAF=-1};
struct Node {
	int type; // 1==AND, 0==OR, -1==LEAF
	int val;
	bool changable; // 
};

static const int INF = 0x30000000;

int solve( vector<Node>& t, int V )
{
	vector<int> min_to_0(t.size(), INF);
	vector<int> min_to_1(t.size(), INF);
	for(int x=t.size()-1; x>=1; --x)
	{
		if( t[x].val == 0 ) min_to_0[x] = 0;
		if( t[x].val == 1 ) min_to_1[x] = 0;
		if( t[x].type == LEAF )
			continue;

		int m0L = min_to_0[2*x];
		int m0R = min_to_0[2*x+1];
		int m1L = min_to_1[2*x];
		int m1R = min_to_1[2*x+1];
		int am0 = min(INF, min(m0L+m0R, min(m0L+m1R, m1L+m0R)));
		int am1 = min(INF, m1L+m1R);
		int om0 = min(INF, m0L+m0R);
		int om1 = min(INF, min(m1L+m1R, min(m0L+m1R, m1L+m0R)));
		if( t[x].type == AND ) {
			min_to_0[x] = min(min_to_0[x], am0);
			min_to_1[x] = min(min_to_1[x], am1);
			if( t[x].changable ) {
				min_to_0[x] = min(min_to_0[x], om0+1);
				min_to_1[x] = min(min_to_1[x], om1+1);
			}
		} else if( t[x].type == OR ) {
			min_to_0[x] = min(min_to_0[x], om0);
			min_to_1[x] = min(min_to_1[x], om1);
			if( t[x].changable ) {
				min_to_0[x] = min(min_to_0[x], am0+1);
				min_to_1[x] = min(min_to_1[x], am1+1);
			}
		}
	}
	return (V==0 ? min_to_0 : min_to_1)[1];
}

int main()
{
	int nCase; cin >> nCase;
	for(int caseNo=1; caseNo<=nCase; ++caseNo)
	{
		vector<Node> tree;
		tree.push_back(Node()); // dummy

		int M, V; cin >> M >> V;
		for(int i=0; i<(M-1)/2; ++i)
		{
			int G, C;
			cin >> G >> C;
			Node n = {G,0,C==1};
			tree.push_back(n);
		}
		for(int i=0; i<(M+1)/2; ++i)
		{
			int l;
			cin >> l;
			Node n = {-1,l,false};
			tree.push_back(n);
		}
		for(int x=(M-1)/2; x>=1; --x)
		{
			if( tree[x].type == AND )
				tree[x].val = tree[2*x].val & tree[2*x+1].val;
			else if( tree[x].type == OR )
				tree[x].val = tree[2*x].val | tree[2*x+1].val;
		}

		int ans = solve(tree,V);
		cout << "Case #" << caseNo << ": ";
		if( ans==INF )
			cout << "IMPOSSIBLE";
		else
			cout << ans;
		cout << endl;
	}
}
