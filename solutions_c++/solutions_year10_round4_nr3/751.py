#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>
#include<set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

using namespace std;

int R, COUNT, H, W;
int x[100][100];

void trans(){

	COUNT = 0;
	for(int r = H - 1; r >= 0; r--){
		for(int c = W - 1; c >= 0; c--){

			if(x[r][c]){

				if((!r || !x[r - 1][c])&&
						(!c || !x[r][c - 1])
						){
					x[r][c] = 0;
				}
			}
			else{
				if((r && x[r - 1][c]) &&
						(c && x[r][c - 1])
					){
					x[r][c] = 1;

				}
			}

			COUNT += x[r][c];
		}
	}

}

int main()
{
	
	int ncase, cidx;

	scanf("%d", &ncase);
	for(cidx = 1; cidx <= ncase; cidx++){
		memset(x, 0, sizeof(x));

		scanf("%d", &R);

		H = W = 0;

		for(int i = 0; i < R; i++){

			int x1, x2, y1, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

			H = MAX(H, y2);
			W = MAX(W, x2);


			for(int r = y1; r <= y2; r++){
				for(int c = x1; c <= x2; c++){
					x[r - 1][c - 1] = 1;
				}
			}


		}
		/*
		for(int r = 0; r < H; r++){
			for(int c = 0; c < W; c++){
				printf("%d", x[r][c]);
			}
			printf("\n");
		}
		*/

		long ret = 0;
		do{

			trans();

			ret++;
		}while(COUNT);

		printf("Case #%d: %ld\n", cidx, ret);


	}
	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */
