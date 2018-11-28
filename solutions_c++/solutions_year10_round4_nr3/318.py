
#include <cstdio>
#include <cstring>
using namespace std;

const int MAX_X = 200 + 15;
const int MAX_Y = 200 + 15;

bool has[MAX_X][MAX_Y];

int main() {
	int tst;
	scanf("%d", &tst);
	for (int cas = 0; cas < tst; ++cas) {
		int R;
		scanf("%d", &R);
		memset(has, 0, sizeof(has));
		for (int i = 0; i < R; ++i) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
					has[y][x] = true;
		}
		
		for (int res = 0; ; ++res) {
			bool any = false;
			static bool nhas[MAX_X][MAX_Y];
			memset(nhas, 0, sizeof(nhas));
			
//			for (int x = 0; x < 20; ++x, puts(""))
//				for (int y = 0; y < 20; ++y)
//					printf("%c", has[x][y] ? 'x' : '.');
//			puts("");
			for (int x = 0; x < 205; ++x)
				for (int y = 0; y < 205; ++y) {
					if (has[x][y])
						any = true;
					if (has[x][y] && (x > 0 && has[x - 1][y] || y > 0 && has[x][y - 1]))
						nhas[x][y] = true;
					if (!has[x][y] && (x > 0 && has[x - 1][y] && y > 0 && has[x][y - 1]))
						nhas[x][y] = true;
				}
			if (!any) {
				printf("Case #%d: %d\n", cas + 1, res);
				break;
			} else {
				memcpy(has, nhas, sizeof(nhas));
			}
		}
		
		fprintf(stderr, "Solving test case %d..\n", cas + 1);
		fflush(stderr);
	}
	return 0;
}