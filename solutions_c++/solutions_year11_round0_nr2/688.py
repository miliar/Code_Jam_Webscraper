#include <cstdio>
#include <cstring>
#include <list>
#define FOR(i,a,b) for(int i=int(a);i<int(b);++i)
using namespace std;

char C[26][26];
bool D[26][26];
int was[26];
char seq[111];
char buf[111];

inline int ci(char x) {
    return int(x - 'A');
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(z,0,T) {
		int c, d, n, s = 0;
		memset(C, 0, sizeof(C));
		memset(D, 0, sizeof(D));
		memset(was, 0, sizeof(was));
		scanf("%d", &c);
		FOR(i,0,c) {
			char str[4];
			scanf("%s", str);
			C[ ci(str[0]) ][ ci(str[1]) ] = str[2];
			C[ ci(str[1]) ][ ci(str[0]) ] = str[2];
		}
		scanf("%d", &d);
		FOR(i,0,d) {
			char str[3];
			scanf("%s", str);
			D[ ci(str[0]) ][ ci(str[1]) ] = true;
			D[ ci(str[1]) ][ ci(str[0]) ] = true;
		}
		scanf("%d%s", &n, seq);
		FOR(i,0,n) {
			++was[ ci(seq[i]) ];
			buf[s++] = seq[i];
			if(s < 2) continue;
			char cc =  C[ ci(buf[s-1]) ][ ci(buf[s-2]) ];
			if(cc != 0) {
				--was[ ci(buf[s-1]) ];
				--was[ ci(buf[s-2]) ];
				buf[s-2] = cc, --s;
			} else {
				FOR(j,0,26) if(was[j] > 0 && D[ ci(buf[s-1]) ][ j ]) {
					memset(was, 0, sizeof(was)), s = 0;
					break;
				}
			}
		}
		printf("Case #%d: [", z + 1);
		FOR(i,0,s) {
			if(i != 0) printf(", ");
			printf("%c", buf[i]);
		}
		printf("]\n");
	}
	return 0;
}
