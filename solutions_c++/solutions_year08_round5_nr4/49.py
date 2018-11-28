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
const int MOD = 10007;
int fact[66666667];
int fastpow(int n, int k)
{
	if(k==0)
		return 1;
	int res = fastpow(n, k/2);
	res = (res*res)%MOD;
	if(k%2)
		res = (res*n)%MOD;
	return res;
}
int modinv(int n)
{
	return fastpow(n,MOD-2);
}
int ways(int dx, int dy)
{
	if((2*dy-dx)%3)
		return 0;
	if((2*dx-dy)%3)
		return 0;
	if(2*dy-dx<0)
		return 0;
	if(2*dx-dy<0)
		return 0;
	int A = (2*dy-dx)/3;
	int B = (2*dx-dy)/3;
	int T = A+B;
	int res = fact[T];
	res = (res*modinv(fact[A]))%MOD;
	res = (res*modinv(fact[B]))%MOD;
	return res;
}
pii rocks[10];
int main()
{
	fact[0] = 1;
	for(ll i = 1; i<=66666666; i++)
		fact[i] = int((fact[i-1]*i)%MOD);
	int TESTS;
	scanf("%d", &TESTS);
	FOR(tests,TESTS)
	{
		fprintf(stderr, "TEST %d\n", tests+1);
		int H, W,R;
		scanf("%d%d%d", &H, &W, &R);
		int res = 0;
		FOR(i,R)
			scanf("%d%d", &rocks[i].first, &rocks[i].second);
		sort(rocks, rocks+R);
		FOR(s,1<<R)
		{
			int bits = 0;
			int r = 1;
			int c = 1;
			int ret = 1;
			FOR(i,R)
			{
				if(s&(1<<i))
				{
					bits++;
					ret = (ret*ways(rocks[i].first-r, rocks[i].second-c))%MOD;
					r = rocks[i].first;
					c = rocks[i].second;
				}
			}
			ret = (ret*ways(H-r, W-c))%MOD;
			if(bits%2)
			{
				res = (res-ret+MOD)%MOD;
			}
			else
			{
				res = (res+ret)%MOD;
			}
		}
		printf("Case #%d: %d\n", tests+1, res);
	}
	return 0;
}
