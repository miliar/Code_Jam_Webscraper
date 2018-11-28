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

const int mod = 100003;
const int mn = 512;
LL dp[mn][mn];
LL F ( int n , int m )
{
	if ( n == 0 && m >= 0 )
		return 1;
	if ( n < 0 )
		return 0;
	if ( m == 0 )
		return 0;
	LL & res = dp[n][m];
	if ( res != -1 )
		return res;
	res = 0;
	for ( int i=1;i<=m;i++ )
		(res += F(n-i,m))%=mod;
	return res;
}

int main()
{
	int kase_;
	int arr[mn][mn];
	memset ( dp ,-1 , sizeof ( dp ) );
	for ( int i=0;i<mn;i++ )
	for ( int j=1;j<mn;j++ ) arr[i][j-1] = F(i,j);
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		int N;
		cin >> N;
		N--;
		LL result = 0;
		for ( int col=0;col<N;col ++ )
			(result += arr[N-1-col][col])%=mod;
			
		cout <<"Case #" << kase <<": " << result << endl;
	}
	return 0;
}
