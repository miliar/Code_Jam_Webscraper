#include <cstdio>

char a[100][100];
int r, c, t, left;

int main(){
	scanf("%d", &t);
	for (int T = 1; T <= t; T++){
		scanf("%d%d", &r, &c);
		left = 0;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				scanf(" %c", &a[i][j]), left += a[i][j] == '#';
		
		for (int i = 0; i < r - 1; i++)
			for (int j = 0; j < c - 1; j++)
				if (a[i][j] == '#' && a[i + 1][j] == '#' && a[i][j + 1] == '#' && a[i + 1][j + 1] == '#'){
					a[i][j] = '/';
					a[i + 1][j] = '\\';
					a[i][j + 1] = '\\';
					a[i + 1][j + 1] = '/';
					left -= 4;
				}
		
		if (left == 0){
			printf("Case #%d:\n", T);
			for (int i = 0; i < r; i++){
				for (int j = 0; j < c; j++)
					printf("%c", a[i][j]);
				printf("\n");
			}
		} else {
			printf("Case #%d:\n", T);
			printf("Impossible\n");
		}
	}
}
