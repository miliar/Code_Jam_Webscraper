/*
 * =====================================================================================
 *
 *       Filename:  gcj.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  05/26/2012 09:59:01 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  ronaflx
 *        Company:  hit-ACM-Group
 *
 * =====================================================================================
 */

#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <climits>
#include <algorithm>
#include <iterator>
#include <functional>
#include <limits>
#include <numeric>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <iterator>
#include <stdexcept>
#include <utility>
#include <cassert>
#include <complex>
using namespace std;
#define LT(i) ((i) << 1)
#define RT(i) (((i) << 1) | 1)
#define MID(i) ((l[i] + r[i]) >> 1)
#define CC(i, v) memset(i, v, sizeof(i))
#define REP(i, l, n) for(int i = l;i < int(n);++i)
#define FOREACH(con, i) for(__typeof(con.begin()) i = con.begin();i != con.end();++i)
template<class T>bool checkmax(T &a,T b){return a < b ? a = b, 1 : 0;}
template<class T>bool checkmin(T &a,T b){return a > b ? a = b, 1 : 0;}
typedef long long LL;
typedef pair<int, int> PII;
template<class T> void string_reader(string s, vector<T>& vec){
	istringstream sin(s);
	copy(istream_iterator<T>(sin), istream_iterator<T>(), back_inserter(vec));
}
const int N = 10000;
int dp[N];
int d[N], l[N];
bool check(int n, int D)
{
	memset(dp, 0, sizeof(dp));
	dp[0] = d[0];
	for(int i = 0;i < n;i++)
	{
		for(int j = i + 1;j < n;j++)
		{
			int dst = d[j] - d[i];
			if(dp[i] >= dst)
				checkmax(dp[j], min(dst, l[j]));
		}
	}
	for(int i = 0;i < n;i++)
		if(dp[i] >= D - d[i]) return true;
	return false;

}
int main()
{
	int t, n, D;
	scanf("%d", &t);
	for(int cas = 0;cas < t;cas++)
	{
		scanf("%d", &n);
		REP(i, 0, n) scanf("%d %d", &d[i], &l[i]);
		scanf("%d", &D);
		printf("Case #%d: %s\n", cas + 1, check(n, D) ? "YES" : "NO");
	}
	return 0;
}
