#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;

#define sz size()
#define pb push_back
#define MAX 0x3FFFFFFF
#define all(x) (x).begin(),(x).end()
#define For(i,n) for(int i=0, _n=(n);i<_n;++i)
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i)
#define Forit(it,x) for(typeof((x).begin()) it=(x).begin(), ed=(x).end();it!=ed;++it)

ll a[1024];
ll b[1024];
ll c[1024];

int main()
{
	int tn;
	int ti = 0;
	int M = 1000000007;
	FILE *in = fopen("C-small-attempt1.in","r");
	FILE *out = fopen("output.txt","w");
	//in = stdin;
	//out = stdout;
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		int n, m;
		ll X, Y, Z;
		fscanf(in,"%d %d %lld %lld %lld",&n,&m,&X,&Y,&Z);
		For(i,m) fscanf(in,"%lld",&a[i]);
		For(i,n)
		{
			b[i] = a[i%m];
			a[i%m] = (X*a[i%m] + Y*(i+1))%Z;
		}
		For(i,n) 
		{
			c[i] = 1;
			For(j,i) if(b[j] < b[i]) {c[i] += c[j]; c[i] %= M;}
		}
		ll ans = 0;
		For(i,n) {ans += c[i]; ans %= M;}
		fprintf(out,"Case #%d: %lld\n", ++ti, ans);
	}
}