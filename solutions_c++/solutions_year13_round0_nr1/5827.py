#include<cstdio>
#define XWON 1
#define OWON 2
#define DRAW 3
#define NOTC 4

using namespace std;

int check(char * mat) {
	for(int i = 0;i < 4;i++){
		if(mat[i*4] == mat[i*4+1]&&
				mat[i*4] == mat[i*4+2] &&
				mat[i*4] == mat[i*4+3]){
			if(mat[i*4] == 'X'){
				return XWON;
			}
			else if(mat[i*4] == 'O')
				return OWON;
		}
	}
	for(int i = 0;i < 4;i++){
		if(mat[i] == mat[i+4]&&
				mat[i] == mat[i+8] &&
				mat[i] == mat[i+12]){
			if(mat[i] == 'X'){
				return XWON;
			}
			else if(mat[i] == 'O')
				return OWON;
		}
	}
	if (mat[0] == mat[5]&&
			mat[0] == mat[10]&&
			mat[0] == mat[15]){
		if(mat[0] == 'X'){
			return XWON;
		}
		else if(mat[0] == 'O')
			return OWON;
	}
	else if(mat[3] == mat[6]&&
			mat[3] == mat[9]&&
			mat[3] == mat[12]){
		if(mat[3] == 'X'){
			return XWON;
		}
		else if(mat[3] == 'O')
			return OWON;
	}
	return DRAW;
}


int main() {
	int t;
	int caseNum = 1;
	char xx;
	char mat[16];
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&t);
	for(;caseNum <= t;caseNum++){
		int flag = 0;
		int tflag = 0;
		int rowIndex = 0;
		int colIndex = 0;
		for(int row = 0;row < 4;row++){
			scanf("%s",mat+row*4);
			for(int i = 0;i<4;i++){
				if(mat[row*4+i] == '.'){
					flag = 1;
				}
				else if(mat[row*4+i] == 'T'){
					tflag = 1;
					rowIndex = row;
					colIndex = i;
				}
			}
		}
		if(tflag){
			mat[rowIndex*4+colIndex] = 'X';
			if(check(mat) == XWON){
				printf("Case #%d: X won\n",caseNum);
				continue;
			}
			mat[rowIndex*4+colIndex] = 'O';
			if(check(mat) == OWON){
				printf("Case #%d: O won\n",caseNum);
				continue;
			}
			if(flag){
				printf("Case #%d: Game has not completed\n",caseNum);
				continue;
			}
			else {
				printf("Case #%d: Draw\n",caseNum);
				continue;
			}
		}
		else {
			switch(check(mat)){
				case XWON:
					printf("Case #%d: X won\n",caseNum);
					break;
				case OWON:
					printf("Case #%d: O won\n",caseNum);
					break;
				case DRAW:
					if(flag){
						printf("Case #%d: Game has not completed\n",caseNum);
					}
					else {
						printf("Case #%d: Draw\n",caseNum);
					}
					break;
			}
		}
	}
	return 0;
}
