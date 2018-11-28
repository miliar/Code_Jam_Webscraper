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
#define INF           (1<<30)
typedef long long          LL;
typedef long double        LD;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int,int>      II;

int T, N;
// calculated with default calculator :)
string ans[30] = {"005", "027", "143", "751", "935", "607", "903", "991", "335", "047", "943", "471", "055", "447", "463", 
	              "991", "095", "607", "263", "151", "855", "527", "743", "351", "135", "407", "903", "791", "135", "647"};

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "rt", stdin);
    freopen("out.out", "wt", stdout);
#endif

	scanf("%d", &T);
	REP(tc,T)
	{
		scanf("%d", &N);
		printf("Case #%d: %s\n", tc+1, ans[N-1].c_str());		
	}

    return 0;
}

