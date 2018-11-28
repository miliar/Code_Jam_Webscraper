#include<cstdio>
#include<cstdlib>
#include<cstring>

#define	LINES	10	// 0~3:row, 4~7:col, 8:l->r, 9:r->l
#define	SIZE	5

int inToNum(char a){
	if(a == '.'){
		return 1;
	}
	else if(a == 'X'){
		return 2;
	}
	else if(a == 'O'){
		return 3;
	}
	else if(a == 'T'){
		return 0;
	}
	else{
		return -1;
	}
}

int main(){

	int T;
	int CaseNum = 1;
	int temp;
	int i, j;
	int ans;
	int lineStatus;			// 0:Draw 1:empty slot, 2:X, 3:O
	int lineElement[LINES][SIZE-1];	// 0:T, 1:empty, 2:X, 3:O
	char inputLine[SIZE];

	scanf("%d",&T);

	while(T > 0){		
		for(i=0;i<LINES;i++){
			memset(lineElement[i],1,SIZE-1);
		}

		// read the first line
		scanf("%s",&inputLine);
		temp = inToNum(inputLine[0]);
		lineElement[0][0] = temp;
		lineElement[4][0] = temp;
		lineElement[8][0] = temp;
		temp = inToNum(inputLine[1]);
		lineElement[0][1] = temp;
		lineElement[5][0] = temp;		
		temp = inToNum(inputLine[2]);
		lineElement[0][2] = temp;
		lineElement[6][0] = temp;
		temp = inToNum(inputLine[3]);
		lineElement[0][3] = temp;
		lineElement[7][0] = temp;
		lineElement[9][0] = temp;
		// read the second line
		scanf("%s",&inputLine);
		temp = inToNum(inputLine[0]);
		lineElement[1][0] = temp;
		lineElement[4][1] = temp;
		temp = inToNum(inputLine[1]);
		lineElement[1][1] = temp;
		lineElement[5][1] = temp;
		lineElement[8][1] = temp;
		temp = inToNum(inputLine[2]);
		lineElement[1][2] = temp;
		lineElement[6][1] = temp;
		lineElement[9][1] = temp;
		temp = inToNum(inputLine[3]);
		lineElement[1][3] = temp;
		lineElement[7][1] = temp;
		// read the thrid line
		scanf("%s",&inputLine);
		temp = inToNum(inputLine[0]);
		lineElement[2][0] = temp;
		lineElement[4][2] = temp;
		temp = inToNum(inputLine[1]);
		lineElement[2][1] = temp;
		lineElement[5][2] = temp;
		lineElement[9][2] = temp;
		temp = inToNum(inputLine[2]);
		lineElement[2][2] = temp;
		lineElement[6][2] = temp;
		lineElement[8][2] = temp;
		temp = inToNum(inputLine[3]);
		lineElement[2][3] = temp;
		lineElement[7][2] = temp;
		// read the fourth line
		scanf("%s",&inputLine);
		temp = inToNum(inputLine[0]);
		lineElement[3][0] = temp;
		lineElement[4][3] = temp;
		lineElement[9][3] = temp;
		temp = inToNum(inputLine[1]);
		lineElement[3][1] = temp;
		lineElement[5][3] = temp;
		temp = inToNum(inputLine[2]);
		lineElement[3][2] = temp;
		lineElement[6][3] = temp;
		temp = inToNum(inputLine[3]);
		lineElement[3][3] = temp;
		lineElement[7][3] = temp;
		lineElement[8][3] = temp;

		ans = 0;	// Draw
		for(i=0;i<LINES;i++){
			j = 0;
			while(lineElement[i][j] == 0){
				j++;
			};
			lineStatus = lineElement[i][j];

			for(;j<SIZE-1;j++){
				if(lineStatus != lineElement[i][j]){
					if(lineElement[i][j] == 1){	// empty slot
						lineStatus = 1;
					}
					else if(lineElement[i][j] == 0){
						// T, nothing changes
					}
					else{
						if(lineStatus != 1){
							lineStatus = 0;
						}
					}
				}
			}
			if(lineStatus > ans){
				ans = lineStatus;
			}
		}

		switch(ans){
			case 0:
				printf("Case #%d: Draw\n",CaseNum);
				break;
			case 1:
				printf("Case #%d: Game has not completed\n",CaseNum);
				break;
			case 2:
				printf("Case #%d: X won\n",CaseNum);
				break;
			case 3:
				printf("Case #%d: O won\n",CaseNum);
				break;
			default:
				break;
		}
		CaseNum++;
		T--;
	};

	return 0;
}
