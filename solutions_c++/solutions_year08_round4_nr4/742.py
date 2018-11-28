#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <stdio.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define REP(i,n)      for(int i=0,len123=(n);i<len123;i++)
#define FOR(i,n,m)    for(int i=(n),len123=(m);i<len123;i++)
#define INF           (1<<28)
typedef long long          LL;
typedef long double        LD;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int,int>      II;

int TC, k;
int mmin;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "rt", stdin);
   // freopen("out.out", "wt+", stdout);
#endif

	scanf("%d", &TC);
	REP(tc, TC)
	{
		scanf("%d", &k);
		mmin = INF;
		
		string x;
		cin >> x;
		
		int len = SZ(x);

		VI p;
		REP(i,k)
			p.push_back(i);

		do
		{
			string s; s.resize(len);
			REP(i,len) {
				int idx = (i/k)*k;
				s[i] = x[idx+p[i%k]];
			}
			
			int res = 1;
			REP(i,len-1)
				if (s[i] != s[i+1])
					res++;

			printf("");
			printf("");

			if (res < mmin)
				mmin = res;
		} while (next_permutation(ALL(p)));

		printf("Case #%d: %d\n", tc+1, mmin);
	}

    return 0;
}


