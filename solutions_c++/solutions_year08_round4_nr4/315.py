#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<deque>
#include<map>
#include<functional>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOREACH(i,x) for(typeof(x)::iterator it=(x).begin(); it!=(x).end(); ++it)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define pb	push_back
#define mp	make_pair
#define eps	1e-15
#define inf 0x3FFFFFFF

typedef long long int int64_t;
typedef long long int lint;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;


void solve()
{
	char s[50001];
	char s1[50001];
	int k;
	int a[16];

	scanf("%d",&k);
	scanf("%s",s);
	int len = strlen(s);

	REP(i,k) a[i] = i;

	int ret = inf;
	do {
		int i = 0;
		int t = 1;
		while(i < len) {
			REP(j, k){
				s1[i+j] = s[i+a[j]];
				if (i+j > 0 && s1[i+j] != s1[i+j-1])
					t++;
			}
			i += k;

		}
			ret = min(ret, t);
	} while(next_permutation(a, a+k));

	printf("%d\n",ret);
}

int main(void)
{
	int t;

	scanf("%d",&t);
	
	REP(i,t) {
		printf("Case #%d: ", i+1);
		solve();
	}
}

