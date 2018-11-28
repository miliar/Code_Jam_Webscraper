#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

char room[100][100];

int main()
{
	int T;
	scanf("%d",&T);
	for (int test=1; test<=T; ++test)  {

		int R,C;
		scanf("%d%d",&R,&C);
		for (int i=0; i<R; ++i) {
			scanf("%s",room[i]);
		}
		bool notpossible = false;
		for (int i=0; i<R && !notpossible; ++i) {
			for (int j=0; j<C && !notpossible; ++j) {
				if (room[i][j] == '#') {
					if (j+1 < C && i+1 < R) {
						if (room[i][j+1] == '#' && room[i+1][j] == '#' && room[i+1][j+1] == '#') {
							room[i][j]='/';room[i][j+1]='\\';room[i+1][j]='\\';room[i+1][j+1]='/';
						}
						else
						{
							notpossible = true;
						}
					}
					else {
						notpossible = true;
					}
				}
			}
		}
		printf("Case #%d:\n", test);
		if (notpossible) {
			printf("Impossible\n");
		}
		else {
			for (int i=0; i<R; ++i) {
				for (int j=0; j<C; ++j) {
					printf("%c",room[i][j]);
				}
				printf("\n");
			}
		}
		
	}
	return 0;
}
