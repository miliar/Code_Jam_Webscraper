#include <iostream>
#include <cstdio>
#include <math.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

long gcd(long a, long b)
{
	if (b==0) return a;
	else return gcd(b,a%b);
}

bool check(long long n, long pd, long pg)
{
	if ((pd>0 && pg==0) || (pd<100 && pg==100)) return false;
	if (pd==0) return true;
	if (100/gcd(pd,100)<=n) return true;
	else return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);

	long long n;
	long pd, pg;
	long TextNum, Tnum = 0;
	cin >> TextNum;
	while (TextNum--) {
		++Tnum;
		cout << "Case #" << Tnum << ": ";
		cin >> n >> pd >> pg;
		if (check(n,pd,pg)) cout << "Possible" << endl;
		else cout << "Broken" << endl;
	}
	return 0;
}