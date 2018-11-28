#include <stdio.h>
#include <string.h>

char map[5][5];

int check(char tag){
	int count4 = 0,c7 = 0;
	for(int i = 0; i < 4; i ++){
		int count1 = 0,count2 = 0,count3=0,c4 = 0,c5= 0,c6= 0;
		for(int j = 0; j < 4; j ++){
			if(map[i][j] == tag) count1 ++;
			if(map[i][j] == 'T' && !c4) c4 ++;
			if(map[j][i] == tag) count2 ++;
			if(map[j][i] == 'T' && !c5) c5++;
			if(map[j][j] == tag) count3 ++;
			if(map[j][j] == 'T' && !c6) c6++;
			if(i + j == 3){
				if(map[j][i] == tag) count4 ++;
				if(map[j][i] == 'T' && !c7) c7 ++; 
			}
		}
		if(count1 + c4 == 4 || count2 + c5 == 4 || count3 + c6 == 4 || count4 + c7 == 4) return 1;
	}
	return 0;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);

	for(int cas = 1; cas <= T; cas ++){
		gets(map[0]);
		for(int i = 0; i < 4; i ++){
			scanf("%s",map[i]);
		}
		printf("Case #%d: ",cas);
		int a,b;
		a = check('X');
		b = check('O');
		if(a && b) {printf("Draw\n");continue;}
		if(a) {printf("X won\n");continue;}
		if(b) {printf("O won\n");continue;}
		int cnt = 0;
		for(int i = 0; i < 4; i ++){
			for(int j = 0; j < 4; j ++){
				if(map[i][j] == '.') cnt ++;
			}
		}
		if(cnt){
			printf("Game has not completed\n");
		}else{
			printf("Draw\n");
		}
	}

	return 0;
}