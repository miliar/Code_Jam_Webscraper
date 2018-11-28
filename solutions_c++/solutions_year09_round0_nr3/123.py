#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <list>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i(a), _n(b); i<=_n; i++)
#define FR(i,b) FOR(i,0,b-1)
#define REP(i,a,b) for(int i(a), _n(b); i >= _n; i--)
#define _M(a) memset(a,0,sizeof(a))
#define IN scanf
#define OUT printf
#define sqr(q) ((q)*(q))
#define ll long long
#define ul unsigned ll
#define INF 1000000000

int KT;
const char C[] = "welcome to code jam";

int a[100];
int b[100];
char s[600];

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	IN("%d\n", &KT);
	
	FOR(test, 1, KT)
	{
		gets(s);
		_M(a);
		
		for(int i = 0; s[i]; i++)
		{
			
			_M(b);
			if (s[i] == 'w') b[0] = 1 + a[0]; else b[0] = a[0];
		
			FOR(j,1,18)
			{
				b[j] = (a[j-1] * (C[j] == s[i]) + a[j]) % 10000;			
			}
			
			FR(j,19) a[j] = b[j];
		}
		int c = a[18];
		OUT("Case #%d: ", test);
		if (c < 1000) cout << 0;
		if (c < 100) cout << 0;
		if (c < 10) cout << 0;
		cout << c << endl;
 	}
	

	return 0;
}
