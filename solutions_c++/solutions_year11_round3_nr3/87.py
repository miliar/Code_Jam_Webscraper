#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define eps	1e-15

typedef long long int lint;

bool divide(lint a, lint b)
{
	if ( a < b ) swap(a, b);
	return a % b == 0;
}

void solve()
{
	int n;
   	lint l, h;
	lint f[1001];
	scanf("%d",&n);
	scanf("%I64d%I64d",&l,&h);
	REP(i,n) scanf("%I64d",&f[i]);


	for(; l<=h; l++){
		bool flag = true;
		REP(i,n) {
			if (!divide(f[i], l)) {
				flag = false;
				break;
			}
		}
		if ( flag ) break;
	}

	if ( l > h ) printf("NO\n");
	else printf("%d\n",l);
}

int main(void)
{
	int T;
	scanf("%d",&T);

	REP(i,T) {
		printf("Case #%d: ", i+1 );
		solve();
	}


	return 0;
}

