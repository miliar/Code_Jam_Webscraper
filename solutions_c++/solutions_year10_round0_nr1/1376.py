#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)

char msg[2][4] = {"OFF","ON"};

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int TT; cin >> TT;
	forn(tt,TT)
	{
		int n,k;
		cin >> n >> k;
		printf("Case #%d: %s\n",tt+1,msg[((k+1) & ((1<<n)-1)) == 0]);
	}
	return 0;
}