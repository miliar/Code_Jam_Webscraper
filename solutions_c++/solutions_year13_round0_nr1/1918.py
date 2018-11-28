#include <stdio.h>
#include <stdlib.h>
char arr[4][4];
int getres(){
	int X,O;
	for(int i=0;i<4;i++){
		X=O=0;
		for(int j=0;j<4;j++){
			if(arr[i][j]=='X')
				X++;
			else if(arr[i][j]=='O')
				O++;
			else if(arr[i][j]=='T')
				X++,O++;
		}
		if(X==4)
			return 1;
		if(O==4)
			return 0;
	}
	for(int j=0;j<4;j++){
		X=O=0;
		for(int i=0;i<4;i++){
			if(arr[i][j]=='X')
				X++;
			else if(arr[i][j]=='O')
				O++;
			else if(arr[i][j]=='T')
				X++,O++;
		}
		if(X==4)
			return 1;
		if(O==4)
			return 0;
	}
	X=O=0;
	for(int i=0;i<4;i++){
			if(arr[i][i]=='X')
				X++;
			else if(arr[i][i]=='O')
				O++;
			else if(arr[i][i]=='T')
				X++,O++;
	}
	if(X==4)
		return 1;
	if(O==4)
		return 0;
	X=O=0;
	for(int i=0;i<4;i++){
			if(arr[i][3-i]=='X')
				X++;
			else if(arr[i][3-i]=='O')
				O++;
			else if(arr[i][3-i]=='T')
				X++,O++;
	}
	if(X==4)
		return 1;
	if(O==4)
		return 0;

	
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(arr[i][j]=='.')
				return -1;
		}
	}

	return -2;
}
int main(){
	int T;
	char tmp[10];

	freopen("in.txt","r",stdin);

	scanf("%d",&T);
	for(int C=1;C<=T;C++){
		//INPUT
		for(int i=0;i<4;i++){
			scanf("%s",tmp);
			for(int j=0;j<4;j++){
				arr[i][j]=tmp[j];
			}
		}
		printf("Case #%d: ",C);
		switch(getres()){
		case -1:
			printf("Game has not completed\n");
			break;
		case 0:
			printf("O won\n");
			break;
		case 1:
			printf("X won\n");
			break;
		case -2:
			printf("Draw\n");
			break;
		}
	}
	system("pause");
}