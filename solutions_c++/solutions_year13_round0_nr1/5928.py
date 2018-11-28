#include <stdio.h>

#include <stdlib.h>
#include <string.h>
FILE *fi,*fo;
char board[5][5];

int main(){
	fi=fopen("A-small-attempt2.in","r");
	int i,j;
	int T;
	fo=fopen("A-small-attempt2.out","w");
	int num=0,t=0;
	int k;
	char tmpc;
	fscanf(fi,"%d",&num);
	k=num;
	while(num--){
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				while(1){
					fscanf(fi,"%c",&tmpc);
					if(tmpc=='T'||tmpc=='X'||tmpc=='O'||tmpc=='.'){
						board[i][j]=tmpc;
						break;
					}
				}
			}}
		t=0;


		for(i=0;i<4&&t==0;i++){
			T=0;
			if(board[i][0]=='T')
				T++;

			if (board[i][T]=='O'){
				for(j=1;(j)<4&&t==0;j++){
					if(board[i][j]=='O'||board[i][j]=='T'){
						if((j)==3){
							fprintf(fo,"Case #%d: O won\n",k-num);
							i=5;
							t=2;
						}
						continue;
					}
					break;
				}
			}
			else if(board[i][0]=='X'){
				for(j=1;(j)<4&&t==0;j++){
					if(board[i][j]=='X'||board[i][j]=='T'){
						if((j)==3){
							fprintf(fo,"Case #%d: X won\n",k-num);
							i=5;
							t=1;
						}
						continue;
					}
					break;
				}
			}
		}

		for(j=0;j<4&&t==0;j++){
			T=0;
			if(board[0][j]=='T')
				T++;

			if (board[T][j]=='O'){
				for(i=1;(i)<4&&t==0;i++){
					if(board[i][j]=='O'||board[i][j]=='T'){
						if((i)==3){
							fprintf(fo,"Case #%d: O won\n",k-num);

							t=2;
						}
						continue;
					}
					break;
				}
			}
			else if(board[T][j]=='X'){
				for(i=1;(i)<4&&t==0;i++){
					if(board[i][j]=='X'||board[i][j]=='T'){
						if((i)==3){
							fprintf(fo,"Case #%d: X won\n",k-num);

							t=1;
						}
						continue;
					}
					break;
				}
			}
		}
		if(t!=0)
			continue;
		T=0;
		if(board[0][0]=='T')
			T=1;
		if(board[T][T]=='O'){
			for(i=T;i<4;i++){
				if(board[i][i]=='O'||board[i][i]=='T'){
					if(i==3){
						t=2;
						fprintf(fo,"Case #%d: O won\n",k-num);
					}
					continue;
				}
				else 
					break;
			}
		}
		if(board[T][T]=='X'){
			for(i=T;i<4;i++){
				if(board[i][i]=='X'||board[i][i]=='T'){
					if(i==3){
						t=1;
						fprintf(fo,"Case #%d: X won\n",k-num);
					}
					continue;
				}
				else 
					break;
			}
		}
		if(t!=0)
			continue;
		T=0;
		if(board[3][0]=='T')
			T=1;
		if(board[3-T][T]=='O'){
			for(i=T;i<4;i++){
				if(board[3-i][i]=='O'||board[3-i][i]=='T'){
					if(i==3){
						t=2;
						fprintf(fo,"Case #%d: O won\n",k-num);
					}
					continue;
				}
				else 
					break;
			}
		}
		if(board[3-T][T]=='X'){
			for(i=T;i<4;i++){
				if(board[3-i][i]=='X'||board[3-i][i]=='T'){
					if(i==3){
						t=1;
						fprintf(fo,"Case #%d: X won\n",k-num);
					}
					continue;
				}
				else 
					break;
			}
		}
		for(i=0;t==0&&i<4;i++){

			for(j=0;t==0&&j<4;j++){
				if(board[i][j]=='.'){
					fprintf(fo,"Case #%d: Game has not completed\n",k-num);
					t=4;
				}
			}
		}


		if(t==0){
			fprintf(fo,"Case #%d: Draw\n",k-num);
			t=5;
		}
	}





	fclose(fi);
	fclose(fo);
	return 0;

}


