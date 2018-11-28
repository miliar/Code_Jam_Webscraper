#include <cstdio>

using namespace std;

int grid[4][4];

int main() {
	int T;
	scanf(" %d", &T);
	for(int t = 0; t < T; t ++) {
		for(int i = 0; i < 4; i ++)
			for(int j = 0; j < 4; j ++) {
				char c;
				scanf(" %c", &c);
				if(c == 'X')
					grid[i][j] = 10;
				if(c == 'T')
					grid[i][j] = 7;
				if(c == 'O')
					grid[i][j] = 200;
				if(c == '.')
					grid[i][j] = 1000;
			}
		bool winx = false, winy = false, comp = true;
		//Rows
		for(int i = 0; i < 4; i ++) {
			int sum = 0;
			for(int j = 0; j < 4; j ++)
				sum += grid[i][j];
			if(sum == 40 || sum == 37)
				winx = true;
			if(sum == 800 || sum == 607)
				winy = true;
			if(sum >= 1000)
				comp = false;
		}
		//Rows
		for(int i = 0; i < 4; i ++) {
			int sum = 0;
			for(int j = 0; j < 4; j ++)
				sum += grid[j][i];
			if(sum == 40 || sum == 37)
				winx = true;
			if(sum == 800 || sum == 607)
				winy = true;
			if(sum >= 1000)
				comp = false;
		}
		//Diagnols
		int sum = 0;
		for(int i = 0; i < 4; i ++) {
				sum += grid[i][i];
			if(sum == 40 || sum == 37)
				winx = true;
			if(sum == 800 || sum == 607)
				winy = true;
			if(sum >= 1000)
				comp = false;
		}
		sum = 0;
		for(int i = 0; i < 4; i ++) {
				sum += grid[i][3 - i];
			if(sum == 40 || sum == 37)
				winx = true;
			if(sum == 800 || sum == 607)
				winy = true;
			if(sum >= 1000)
				comp = false;
		}
		printf("Case #%d: ", t + 1);
		if(winx)
			printf("X won\n");
		else if(winy)
			printf("O won\n");
		else if(!comp)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	return 0;
}
