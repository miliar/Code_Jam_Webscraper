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

int a[1024];

int main()
{
	int tn;
	int ti = 0;
	FILE *in = fopen("A-large.in","r");
	FILE *out = fopen("output.txt","w");
	//in = stdin;
	//out = stdout;
	fscanf(in,"%d",&tn);
	while(tn--)
	{
		int p, k, l;
		fscanf(in,"%d %d %d",&p, &k, &l);
		For(i,l) fscanf(in,"%d",&a[i]);
		if(p*k < l) {fprintf(out,"Case #%d: Impossible\n", ++ti); continue;}
		sort(a,a+l); reverse(a,a+l);
		ll ans = 0;
		int t = 0;
		For(i,p) For(j,k) if(t < l) ans += (ll)(i+1) * (ll)a[t++];
		fprintf(out,"Case #%d: %lld\n", ++ti, ans);
	}
}