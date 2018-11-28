/*********************************HEADER FILES************************************/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <cstring>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SZ(x) ((int)(x).size())
#define FORV(i,x) FOR(i,0,SZ(x))  
#define DBG(x) cout<<(#x)<<" : "<<(x)<<endl
#define PB push_back
#define ALL(x) x.begin(),x.end()

#define ACC(x) accumulate(ALL(x)) 
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define ROFE(i,a,b) for(int i=(b);i>=(a);i--)
#define MP make_pair
#define left(x) (x<<1)
#define right(x) (left(x)+1)
#define PI pair<int,int>
#define PD pair<double,double>
#define F first
#define S second 
#define LL long long
#define ULL unsigned long long
#define MAX 50010

int spl(int s)
{
	
	//x, x, x - 2
	//x, x - 2, x - 2
	//x, x - 1, x - 2
	if((s + 2) % 3 == 0) return (s + 2) / 3;
	if((s + 3) % 3 == 0) return (s + 3) / 3;
	if((s + 4) % 3 == 0) return (s + 4) / 3;
	return -1;
}

int nor(int s)
{
	//x, x - 1, x - 1
	//x, x, x - 1
	//x, x, x
	if((s + 2) % 3 == 0) return (s + 2) / 3;
	if((s + 1) % 3 == 0) return (s + 1) / 3;
	if(s % 3 == 0) return s / 3;
	return -1;
}

int main()
{
	int cases, n, s, p, res, a[110];
	scanf("%d", &cases); string str;
	FOR(c, 1, cases + 1)
	{
		scanf("%d %d %d", &n, &s, &p); res = 0;
		FOR(i, 0, n) scanf("%d", &a[i]);
		sort(a, a + n, greater<int>());
		FOR(i, 0, n)
		{
			int t1 = nor(a[i]), t2 = spl(a[i]);
			if(t1 >= p && a[i] >= 0) res ++;
			else if(s > 0 && t2 >= p && a[i] >= 2) res ++, s --;
		}
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}