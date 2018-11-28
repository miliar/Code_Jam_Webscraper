#include<stdio.h>

int T;

FILE *in = fopen("test.in","r");
FILE *out= fopen("tt.out","w");

int main(){

	int cnt_o_horizon[10], cnt_x_horizon[10], cnt_o_vertical[10], cnt_x_vertical[10];
	int cnt_o_same, cnt_x_same, cnt_o_reverse, cnt_x_reverse;
	int d[10][10];
	char temp[6];

	fscanf(in, "%d", &T);
	for(int k=1;k<=T;k++){
		for(int i=1;i<=4;i++){
			fscanf(in, "%s", &temp[1]);
			for(int j=1;j<=4;j++){
				if(temp[j] == 'X') d[i][j] = 1;
				else if(temp[j] == 'O') d[i][j] = 2;
				else if(temp[j] == 'T') d[i][j] = 3;
				else d[i][j] = 0;

			}

			cnt_o_horizon[i] = cnt_o_vertical[i] = 0;
			cnt_x_horizon[i] = cnt_x_vertical[i] = 0;
		}
		cnt_x_same = cnt_o_same = 0;
		cnt_x_reverse = cnt_o_reverse = 0;
		bool check = false;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				if(d[i][j] == 1 || d[i][j] == 3){
					cnt_x_horizon[i] ++;
					cnt_x_vertical[j] ++;
					if(i==j) cnt_x_same++;
					if(i+j == 5) cnt_x_reverse++;

				}
				if(d[i][j] == 2 || d[i][j] == 3){
					cnt_o_horizon[i] ++;
					cnt_o_vertical[j] ++;
					if(i==j)cnt_o_same++;
					if(i+j == 5) cnt_o_reverse++;
				}
				if(d[i][j] == 0 ) check = true;
			}
		}
		bool o_win;
		bool x_win;

		o_win = x_win = false;
		for(int i=1;i<=4;i++){
			if(cnt_o_horizon[i] == 4 || cnt_o_same == 4 || cnt_o_vertical[i] == 4 || cnt_o_reverse == 4) o_win=true;
			if(cnt_x_horizon[i] == 4 || cnt_x_same == 4 || cnt_x_vertical[i] == 4 || cnt_x_reverse == 4) x_win=true;

		}
		if(x_win == true ) fprintf(out, "Case #%d: X won\n", k);
		else if(o_win == true) fprintf(out, "Case #%d: O won\n", k); 
		else if(check == false) fprintf(out, "Case #%d: Draw\n", k);
		else fprintf(out, "Case #%d: Game has not completed\n", k);
	}
}