#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define eps	1e-15

typedef long long int lint;

int a[1048576];
int c[1048576];

lint solve()
{
	int l, n, cc;
	lint t;
	scanf("%d%I64d%d%d",&l,&t,&n,&cc);
	REP(i,cc) scanf("%d",&c[i]);

	int jj = 0;
	REP(i,n) {
		if ( jj == cc ) jj = 0;
		a[i] = c[jj++];
	}

	lint result = 0;
	vector<int> v;
	v.reserve(n);
	REP(i,n) {
		lint next = result + a[i] * 2;
		if ( next >= t ) {
			if ( next > t ) {
				v.push_back((int)(next-t) / 2);
			}
			result = t;
			for(int j=i+1; j<n; j++)
				v.push_back(a[j]);
			break;
		}
		result = next;
	}

	if ( !v.empty() ) {
		sort(v.begin(), v.end(), greater<int>() );
		for(int i=0; i<v.size(); i++) {
			if ( l > 0 ) {
				result += v[i];
				l--;
			} else result += v[i]*2;
		}
	}
	return result;
}

int main(void)
{
	int T;
	scanf("%d",&T);

	REP(i,T) {
		printf("Case #%d: ", i+1 );
		printf("%I64d\n", solve() );		
	}


	return 0;
}

