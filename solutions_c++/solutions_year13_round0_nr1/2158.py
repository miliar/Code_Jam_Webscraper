//============================================================================
// Name        : 130414-tictactoe.cpp
// Author      : myscloud
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <string.h>

char tab[5][5];
int o,x,t,status;

void countt(int i,int j){
	if(tab[i][j]=='O') o++;
	else if(tab[i][j]=='X') x++;
	else if(tab[i][j]=='T') t++;

}

void chk(void){
	if(x==4 || (x==3 && t==1)) status = 1; //x won
	else if(o==4 || (o==3 && t==1)) status = 2; // o won
}

int main(){

	int n,i,j,k,count,dot;

	scanf("%d",&n);

	for(k=1;k<=n;k++){

		status = count = dot = 0;

		for(i=0;i<4;i++) scanf("%s",tab[i]);

		//check horizon
		for(i=0;i<4;i++){
			o = x = t = 0;
			for(j=0;j<4;j++) countt(i,j);
			chk();
		}

		//check vertical
		for(j=0;j<4;j++){
			o = x = t = 0;
			for(i=0;i<4;i++) countt(i,j);
			chk();
		}

		//check diagonal
		o = x = t = 0;
		for(i=0;i<4;i++){
			countt(i,i);
			chk();
		}

		o = x = t = 0;
		for(i=0;i<4;i++){
			countt(i,3-i);
			chk();
		}

		//chk for draw or not end
		if(status==0){
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					if(tab[i][j]=='.') dot++;

			if(dot==0) status = 3; // draw
			else status = 4; //not complete
		}

		if(status==1) printf("Case #%d: X won\n",k);
		else if(status==2) printf("Case #%d: O won\n",k);
		else if(status==3) printf("Case #%d: Draw\n",k);
		else printf("Case #%d: Game has not completed\n",k);

	}

	return 0;
}
