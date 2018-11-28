#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>
#include <cctype>
#include <vector>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef pair<int,int> PI;
#define dbg(x) cerr << #x << " -> " << (x) << "\t";
#define dbge(x) cerr << #x << " -> " << (x) << "\n";
const int mn = 1e4;

struct Node
{
	vector < int > children;
	vector < string > names;
} Tree[mn];

int top;

int insert ( int u , string path )
{
//	cout << u << " " << path << endl;
	if ( path.length() == 0 ) 
		return 0;
	string nxt;
	assert ( path[0] == '/' );
	assert ( Tree[u].names.size() == Tree[u].children.size() );
	int pos;
	for ( pos=1;pos < path.length() && path[pos] != '/' ; pos ++ )
		nxt += path[pos];

	for ( int i=0;i<Tree[u].names.size();i++ ) if ( Tree[u].names[i] == nxt )
		return insert ( Tree[u].children[i] , path.substr ( pos ) );	

	Tree[u].names.push_back ( nxt );
	Tree[u].children.push_back ( ++top );

	return 1 + insert ( top , path.substr ( pos ) );
}

void clearall ()
{
	top = 0;
	for ( int i=0;i<mn;i++ )
		Tree[i].children.clear() , Tree[i].names.clear();
}


int main()
{
	int kase_;
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		int N,M;
		cin >> N >> M;
		clearall();
		string path;
		for ( int i=0;i<N;i++ )
		{
			cin >> path;
			if ( path == "/" ) continue;
			insert ( 0 , path );
		}
		int result = 0;
		for ( int i=0;i<M;i++ )
		{
			cin >> path;
			if ( path == "/" ) continue;
			result += insert ( 0 , path );
		}
		dbge(top);
		cout <<"Case #" << kase <<": " << result << endl;
	}
	return 0;
}
