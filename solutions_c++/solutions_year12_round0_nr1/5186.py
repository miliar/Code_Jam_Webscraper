#include <iostream>
#include <cstdio>
using namespace std;
#define FOR(i,a,b) for(long i=a; i<=b; i++)
#define maxn 300

long ntest;
char f[maxn];
string s;

int main()
{	freopen("TEST.IN", "r", stdin);
	freopen("TEST.OUT", "w", stdout);
	scanf("%ld\n", &ntest);

	f[97] = 'y'; f[98] = 'h'; f[99] = 'e'; f[100] = 's'; f[101] = 'o';
	f[102] = 'c'; f[103] = 'v'; f[104] = 'x'; f[105] = 'd'; f[106] = 'u';
	f[107] = 'i'; f[108] = 'g'; f[109] = 'l'; f[110] = 'b'; f[111] = 'k';
	f[112] = 'r'; f[113] = 'z'; f[114] = 't'; f[115] = 'n'; f[116] = 'w';
	f[117] = 'j'; f[118] = 'p'; f[119] = 'f'; f[120] = 'm'; f[121] = 'a';
	f[122] = 'q';
	FOR(test,1,ntest)
	{
		getline(cin, s);
		printf("Case #%ld: ", test);
		FOR(i,0,s.length()-1) cout << f[s[i]];
		if (test != ntest) cout << endl;
	}
	return 0;
}
