#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <string>
#include <cmath>
#include <iostream>
#include <stack>
#include <queue>
#include <ctime>
#include <utility>
#include <bitset>
#include <memory.h>
#include <deque>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define forn(i, a, b) for (int (i) = a; (i) < (b); (i)++)
#define ford(i,a,b) for (int i(a);i>=(b);--i)
#define sqr(n) (n)*(n)
#define all(v) (v).begin(), (v).end()
#define mem0(a) memset(a,0,sizeof(a))
#define mem1(a) memset(a,-1,sizeof(a))

#define INF 2000000000

typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<pll> vll;

typedef pair<int, int> pii;
typedef vector<pii> vii;

typedef vector<int> vi;
typedef vector<vi> vvi;

bool f[1000010];

int main()
{
	//freopen("C-small.in","r",stdin);
	//freopen("C-small.out","w",stdout);

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	mem0(f);
	for(int i = 2; i < 1000010; i++)
		if(!f[i])
			for(int j = 2 * i; j < 1000010; j+=i)
				f[j] = true;

	int T;
	scanf("%d",&T);
	for(int z = 0; z < T; z++){
		printf("Case #%d: ",z+1);
		long long N;
		scanf("%lld",&N);
		long long up = 1;
		long long down = 0;
		for(int i = 2; i <= min(N,(long long)1000001); i++ )
			if(!f[i])
				down++;
		for(int i = 2; i <= min(N,(long long)1000001); i++)
			if(!f[i]){
				long long c = N;
				while(c>=(long long)i){
					c/=(long long)i;
					up++;
				}
			}
		if(N==(long long)1)
			up--;
		printf("%lld",up - down);
		printf("\n");
	}

	return 0;
}