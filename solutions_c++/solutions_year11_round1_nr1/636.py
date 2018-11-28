#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;

int gcd(int a, int b){return (b==0)?a:gcd(b,a%b);}
int T,C,p,q,r,s,g; long long N,v;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	scanf ("%d",&T); while (T--){
		scanf ("%lld",&N);
		scanf ("%d %d",&p,&r); q = s = 100;
		g = gcd(p,q); p /= g; q /= g;
		g = gcd(r,s); r /= g; s /= g;
		v = N / q;

		printf ("Case #%d: ",++C);
		if (v < 1 || (q != 0 && s == 0) || (p - q != 0 && r - s == 0) || (p != 0 && r == 0)) printf ("Broken\n");
		else printf ("Possible\n");
	}

	return 0;
}