#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
using namespace std;

#define FR(i,a,n) for(int (i) = (a); (i)<(n); (i)++)
#define RF(i,a,n) for(int (i) = int(n)-1; (i)>=(a); (i)--)
#define FOR(i,n) FR(i,0,n)
#define ROF(i,n) RF(i,0,n)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;

int dr[4] = {-1,0,1,0};
int dc[4] = {0,1,0,-1};
char S[10001];
int L;
int perm[16];
int main()
{
	int TESTS;
	scanf("%d", &TESTS);
	FOR(tests, TESTS)
	{
		int k;
		scanf("%d%s", &k, S);
		L = strlen(S);
		FOR(i,k)
			perm[i] = i;
		int res = 1000000;
		do
		{
			char prev = 0;
			int ans = 0;
			FOR(i,L)
			{
				char cur = S[i/k*k+perm[i%k]];
				if(cur!=prev)
				{
					ans++;
					prev = cur;
				}
			}
			if(ans<res)
				res = ans;
		}
		while(next_permutation(perm, perm+k));
		printf("Case #%d: %d\n", tests+1, res);
	}
	return 0;
}
