#include"stdio.h"
bool check(char inp[4][5], char c){
	bool b1,b2,b3,b4;
	for(int i=0;i<4;i++){
		b1 = 1, b2 = 1, b3 = 1, b4 = 1;
		for(int j=0;j<4;j++){
			b1&=(inp[i][j]==c || inp[i][j]=='T');
			b2&=(inp[j][i]==c || inp[j][i]=='T');
			b3&=(inp[j][j]==c || inp[j][j]=='T');
			b4&=(inp[j][3-j]==c || inp[j][3-j]=='T');
		}
		if (b1 || b2 || b3 || b4) return 1;
	}
	return 0;
}
int main(){
	int T;
	scanf("%d\n", &T);
	for(int t=1;t<=T;t++){
		char inp [4][5];
		bool dot = 0;
		for(int i=0;i<4;i++){
			scanf("%s\n",inp[i]);
//			printf("%s\n",inp[i]);
			for(int j=0;j<4;j++)dot |= (inp[i][j]=='.');
		}
		scanf("\n");
		printf("Case #%d: ",t);
		if(check(inp,'X')){
			printf("X won\n");
			continue;
		}
		if(check(inp,'O')){
			printf("O won\n");
			continue;
		}
		printf("%s\n",dot?"Game has not completed":"Draw");
	}
}
