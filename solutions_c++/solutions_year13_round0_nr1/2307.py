#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		char m[6][6];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf(" %c", &m[i][j]);
		printf("Case #%d: ", t);
		bool end = false;
		for (int i = 0; i < 4; i++){
			int j;
			for (j = 0; j < 4; j++)
				if(m[i][j] != 'T' && m[i][j] != 'X')
					break;
			if(j == 4){
				printf("X won\n");
				end = true;
				break;
			}
			for (j = 0; j < 4; j++)
				if(m[j][i] != 'T' && m[j][i] != 'X')
					break;
			if(j == 4){
				printf("X won\n");
				end = true;
				break;
			}
			for(j = 0; j < 4; j++)
				if(m[j][j] != 'T' && m[j][j] != 'X')
					break;
			if(j == 4){
				printf("X won\n");
				end = true;
				break;
			}
			for(j = 0; j < 4; j++)
				if(m[j][3-j] != 'T' && m[j][3-j] != 'X')
					break;
			if(j == 4){
				printf("X won\n");
				end = true;
				break;
			}
		}

		for (int i = 0; !end && i < 4; i++){
			int j;
			for (j = 0; j < 4; j++)
				if(m[i][j] != 'T' && m[i][j] != 'O')
					break;
			if(j == 4){
				printf("O won\n");
				end = true;
				break;
			}
			for (j = 0; j < 4; j++)
				if(m[j][i] != 'T' && m[j][i] != 'O')
					break;
			if(j == 4){
				printf("O won\n");
				end = true;
				break;
			}
			for(j = 0; j < 4; j++)
				if(m[j][j] != 'T' && m[j][j] != 'O')
					break;
			if(j == 4){
				printf("O won\n");
				end = true;
				break;
			}
			for(j = 0; j < 4; j++)
				if(m[j][3-j] != 'T' && m[j][3-j] != 'O')
					break;
			if(j == 4){
				printf("O won\n");
				end = true;
				break;
			}
		}
		if(end)
			continue;
		for(int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if(m[i][j] == '.')
					end = true;
		if(end)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	return 0;
}
