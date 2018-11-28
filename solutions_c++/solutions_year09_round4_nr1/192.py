#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<cmath>
#include<algorithm>
#include<set>
using namespace std;

#define sz(q) ((int)(q).size())
#define _fill(mem,v) memset(mem,v,sizeof(mem))
#define FOR(i,q1,q2) for(int i=(q1); i<=(q2); ++i)
#define FORD(i,q1,q2) for(int i=(q1); i>=(q2); --i)
#define FOREACH(it,mp) for(typeof((mp).begin()) it=(mp).begin(); it!=(mp).end(); ++it)

#define isdig(c) ('0'<=(c) && (c)<='9')

#define inbit(i,n) ((n & (1<<i))>0?1:0)
#define bit(i) (1<<i)

#define mp make_pair
#define xx first
#define yy second

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

int N, a[100], ans;
char str[100][100];

void move_forward(int ind, int futind) {
	if( a[ind]<=futind ) return;
	if( a[ind+1]>futind )
		move_forward(ind+1, futind);
	swap(a[ind], a[ind+1]);
	ans++;
}

void resolve(int ind) {
	if( a[ind]<=ind ) return;
	
	if( a[ind+1]>ind )
		move_forward(ind+1, ind);
	swap(a[ind], a[ind+1]);
	ans++;
}

int main() {
	int ntest;
	scanf("%d",&ntest);
	for(int itest=1; itest<=ntest; ++itest) {
		scanf("%d", &N);
		for(int i=0; i<N; ++i) {
			scanf("%s", str[i]);
			a[i] = 0;
			for(int j=0; j<N; ++j)
				if( str[i][j]=='1' )
					a[i] = j;
		}
		
		ans = 0;
		for(int i=0; i<N; ++i)
			if( a[i]>i )
				resolve(i);
		printf("Case #%d: %d\n", itest, ans);
	}
	
	return 0;
}
