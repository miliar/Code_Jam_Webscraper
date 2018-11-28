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

int ok(int x, int y)
{
	vector <int> d1, d2, nd;
	while(x) d1.PB(x % 10), x /= 10;
	while(y) d2.PB(y % 10), y /= 10;
	FORV(i, d2)
		if(d2[i] == d1[0])
		{
			vector <int> tmp;
			FOR(j, i, SZ(d2)) tmp.PB(d2[j]);
			FOR(j, 0, i) tmp.PB(d2[j]);
			if(tmp == d1) return true;
		}
	return false;
}

int main()
{
	int cases, a, b;
	scanf("%d", &cases);
	FOR(c, 1, cases + 1)
	{
		int res = 0;
		scanf("%d %d", &a, &b);
		FOR(i, a, b + 1)
			FOR(j, i + 1, b + 1)
				res += ok(i, j);
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}