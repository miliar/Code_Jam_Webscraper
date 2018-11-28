#include <stdio.h>
#include <vector>

using namespace std;

#define FORab(i,a,b) for(int i = (a); i < (b); i++)
#define FORn(i,n) FORab(i,0,n)
#define DBG(args...) /*fprintf(stderr, args)*/

typedef float ff;
typedef unsigned long long ii;

#define MAXR 51
#define MAXC 51
char str[MAXC+1], out[MAXR][MAXC];

bool main2() {
	int R, C; scanf("%d %d", &R, &C);
	char str[MAXC+1];

	FORn(r,R) {
		scanf("%s", str);
		FORn(c,C) out[r][c] = str[c];
		out[r][C] = 0;
	}

	FORn(r,R) {
		FORn(c,C) {
			if(out[r][c] == '#') {
				if(c == C-1 || r == R-1 || out[r+1][c] != '#' || out[r][c+1] != '#' || out[r+1][c+1] != '#')
					return false;
				out[r][c] = '/'; out[r][c+1] = '\\';
				out[r+1][c] = '\\'; out[r+1][c+1] = '/';
			}
		}
	}

	FORn(r,R) printf("%s\n", out[r]);

	return true;
}

int main() {
	int T; scanf("%d", &T);

	for(int caseno = 1; caseno <= T; caseno++) {
		printf("Case #%d:\n", caseno);
		if(!main2()) printf("Impossible\n");
	}

	return 0;
}
