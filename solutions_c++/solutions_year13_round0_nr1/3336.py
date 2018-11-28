#include<iostream>
using namespace std;

char str[10][10];
int ok(char ch){
	int sign = 0;
	for(int j,i=0; i<4; i++){
		for(j=0; j<4; j++){
			if(str[i][j] == ch || str[i][j] == 'T')
				continue;
			break;
		}
		if( j == 4)
			return 1;
	}

	for(int i,j=0; j<4; j++){
		for(i=0; i<4; i++){
			if(str[i][j] == ch || str[i][j] == 'T')
				continue;
			break;
		}
		if( i == 4)
			return 1;
	}
	int i;
	for(i=0; i<4; i++){
		if(str[i][i] == ch || str[i][i] == 'T')
			continue;
		break;
	}
	if(i == 4)
		return 1;
	for(i=0; i<4; i++){
		if(str[i][3-i] == ch || str[i][3-i] == 'T')
			continue;
		break;
	}
	if( i== 4)
		return 1;
	return 0;
}
int hav(){
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(str[i][j] == '.')
				return 1;
	return 0;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("AC.out","w", stdout);
	int cas;
	int ca=1;
	scanf("%d", &cas);
	
	while(cas--){
		for(int i=0; i<4; i++)
			scanf("%s", str[i]);
		if(ok('X'))
			printf("Case #%d: X won\n",ca++);
		else if(ok('O'))
			printf("Case #%d: O won\n",ca++);
		else if(hav())
			printf("Case #%d: Game has not completed\n",ca++);
		else
			printf("Case #%d: Draw\n",ca++);
	}
	return 0;
}
