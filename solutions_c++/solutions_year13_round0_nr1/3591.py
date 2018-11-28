#include<cstdio>
#include<iostream>
int main()
{
 //
  //  freopen("a.in", "r", stdin);
 //   freopen("a.out", "w", stdout);
    int round;
    scanf("%d\t", &round);
    char ch[5][5];
    int sig[5][5];
    int check[10];
    int state;
	for(int i = 1;i <= round;i++){
		for(int j = 0;j < 4;j++){
			scanf("%c%c%c%c\n", &ch[0][j], &ch[1][j], &ch[2][j], &ch[3][j]);
	    	for(int ii = 0;ii < 4;ii++){
				if(ch[ii][j] == 'O')sig[ii][j] = 10;
				if(ch[ii][j] == '.')sig[ii][j] = 1;
				if(ch[ii][j] == 'X')sig[ii][j] = 0;
				if(ch[ii][j] == 'T')sig[ii][j] = 5;
			}
		}
		scanf("\n");
		memset(check, 0, sizeof(check));
		for(int jj = 0; jj < 4;jj++){
			for(int kk = 0; kk < 4;kk++){
				check[jj] += sig[jj][kk];
				check[jj+4] += sig[kk][jj];
			}
			check[8] += sig[jj][jj];
			check[9] += sig[jj][3-jj];
		}
		bool iswin = false;
		bool isdraw = true;
		for(int jj = 0;jj < 10; jj++){
			if(check[jj] == 35 || check[jj] == 40){
				printf("Case #%d: O won\n", i);
				iswin = true;
				break;
			}
			if(check[jj] == 0 || check[jj] == 5){
				iswin = true;
				printf("Case #%d: X won\n", i);
				break;
			}
			if(check[jj] % 5 != 0)
				isdraw = false;
		}
		if(!iswin){
			if(isdraw){
				printf("Case #%d: Draw\n", i);
			}
			else 
				printf("Case #%d: Game has not completed\n", i);		
		}
	}
	return 0;   
}
