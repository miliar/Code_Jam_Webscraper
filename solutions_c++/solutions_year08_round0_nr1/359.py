#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) ((x).begin, (x).end)
#define eps	1e-15

typedef long long int lint;

int solve()
{
	int c;
	map<string, int> m;
	string s;
	scanf("%d",&c);
	char buf[255];
	gets(buf);

	REP(i, c) {
		gets(buf);
		s = buf;
		m[s] = i;
	}
	
	char check[200];
	memset(check, 0, 200);
	int cnt = 0;
	int ret = 0;

	int q;
	scanf("%d", &q);
	gets(buf);
	REP(i, q) {
		gets(buf);
		s = buf;
		int t = m[s];
		if (check[t] == 0) {
			if (++cnt == c) {
				ret++;
				cnt = 1;
				memset(check, 0, 200);
			}
			check[t] = 1;
		}
	}
	
	return ret;
}


int main(void)
{
	int test;
	int cnt = 0;
 	scanf("%d", &test);

	REP(i, test)
		printf("Case #%d: %d\n", ++cnt, solve());

	return 0;
}

