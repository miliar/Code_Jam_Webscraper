
/***** Author : Kunal *****/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>

using namespace std;

#define F(a,b) for(int a=0;a<b;a++)
#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define S scanf
#define P printf

#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<int, PII> PIII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;

//int d[][2]={{-1.0},{1,0},{0,-1},{0,1}};

int A[30];

void Pre()
{
	FOR(n,2,26)
	{
	int Ans = 0;
	REP(i, 1<<n )
	{
		if( i&(1<<(n-1)) && (i&1)==0  )
		{
			bool fl = true;
			int ctr = n-1;
			while( ctr>1 )
			{
				int tmp = 0;
				REP(x, ctr+1)
				{
					if( i&(1<<x) ) tmp++;
				}
				if( tmp == 1 ) break;
				if( !(i&(1<<(tmp-1))) )
				{
					fl = false;
					break;
				}
				ctr = tmp-1;
			}
			if( fl && (i&1)==0 ) Ans++;
		}
	}
	//P("%d\n", Ans%100003);
	A[n] = Ans%100003;
	}
}
int main()
{
	Pre();
	int t; S("%d", &t);
	REP(tc,t)
	{
		int n; S("%d", &n);
		P("Case #%d: %d\n", tc+1, A[n]);
	}
	return 0;
}
