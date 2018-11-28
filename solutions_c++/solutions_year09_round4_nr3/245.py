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
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef pair<int,int> PI;
#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define dbge(x) cout << #x << " -> " << (x) << "\n";

const int mn = 128;

int match[mn],seen[mn],G[mn][mn],L,R;

int go ( int u )
{
	if ( seen[u] ) 
		return false;
	seen[u] = 1;
	for ( int i=0;i<R;i++ ) if ( G[u][i] )
	{
		if ( match[i] == -1 || go ( match[i] ) )
		{
			match[i] = u;
			return true;	
		}
	}
	return false;
}


int A[mn][mn],N,K;

void construct()
{
	memset ( G , 0 , sizeof ( G ) );
	for ( int i=0;i<N;i++ ) 
	{
		for ( int j=0;j<N;j++ ) 
		{
			bool good = true;
			for ( int k=0;k<K;k++ ) if ( A[i][k] >= A[j][k] ) good = false;
			G[i][j] = good;
		}
	}
	L = R = N;
}


int main()
{
	int kase_;
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		cin >> N >> K;
		for ( int i=0;i<N;i++ )
		for ( int j=0;j<K;j++ ) cin >> A[i][j];
		construct();		
		int result =0;
		memset ( match , -1 , sizeof ( match ) );
		for ( int i=0;i<L;i++ ) 
		{
			memset ( seen , 0 , sizeof ( seen ) );
			result += go ( i );
		}
		
		cout <<"Case #" << kase <<": " << N-result << endl;
	}
	return 0;
}
