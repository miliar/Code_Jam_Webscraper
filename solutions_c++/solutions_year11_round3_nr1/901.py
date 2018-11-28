#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>

using namespace std;
int cn;
int R,C;
char world[70][70];

bool isValid(int i, int j) {
	return i >= 0 && i < R && j >= 0 && j < C;
}

int main() {
	int cases;
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d%d",&R,&C);
		for (int i=0; i < R; ++i) {
			scanf("%s",world[i]);
		}
		bool ok = true;
		for (int i=0; i < R; ++i) {
			for (int j=0; j < C; ++j) {
				if (world[i][j]=='#') {
					if (isValid(i+1,j) && world[i+1][j]=='#' && isValid(i,j+1) && world[i][j+1]=='#' && isValid(i+1,j+1) && world[i+1][j+1]=='#') {
						world[i][j]='/';
						world[i+1][j]='\\';
						world[i][j+1]='\\';
						world[i+1][j+1]='/';
					}
					else {
						ok=false;
						goto end;
					}
				}
			}
		}
		end:

		printf("Case #%d:\n",++cn);
		if (ok) {
			for (int i=0; i < R; ++i) {
				printf("%s\n",world[i]);
			}
		}
		else printf("Impossible\n");
	}


	return 0;
}
