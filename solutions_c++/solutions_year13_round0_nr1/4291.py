#include <stdio.h>

using namespace std;

char tmp[10];
int mat[5][5],cnt;

int solv() {
	//->
	for (int i = 0;i < 4;i++) {
		int count[] = {0,0,0};
		for (int j = 0;j < 4;j++) {
			if (mat[i][j] < 3)
				count[mat[i][j]]++;
			else
				count[1]++,count[2]++;
		}
		if (count[1] == 4) 
			return 1;
		else if (count[2] == 4)
			return 2;
	}
	// |
	//\ /
	for (int i = 0;i < 4;i++) {
		int count[] = {0,0,0};
		for (int j = 0;j < 4;j++) {
			if (mat[j][i] < 3)
				count[mat[j][i]]++;
			else
				count[1]++,count[2]++;
		}
		if (count[1] == 4) 
			return 1;
		else if (count[2] == 4)
			return 2;
	}
	//
	{
		int count[] = {0,0,0};
		for (int i = 0;i < 4;i++) {
			if (mat[i][i] < 3) 
				count[mat[i][i]]++;
			else
				count[1]++,count[2]++;
		}
		if (count[1] == 4)
			return 1;
		else if (count[2] == 4)
			return 2;
	}
	//
	{
		int count[] = {0,0,0};
		for (int i = 0;i < 4;i++) {
			if (mat[i][3-i] < 3) 
				count[mat[i][3-i]]++;
			else
				count[1]++,count[2]++;
		}
		if (count[1] == 4)
			return 1;
		else if (count[2] == 4)
			return 2;
	}
	if (cnt == 0) 
		return 3;
	return 4;

}


int main() {
	int T;scanf("%d",&T);
	for (int cas = 1;cas <= T;cas++) {
		cnt = 0;
		for (int i = 0;i < 4;i++) {
			scanf("%s",tmp);
			for (int j = 0;j < 4;j++) {
				if (tmp[j] == 'X') 
					mat[i][j] = 1;
				else if (tmp[j] == 'O')
					mat[i][j] = 2;
				else if (tmp[j] == 'T')
					mat[i][j] = 3;
				else
					mat[i][j] = 0,cnt++;
			}
		}
		int ans = solv();
		printf("Case #%d: ",cas);
		if (ans == 1) 
			printf("X won\n");
		else if (ans == 2) 
			printf("O won\n");
		else if (ans == 3)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}
