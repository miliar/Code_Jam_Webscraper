#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;
#define rep(i,l,r) for(int i=l;i<=r;i++)
char s[10008];
int n, map[1008], t, cnt = 0;;
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	map[97] = 'y', map[98] = 'h';
	map[99] = 'e', map[100] = 's';
	map[101] = 'o',	map[102] = 'c';
	map[103] = 'v',	map[104] = 'x';
	map[105] = 'd',	map[106] = 'u';
	map[107] = 'i',	map[108] = 'g';
	map[109] = 'l',	map[110] = 'b';
	map[111] = 'k',	map[112] = 'r';
	map[113] = 'z',	map[114] = 't';
	map[115] = 'n',	map[116] = 'w';
	map[117] = 'j',	map[118] = 'p';
	map[119] = 'f',	map[120] = 'm';
	map[121] = 'a',	map[122] = 'q';
	map[' '] = ' ';
	scanf("%d", &t);
	getchar();
	while (t--)
	{
		gets(s);
		++cnt;
		printf("Case #%d: ", cnt);
		n = strlen(s);
		rep(i,0,n-1) printf("%c", map[s[i]]);	
		printf("\n");
	}
	return 0;
}
