#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define all(x) ((x).begin, (x).end)
#define eps	1e-15

typedef long long int lint;


void extEuclid(int a, int b, int &x, int &y)
{
	int xx = 0; int yy = 1; int lastx = 1; int lasty = 0;
	while(b) {		
		int temp = b;
		int q = a / b;
		b = a % b; a = temp;
		temp = xx;
		xx = lastx - q * xx; lastx = temp;
		temp = yy;
		yy = lasty - q * yy; lasty = temp;
	}
	x = lastx; y = lasty;
}

lint gcd(lint a, lint b)
{
	lint c;
	while(c = a % b) {
		a = b;
		b = c;
	}
	return b;
}


bool solve()
{
	lint n, pd, pg;
	cin >> n >> pd >> pg;
	if ( pd == 0 ) {
		return pg != 100;
	}
	if ( pg == 0 || pg == 100 ) {
		if ( pd == pg ) return true;
		return false;
	}

	lint d1 = 1;
	if ( pd % 5 ) d1 *= 25;
	else if ( pd % 25 ) d1 *= 5;
	if ( pd % 2 ) d1 *= 4;
	else if ( pd % 4 ) d1 *= 2;
	if ( d1 > n ) return false;

	return true;
}

int main(void)
{
	int T;
	scanf("%d",&T);

	REP(i,T) {
		printf("Case #%d: ", i+1 );
		if ( solve() )
			printf("Possible\n");
		else printf("Broken\n");

	}

	return 0;
}

