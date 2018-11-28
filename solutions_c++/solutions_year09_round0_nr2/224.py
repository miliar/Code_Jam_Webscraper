#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cfloat>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <string>

using namespace std;

#define in(a, b)  (a >= 0 and b >= 0 and a < rows and b < cols)

int move[][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}}, rows, cols, tb[104][104], pai[104*104];

int label[104*104];

int acha(int a) {
	return (pai[a] == a?a:pai[a] = acha(pai[a]));
}

void une(int a, int b) {
	pai[acha(a)] = acha(b);
}

int main(void){
	int ds, x, y, bestY, bestX, i, j, k, tc = 1, nextLabel;
	scanf("%d", &ds);
	while(ds--) {
		scanf("%d%d", &rows, &cols);

		for(i = 0; i < rows; ++i)
			for(j = 0; j < cols; ++j) {
				scanf("%d", &tb[i][j]);
				pai[i*cols+j] = i*cols+j;
				label[i*cols+j] = -1;
			}

		for(i = 0; i < rows; ++i)
			for(j = 0; j < cols; ++j) {
				bestX = i;
				bestY = j;
				for(k = 0; k < 4; ++k) {
					x = i+move[k][0];
					y = j+move[k][1];
					if (in(x, y) and tb[bestX][bestY] > tb[x][y]) {
						bestX = x;
						bestY = y;
					}
				}
//				printf("%d %d %d %d\n", i, j, bestX, bestY);
				une(i*cols+j, bestX*cols+bestY);
			}
		printf("Case #%d:\n", tc++);
		nextLabel = 0;
		for(i = 0; i < rows; ++i){
			for(j = 0; j < cols; ++j) {
				k = acha(i*cols+j);
				if (label[k] == -1)
					label[k] = nextLabel++;
				if (j != 0)
					printf(" ");
//				printf("%d", k);
				printf("%c", char('a'+label[k]));
			}
			puts("");
		}
	}
	return 0;
}
