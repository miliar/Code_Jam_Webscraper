#include <iostream>
#include <cstring>

using namespace std;

#define DIM 4

int main()
{
	int cases,t,x,y;
	char cmp;
	int won;

	char matrix[DIM][DIM];
	int exclude_r[DIM], exclude_c[DIM];

	cin>>cases;
	for (t = 0; t < cases; t++){
		won = -1;
		memset(exclude_r, 0, sizeof(int)*DIM);
		memset(exclude_c, 0, sizeof(int)*DIM);

		for(x = 0; x < DIM; x++){
		 for(y = 0; y < DIM; y++){
			cin>>matrix[x][y];
			if (matrix[x][y] == '.'){
				won = 0;
				exclude_c[y] = 1;
				exclude_r[x] = 1;
			}
		 }
		}

		for(x = 0; x < DIM; x++){
			if (exclude_r[x]) continue;
			cmp = (matrix[x][0] == 'T' ? matrix[x][1] : matrix[x][0]);
			for(y = 1; y < DIM; y++)
				if ((matrix[x][y] != cmp) && (matrix[x][y] != 'T')) break;

			if (y == DIM){
				won = (cmp == 'O' ? 1 : 2);
				break;
			}
		}

		if (won < 1){
		 for(x = 0; x < DIM; x++){
			if (exclude_c[x]) continue;
			cmp = (matrix[0][x] == 'T' ? matrix[1][x] : matrix[0][x]);
			for(y = 1; y < DIM; y++)
				if ((matrix[y][x] != cmp) && (matrix[y][x] != 'T')) break;

			if (y == DIM){
				won = (cmp == 'O' ? 1 : 2);
				break;
			}
		 }
		}

		if (won < 1 && matrix[0][0] != '.'){
		 cmp = (matrix[0][0] == 'T' ? matrix[1][1] : matrix[0][0]);
		 for (x = 1; x < DIM; x++)
			if ((matrix[x][x] != cmp) && (matrix[x][x] != 'T')) break;
		 if (x == DIM) won = (cmp == 'O' ? 1 : 2);
		}

		if (won < 1 && matrix[0][DIM-1] != '.'){
		 y = DIM - 1;
		 cmp = (matrix[0][y] == 'T' ? matrix[1][y-1] : matrix[0][y]);
		 for (x = 1; x < DIM; x++)
			if ((matrix[x][y-x] != cmp) && (matrix[x][y-x] != 'T')) break;
		 if (x == DIM) won = (cmp == 'O' ? 1 : 2);
		}

		cout<<"Case #"<<t+1<<": ";
		switch(won){
			case 2:
				cout<<"X won\n";
				break;
			case 1:
				cout<<"O won\n";
				break;
			case 0:
				cout<<"Game has not completed\n";
				break;
			default:
				cout<<"Draw\n";
		}
	}

	return 0;
}
