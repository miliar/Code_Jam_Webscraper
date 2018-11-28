//============================================================================
// Name        : C.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#define MAXN 102

int M,tmp,num,step;
bool mat[MAXN][MAXN];

int main() {
	int cas,cnt=0,i,j,k,x1,x2,y1,y2,maxx,maxy;
	freopen("C-small-attempt0.in", "r", stdin);
	FILE *out;
	out = fopen("output.txt", "w");
	scanf("%d", &cas);
	while(cas--){
		memset(mat,false,sizeof(mat));
		scanf("%d", &M);
		num = 0;
		maxx = 0;
		maxy = 0;
		step = 0;
		for(i = 0; i < M; ++i){
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			maxx = max(max(x1,x2),maxx);
			maxy = max(max(y1,y2),maxy);
			if(x1 > x2){
				tmp = x1;
				x1 = x2;
				x2 = tmp;
			}
			if(y1 > y2){
				tmp = y1;
				y1 = y2;
				y2 = tmp;
			}
			for(j = y1; j <= y2; ++j)
				for(k = x1; k <= x2; ++k){
					if(!mat[j][k]){
						mat[j][k] = true;
						++num;
					}
				}
		}
		while(num){
/*			for(i = 1; i <= maxy; ++i){
				for(j = 1; j <= maxx; ++j)
					printf("%d", mat[i][j]);
				putchar('\n');
			}
			putchar('\n');*/
			for(i = maxy; i >= 1; --i){
				for(j = maxx; j >= 1; --j){
					if(mat[i-1][j] && mat[i][j-1] && !mat[i][j]){
						mat[i][j] = true;
						++num;
					}
					else if(!mat[i-1][j] && !mat[i][j-1] && mat[i][j]){
						mat[i][j] = false;
						--num;
					}
				}
			}

			++step;
		}
		fprintf(out, "Case #%d: %d\n", ++cnt, step);
	}
	fclose(out);
	return 0;
}
