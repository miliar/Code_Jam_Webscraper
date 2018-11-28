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


int main()
{

	int N;
	scanf("%d",&N);
	for(int kases=1;kases<=N;kases++)
	{
		long long p,k,l;
		cin >> p  >> k  >> l;
		long long  a[l];
		REP(i,l) scanf("%lld",&a[i]);
		sort(a,a+l);

		long long  ans = 0 , count = 0;
		for(int i=l-1;i>=0;i--)
		{
			count++;
			if(count%k == 0) ans += (long long )a[i]*(long long )(count/k);
			else ans += (long long )a[i]*(long long )(count/k + 1);
		}
		printf("Case #%d: %lld\n",kases,ans);
	}
	return 0;
}
