#include <cstdio>

char map[4][5];
bool win(char c){
	for (int i=0;i<4;i++){
		int cnt=0;
		for (int j=0;j<4;j++)
			if (map[i][j]==c)
				cnt++;
		if (cnt==4)
			return true;
		cnt=0;
		for (int j=0;j<4;j++)
			if (map[j][i]==c)
				cnt++;
		if (cnt==4)
			return true;		
	}
	int cnt=0;
	for (int i=0;i<4;i++)
		if (map[i][i]==c)
			cnt++;
	if (cnt==4)
		return true;
	cnt=0;
	for (int i=0;i<4;i++)
		if (map[i][3-i]==c)
			cnt++;
	if (cnt==4)
		return true;
	return false;
}
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int t=1;t<=cases;t++){
		printf("Case #%d: ",t);
		int px=-1,py,dot=0;
		for (int i=0;i<4;i++){
			scanf("%s",map[i]);
			for (int j=0;j<4;j++){
				if (map[i][j]=='.')
					dot++;
				if (map[i][j]=='T')
					px=i,py=j;
			}
		}
		if (px!=-1){
			map[px][py]='O';
			if (win('O')){
				puts("O won");
				continue;
			}
			map[px][py]='X';
			if (win('X')){
				puts("X won");
				continue;
			}
		}
		else{
			if (win('O')){
				puts("O won");
				continue;
			}
			if (win('X')){
				puts("X won");
				continue;
			}
		}
		if (dot)
			puts("Game has not completed");
		else
			puts("Draw");
	}
}
