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


/*
The first line of the input gives the number of test cases, C. C test cases follow. Each test case starts with 4 integers on a line -- N, K, B and T. The next line contains the N different integers Xi, in increasing order. The line after that contains the N integers Vi. All distances are in meters; all speeds are in meters per second; all times are in seconds. 
*/

int pos[100];
int speed[100];
int bad[100];


void solve(int test_number) {
	int  n, k, b, t;
	scanf("%d %d %d %d",&n,&k,&b,&t);

	FOR(i,1,n)	
		bad[i] = 0;
	
	FOR(i,1,n)
		scanf("%d",&pos[i]);
	FOR(i,1,n)
		scanf("%d",&speed[i]);
	
	int ok = 0;
	int up = 0;
	FORD(i,n,1)
	{
		int x = pos[i];
		int v = speed[i];
		
		if( x + t*v >= b ) {
			++ok;			
			FOR(j,i+1,n)
				if(bad[j]) ++up;
			if(ok == k) break;
		}
		else
		{
			bad[i] = 1;
		}
	}
	
	if( ok == k )
		printf("Case #%d: %d\n",test_number,up);		
	else
		printf("Case #%d: IMPOSSIBLE\n",test_number);				
}





int main() {
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















