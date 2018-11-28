#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <string>
#include <sstream>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<string> VS;
#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FORD(I,A,B) for(int I=(A);I>=(B);--I)
#define FOREACH(I,C) for(typeof((C.begin())) I=(C).begin();I!=(C).end();++I)
#define ALL(A) (A).begin(),(A).end()
#define SIZE(A) (int)(A).size()
#define ST first
#define ND second
#define MP make_pair
#define PB push_back

int go(int mask,int n)
{
	vector<int> v;
	REP(i,n)
	{
		if(mask&(1<<i))
			v.PB(i+2);
	}
	v.PB(n);
	
	int start = n;
	while(1)
	{
		if(start == 1)
		{
			FOREACH(it,v)
			{
				printf("%d ",*it);
				
			}printf("\n");
			return 1;
		}
			
		int ok = 0;
		FOREACH(it,v)
			if(*it == start)
				ok = 1;
	
		if(!ok)
			return 0;
			
		int cnt = 0;
		FOREACH(it,v)
			if(*it <= start) ++cnt;
			
		start = cnt;
	}
}



int MOD = 100003;

int val[43];
void solve(int test_number) {
	int n;
	scanf("%d",&n);
	printf("Case #%d: %d\n",test_number,val[n-1]%MOD);
}


int dp[509][509];
/*
for rows n >= -1, column m >= 0 is given by F(n,m)=F(n-1,m)+F(n-2,m)+...+F(n-m,m) with F(0,m)=1 (m >= 0), F(n,m)=0 (n<0) and F(n,0)=0 (n>0).
*/

int f(int n,int m)
{
	if(n==0&&m>=0) return 1;
	if(n<0) return 0;
	if(n>0&&m==0) return 0;

	int& res = dp[n][m];
	if( res != -1 ) return res;
	
	res = 0;
	for(int i = 1; i <= m; i++)
	{
		res += (f(n-i,m) + MOD )% MOD;
		res %= MOD;
	}
	return res;
}

int main() {
	FOR(i,0,503)
	FOR(j,0,503)	
		dp[i][j] = -1;
/*
	FOR(i,0,10)
	{
		FOR(j,0,10)
			printf("%d  ",f(i,j));
		printf("\n");
	
	}
*/
	FOR(i,0,503)
	{
//		Then a(n) = 1+Sum{2<=h<=n} F(h-1, n-2). 
		val[i] = 0;
		FOR(j,0,i)
		{
			val[i] += ((f(j,i-j) + MOD) % MOD);
			val[i] %= MOD;
		}
//		printf("%d\n",an);
	}


/*
	FOR(i,4,7) {
		int res = 0;
		REP(mask,(1<<(i-2)))
			res += go(mask,i);
		val[i] = res;
	}
*/
	int number_of_tests;
	scanf("%d",&number_of_tests);
	FOR(test_number,1,number_of_tests) solve(test_number);
	return 0;
}





/*

#define MMAX(X,Y) ((X) = max((X),(typeof(X))(Y)))
#define MMIN(X,Y) ((X) = min((X),(typeof(X))(Y)))

#define BITCNT(X) (__builtin_popcount(X))
#define BIT(X,Y) ((X)&(1<<(Y)))
#define FBIT(X) (__builtin_ctz(X))
#define LBIT(X) (31 - __builtin_clz(X))

void solve(int testNum) {
	printf("Case #%d:",testNum);
}

int main() {
	int tests;
	scanf("%d",&tests);
	FOR(test,1,tests) solve(test);
	return 0;
}
*/















