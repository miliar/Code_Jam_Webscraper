#include <iostream>
#include <string>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)

#define esta(x,c) ((c).find(x) != (c).end())

#define INF 1000000000

inline int modu(int x)
{
	return x%10000;
}

#define W 19

char w[20] = "welcome to code jam";

int c[512][20];

int main()
{
	freopen("entrada.in","r",stdin);
	freopen("salida.out","w",stdout);
	int N;
	cin >> N;
	string s;
	getline(cin,s);
	forn(tt,N)
	{
		getline(cin,s);
		int n = s.size();
		forn(i,W)
			c[n][i] = 0;
		forn(i,n+1)
			c[i][W] = 1;
		dforn(i,n)
		forn(l,W)
		{
			int &res = c[i][l];
			res = 0;
			forsn(j,i,n)
			if (s[j] == w[l])
				res = modu(res+c[j+1][l+1]);
		}
		printf("Case #%d: %04d\n",tt+1,c[0][0]);
	}
	return 0;
}

