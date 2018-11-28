#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define LL long long
#define MP make_pair
#define PB push_back
#define PII pair< int, int >
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,L,R) for(int i=L;i<=R;i++)
#define FORD(i,R,L) for(int i=R;i>=L;i--)
#define ALL(i) (i).begin(),(i).end()
#define sz(i) (int)(i).size()
#define INF 10000000
using namespace std;
int n,k,cas;
int p[31];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	p[0]=1;
	FOR(i,1,30)
		p[i]=p[i-1]*2;
	scanf("%d",&cas);
	int cnt=0;
	while(cas--)
	{
		cnt++;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",cnt);
		if((k+1)%(p[n])==0)
			printf("ON\n");
		else 
			printf("OFF\n");
	}
	return 0;
}
