#include<stdio.h>
#include<string.h>
int r, c;
char map[52][52];
int change(int x, int y)
{
	if(x+1 >= r || map[x+1][y] != '#')
		return 0;
	if(y+1 >= c || map[x][y+1] != '#')
		return 0;
	if(x+1 >= r || y+1 >= c || map[x+1][y+1] != '#')
		return 0;
	map[x][y] = '/';
	map[x+1][y] = '\\';
	map[x][y+1] = '\\';
	map[x+1][y+1] = '/';
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tcase;
	scanf("%d", &tcase);
	for(int ts = 1; ts <= tcase; ts++){
		scanf("%d%d",&r,&c);
		for(int i = 0; i < r; i++){
			scanf("%s",map[i]);
		}
		int flag = 1;
		for(int i = 0; i < r && flag; i++){
			for(int j = 0; j < c && flag; j++){
				if(map[i][j] == '#'){
					if(!change(i,j))
						flag = 0;
				}
			}
		}
		
		printf("Case #%d:\n", ts);
		if(!flag)
			printf("Impossible\n");
		else{
			for(int i = 0; i < r; i++){
				for(int j = 0; j < c; j++)
					printf("%c",map[i][j]);
				printf("\n");
			}
		}
	}	
	return 0;
}
