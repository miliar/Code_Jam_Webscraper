#include <iostream>
#include <ctime>
#include <set>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<n;++i)


int main () {
#ifdef __ASD__
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int tc=1;tc<=t;++tc) {
		string src[4];
		forn(i,4)cin>>src[i];
		bool win = false;
		forn(i, 4) {
			int x=0, o=0, t=0;
			forn(j,4) {
				if (src[i][j]=='X')++x;
				if (src[i][j]=='O')++o;
				if (src[i][j]=='T')++t;
				if (x+t==4) {
					printf("Case #%d: X won\n", tc);						
					win = true;
					goto l;
				} else if (o+t==4) {
					printf("Case #%d: O won\n", tc);						
					win = true;
					goto l;
				}
			}
		}
		forn(i, 4) {
			int x=0, o=0, t=0;
			forn(j,4) {
				if (src[j][i]=='X')++x;
				if (src[j][i]=='O')++o;
				if (src[j][i]=='T')++t;
				if (x+t==4) {
					printf("Case #%d: X won\n", tc);						
					win = true;
					goto l;
				} else if (o+t==4) {
					printf("Case #%d: O won\n", tc);						
					win = true;
					goto l;
				}
			}
		}
		{
			int x=0, o=0, t=0;
			forn(i, 4) {
				if (src[i][i]=='X')++x;
				if (src[i][i]=='O')++o;
				if (src[i][i]=='T')++t;
			}
			if (x+t==4) {
				printf("Case #%d: X won\n", tc);						
				win = true;
				goto l;
			} else if (o+t==4) {
				printf("Case #%d: O won\n", tc);						
				win = true;
				goto l;
			}
		}
		{
			int x=0, o=0, t=0;
			forn(i, 4) {
				if (src[i][3-i]=='X')++x;
				if (src[i][3-i]=='O')++o;
				if (src[i][3-i]=='T')++t;
			}
			if (x+t==4) {
				printf("Case #%d: X won\n", tc);						
				win = true;
				goto l;
			} else if (o+t==4) {
				printf("Case #%d: O won\n", tc);						
				win = true;
				goto l;
			}
		}
		if (!win) {
			bool finished = true;
			forn(i,4)forn(j,4)if(src[i][j]=='.')finished=false;
			if (finished)
				printf("Case #%d: Draw\n", tc);
			else 
				printf("Case #%d: Game has not completed\n", tc);
		}
l:;
	}
	return 0;
}