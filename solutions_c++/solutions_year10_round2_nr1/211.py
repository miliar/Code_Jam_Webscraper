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

int n, m;
char buff[500];

VS getVS() {
	gets(buff);
	int k = strlen(buff);
	REP(j,k)
		if( buff[j] == '/' ) buff[j] = ' ';

	stringstream stream;
	stream.str(string(buff));
	string cmd;
		
	VS vec;
	while(stream>>cmd)
		vec.PB(cmd);
	return vec;
}

void solve(int test_number) {
	scanf("%d %d\n",&n,&m);
	
	vector<VS> v;
	VS x;
	v.PB(x);
	
	FOR(i,1,n) 
		v.PB(getVS());
	
	int res = 0;
	
	FOR(i,1,m) {
		VS vec = getVS();
		int best = 1<<30;
		REP(j,SIZE(v)) {
			VS& v0 = v[j];
			int k = 0;
			
			while(k<SIZE(v0)&&k<SIZE(vec)) {
				if(v0[k] != vec[k]) break;
				++k;
			}
			int ans = SIZE(vec) - k;
			best = min(best,ans);
		}
		v.PB(vec);
		res += best;
	}
	
	
	printf("Case #%d: %d\n",test_number,res);
}





int main() {
	int number_of_tests;
	scanf("%d\n",&number_of_tests);
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

/*
struct node {
	string id;
	vector<*node> v;
};


void add(string x,node& root)
{
	int ok = 0;
	
	REP(i,SIZE(root.v))
	{
	
	}
}
*/

















