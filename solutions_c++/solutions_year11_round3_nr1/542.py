
#include <stdio.h>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int r,c;
char a[64][64];

int main(int argc, char const* argv[])
{
	int case_count;
	scanf("%d", &case_count);
	for (int case_index = 0; case_index < case_count; case_index++) {
		printf("Case #%d:\n", case_index + 1);
		scanf("%d%d", &r, &c);
		memset(a, 0, sizeof(a));
		for (int y = 0; y < r; y++) {
			for (int x = 0; x < c; x++) {
				scanf(" %c", &a[y][x]);
			}
		}
		// greedy fill
		for (int y = 0; y < r; y++) {
			for (int x = 0; x < c; x++) {
				if (a[y][x] == '#' && a[y][x+1]=='#' 
					&& a[y+1][x] == '#' && a[y+1][x+1] == '#') {
					// replace them
					a[y][x] = a[y+1][x+1] = '/';
					a[y+1][x] = a[y][x+1] = '\\';
				}
			}
		}
		bool ok = true;
		for (int y = 0; y < r; y++) {
			if (ok)
			for (int x = 0; x < c; x++) {
				if (a[y][x] == '#') {
					ok = false;
					break;
				}
			}
		}

		if (ok) {
			for (int y = 0; y < r; y++) {
				for (int x = 0; x < c; x++) {
					putchar(a[y][x]);
				}
				puts("");
			}
		} else puts("Impossible");


	}
	
	return 0;
}
