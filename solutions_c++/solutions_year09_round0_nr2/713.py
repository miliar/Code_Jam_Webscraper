#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int globalcount = 0;

typedef vector<int> VI;
typedef vector<VI> VVI;

VVI label(102,VI(102, -1)), grid(102,VI(102, 20000));

int flood(int x, int y){

	int num[4];
	int i, min, minn;

	if (label[x][y] > -1) return label[x][y];

	//height, width
	
	num[0] = grid[x-1][y];
	num[1] = grid[x][y-1];
	num[2] = grid[x][y+1];
	num[3] = grid[x+1][y];

	min = 20000;
	for (i=0; i<4; i++){
		if (min > num[i]){
			min = num[i];
			minn = i;
		}
	}

	if (min < grid[x][y]){
		if (minn == 0) label[x][y] = flood(x-1,y);
		if (minn == 1) label[x][y] = flood(x,y-1);
		if (minn == 2) label[x][y] = flood(x,y+1);
		if (minn == 3) label[x][y] = flood(x+1,y);
	}
	else

		label[x][y] = globalcount++;

	return label[x][y];
}

int main()
{

	int p, num_maps;
	int i, j;
	int h, w;

	scanf("%d", &num_maps);
	for (p=1; p <= num_maps; p++){

		globalcount = 0;

		scanf("%d%d", &h, &w);

		for (i=0; i<=h+1; i++) {
			for (j=0; j<=w+1; j++){
				grid[i][j] = 20000;
				label[i][j] = -1;
			}
		}

		//		printf("....%d\n", grid[0].size());
		for (i=1; i<=h; i++)
			for (j=1; j<=w; j++)
				scanf("%d", &grid[i][j]);

		for (i=1; i<=h; i++){
			for (j=1; j<=w; j++){

				if (label[i][j] == -1) flood(i,j);


				//				if (j < w) printf(" ");

			}
			//						printf("\n");
		}

		printf("Case #%d:\n", p);
		for (i=1; i<=h; i++){
			for (j=1; j<=w; j++){

				printf("%c", label[i][j] + 97);
				if (j < w) printf(" ");

			}
			printf("\n");
		}



	}
	return 0;
}

