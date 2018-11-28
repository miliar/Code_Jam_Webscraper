#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	int t;
	scanf("%d" , &t);
	int k;
	for (k = 0;k < t;k++) {
		char a[11][5];
		int i;
		scanf("%s%s%s%s", a[0], a[1], a[2], a[3]);
		for(i = 0;i < 4;i++){
			a[4][i] = a[i][0];
			a[5][i] = a[i][1];
			a[6][i] = a[i][2];
			a[7][i] = a[i][3];
			a[8][i] = a[i][i];
			a[9][i] = a[i][3-i];
		}
//		for(i = 0;i < 10;i++){
//		printf("s%d = %s\n",i,a[i]);
//		}
		for(i = 0;i < 10;i++) {
			if((a[i][0] == 'X' ||a[i][0] =='T')&&(a[i][1] == 'X' ||a[i][1] =='T') && (a[i][2] == 'X' ||a[i][2] =='T') && (a[i][3] == 'X' ||a[i][3] =='T')){
				printf("Case #%d: X won\n", k+1);
				goto head;
			}
			else if((a[i][0]=='O'||a[i][0]=='T')&&(a[i][1]=='O' ||a[i][1] =='T') && (a[i][2] == 'O' ||a[i][2] =='T') && (a[i][3] == 'O' ||a[i][3] =='T')) {
				printf("Case #%d: O won\n",k+1);
				goto head;
			}
		}
		int x;
		for(i = 0;i < 4;i++) {
			if(a[i][0] == '.' || a[i][1] == '.' || a[i][2] == '.' || a[i][3] == '.') {
				printf("Case #%d: Game has not completed\n",k+1);
				goto head;
			}
		}
		printf("Case #%d: Draw\n",k+1);
		char e;
	//	scanf("%c",&e);
head:;
     	}
	return 0;
}
