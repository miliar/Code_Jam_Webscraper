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
const int mn=2048;
LL INF=1e15;
int P,M[mn], ticket[2*mn];
LL dp[mn][20];

LL go ( int pnode , int chosen )
{
	if ( pnode >= (1<<P) )
	{
		if ( P - chosen <= M[pnode - (1<<P)] )
			return 0;
		else
			return INF;
	}
	LL & res = dp[pnode][chosen];
	if ( res != -1 ) return res;
	res = INF;
	
	res = ticket[pnode] + go ( 2*pnode , chosen + 1 ) + go ( 2*pnode+1 , chosen + 1  );
	res = min ( res , go ( 2*pnode , chosen ) + go ( 2*pnode + 1 , chosen ) );
	return res;
}

int main()
{
	int kase_;
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		cin >> P;
		for ( int i=0;i<(1<<P);i++ ) cin >> M[i];

		int sz = (1<<P-1);
		for ( int i=0;i<P;i++ )
		{
			for ( int j=sz;j<2*sz;j++ )
				cin >> ticket[j];
			sz/=2;
		}
		memset ( dp , -1 , sizeof ( dp ) );
		LL result = go ( 1 , 0 );
		
		cout <<"Case #" << kase <<": " << result << endl;
	}
	return 0;
}
