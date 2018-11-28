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

int A[800];
int B[800];

int main()
{
	int T;
	scanf("%d", &T);
	FOR(t,T)
	{
		int N;
		scanf("%d", &N);
		FOR(i,N)
			scanf("%d", A+i);
		FOR(i,N)
			scanf("%d", B+i);
		sort(A, A+N);
		sort(B, B+N);
		ll res = 0;
		FOR(i,N)
			res+=(ll)A[i]*(ll)B[N-i-1];
		printf("Case #%d: %lld\n", t+1, res);
	}
	return 0;
}
