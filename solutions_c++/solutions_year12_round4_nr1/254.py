#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <ctime>
#include <memory.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define mem0(a) memset(a, 0, sizeof(a))
#define mem1(a) memset(a, -1, sizeof(a))
#define pb push_back

double calc(double a, double b, double or)
{
	if(a > b)
		return 0;
	else
	{
		return min(or, a);
	}
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int TESTs;
	scanf("%d",&TESTs);
	for(int test = 1; test <= TESTs; test++)
	{
		printf("Case #%d: ",test);
		int N;
		scanf("%d",&N);
		vector<pair<double,double>> lians;
		vector<double> best;
		for(int i = 0; i < N; i++)
		{
			double a,b;
			scanf("%lf%lf",&a,&b);
			lians.push_back(make_pair(a,b));

		}
		double D;
		scanf("%lf",&D);
		best.resize(N);
		best[0] = lians[0].first;
		bool possible = false;
		for(int i = 0; i < N; i++)
		{
			if(lians[i].first + best[i] + 1e-6 > D)
				possible = true;
			for(int j = i + 1; j < N; j++)
				best[j] = max(best[j], calc(lians[j].first - lians[i].first, best[i], lians[j].second));
		}
		if(possible)
			printf("YES");
		else
			printf("NO");

		printf("\n");
	}
	return 0;
}