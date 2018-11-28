/*Author :: Yash*/
#include <iostream>
#include <cassert>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <iterator>
#include <utility>
#include <functional>
#include <bitset>
#include <cctype>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define PF push_front
#define PP pop()
#define EM empty()
#define FOR(i,a,b) for(int i = (int )a;i<(int )b;i++)
#define REP(i,n) FOR(i,0,n)

typedef pair<int,int> pi;
typedef pair<int,pi> tri;
typedef vector<pi> vii;
typedef vector<tri> viii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vi> vvi;

main()
{
	int N , kases = 0;
	for(scanf("%d",&N);N;N--)
	{
		long long  n,A,B,C,D,x0,y0,M;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		//cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long  x[n] , y[n];
		x[0] = x0;y[0] = y0;
		A %= M;
		B %= M;
		C %= M;
		D %= M;
		FOR(i,1,n)
		{
			x[i] = ((A)*x[i-1] +  B)%M;
			y[i] = ((C)*y[i-1] +  D)%M;
		}
		long long ans = 0;

		REP(i,n) FOR(j,i+1,n) FOR(k,j+1,n)
		{
			long long temp = x[i] + x[j] + x[k];
			long long  temp1 = y[i] + y[j] + y[k];
			if(temp%3 == 0  && temp1%3 == 0) 
				ans++;
		}
		kases++;
		printf("Case #%d: %lld\n",kases,ans);
	}
	return 0;
}
