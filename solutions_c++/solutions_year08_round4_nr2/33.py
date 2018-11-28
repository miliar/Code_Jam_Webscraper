#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
using namespace std;

#define FR(i,a,n) for(int (i) = (a); (i)<(n); (i)++)
#define RF(i,a,n) for(int (i) = int(n)-1; (i)>=(a); (i)--)
#define FOR(i,n) FR(i,0,n)
#define ROF(i,n) RF(i,0,n)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;

int dr[4] = {-1,0,1,0};
int dc[4] = {0,1,0,-1};


int N, M;
int factor(int v)
{
	if(v==0)
		return 0;
	for(int i = 1; i*i<=v && (i<=N || i<=M); i++)
	{
		if(v%i==0)
		{
			if(i<=N && v/i<=M)
				return i*10001+v/i;
			if(v/i<=N && i<=M)
				return v/i*10001+i;
		}
	}
	return -1;
}
int main()
{
	int TESTS;
	scanf("%d", &TESTS);
	FOR(tests, TESTS)
	{
		fprintf(stderr, "TEST %d\n", tests+1);
		int A;
		scanf("%d%d%d", &N, &M, &A);
		if(A>N*M)
		{
			printf("Case #%d: IMPOSSIBLE\n", tests+1);
			continue;
		}
		bool done = false;
		for(int a = 0; A+a<=N*M && !done; a++)
		{
			int first = factor(a);
			int second = factor(a+A);
			if(first!=-1 && second!=-1)
			{
				printf("Case #%d: %d %d %d %d %d %d\n", tests+1, 0, 0, second/10001, first%10001, first/10001, second%10001);
				done = true;
			}
		}
		if(!done)
			printf("Case #%d: IMPOSSIBLE\n", tests+1);
	}
	return 0;
}
