#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <locale>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))


typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
const double pi = acos(-1.0);
const int inf =(int) 1e9;


int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d",&t);
	int n,s,p;
	int a,b,x;
	int res;
	FOR(i,t)
	{
		scanf("%d%d%d",&n,&s,&p);
		b=p-2;
		if (b<1)
			b=0;
		a=p+b+b;
		res=0;
		FOR(j,n)
		{
			scanf("%d",&x);
			b=x/3;
			if (x%3!=0)
				++b;
			if (b>=p)
			{
				++res;
				continue;
			}
			if (x>=a && s>0)
			{
				++res;
				--s;
			}
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}