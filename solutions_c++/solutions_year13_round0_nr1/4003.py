#include <stdio.h>

int main(){
	FILE *input;
	FILE *output;
	input=fopen("A-large.in", "r");
	output=fopen("out.txt", "w");
	int cases,sum,state=0;
	char row1[5];
	char row2[5];
	char row3[5];
	char row4[5];
	
	char rw1[5];
	char rw2[5];
	char rw3[5];
	char rw4[5];
	char diag1[5];
	char diag2[5];
	char ex[5];
	fscanf(input, "%d", &cases);
	for(int c=0;c<cases;c++){
		sum=0;
		state=0;
		fscanf(input, "%s", row1);
		fscanf(input, "%s", row2);
		fscanf(input, "%s", row3);
		fscanf(input, "%s", row4);
		/*fprintf(output,"%s\n", row1);
		fprintf(output,"%s\n", row2);
		fprintf(output,"%s\n", row3);
		fprintf(output,"%s\n", row4);
		fprintf(output,"\n");*/
		rw1[0]=row1[0];rw1[1]=row2[0];rw1[2]=row3[0];rw1[3]=row4[0];rw2[0]=row1[1];rw2[1]=row2[1];rw2[2]=row3[1];rw2[3]=row4[1];
		rw3[0]=row1[2];rw3[1]=row2[2];rw3[2]=row3[2];rw3[3]=row4[2];rw4[0]=row1[3];rw4[1]=row2[3];rw4[2]=row3[3];rw4[3]=row4[3];
		diag1[0]=row1[0];diag1[1]=row2[1];diag1[2]=row3[2];diag1[3]=row4[3];
		diag2[0]=row1[3];diag2[1]=row2[2];diag2[2]=row3[1];diag2[3]=row4[0];
		ex[0]='T';
		ex[1]='X';
		ex[2]='X';
		ex[3]='X';
		if((row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3]) || (row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3])  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=1;
		}
		ex[0]='X';
		ex[1]='T';
		ex[2]='X';
		ex[3]='X';
		if(row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3] || row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3]  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=1;
		}
		ex[0]='X';
		ex[1]='X';
		ex[2]='T';
		ex[3]='X';
		if(row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3] || row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3]  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=1;
		}
		ex[0]='X';
		ex[1]='X';
		ex[2]='X';
		ex[3]='T';
		if(row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3] || row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3]  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=1;
		}
		ex[0]='X';
		ex[1]='X';
		ex[2]='X';
		ex[3]='X';
		if(row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3] || row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3]  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=1;
		}
		ex[0]='T';
		ex[1]='O';
		ex[2]='O';
		ex[3]='O';
		if(row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3] || row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3]  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=2;
		}
		ex[0]='O';
		ex[1]='T';
		ex[2]='O';
		ex[3]='O';
		if(row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3] || row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3]  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=2;
		}
		ex[0]='O';
		ex[1]='O';
		ex[2]='T';
		ex[3]='O';
		if(row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3] || row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3]  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=2;
		}
		ex[0]='O';
		ex[1]='O';
		ex[2]='O';
		ex[3]='T';
		if(row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3] || row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3]  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=2;
		}
		ex[0]='O';
		ex[1]='O';
		ex[2]='O';
		ex[3]='O';
		if(row1[0]==ex[0] && row1[1]==ex[1] && row1[2]==ex[2] && row1[3]==ex[3] || row2[0]==ex[0] && row2[1]==ex[1] && row2[2]==ex[2] && row2[3]==ex[3]  || row3[0]==ex[0] && row3[1]==ex[1] && row3[2]==ex[2] && row3[3]==ex[3]  || row4[0]==ex[0] && row4[1]==ex[1] && row4[2]==ex[2] && row4[3]==ex[3]  || rw1[0]==ex[0] && rw1[1]==ex[1] && rw1[2]==ex[2] && rw1[3]==ex[3]  || rw2[0]==ex[0] && rw2[1]==ex[1] && rw2[2]==ex[2] && rw2[3]==ex[3]  || rw3[0]==ex[0] && rw3[1]==ex[1] && rw3[2]==ex[2] && rw3[3]==ex[3]  || rw4[0]==ex[0] && rw4[1]==ex[1] && rw4[2]==ex[2] && rw4[3]==ex[3]  || diag1[0]==ex[0] && diag1[1]==ex[1] && diag1[2]==ex[2] && diag1[3]==ex[3]  || diag2[0]==ex[0] && diag2[1]==ex[1] && diag2[2]==ex[2] && diag2[3]==ex[3] ){
			state=2;
		}

		if(state==1){
			fprintf(output, "Case #%d: X won\n", c+1);
		}else if(state==2){
			fprintf(output, "Case #%d: O won\n",c+1);
		}
		if (state==0){
			for(int j=0;j<4;j++){
				if(row1[j]=='.' || row2[j]=='.' || row3[j]=='.' || row4[j]=='.'){
					sum++;
				}
			}
			if (sum!=0){
				fprintf(output, "Case #%d: Game has not completed\n", c+1);
			}
			else{
				fprintf(output, "Case #%d: Draw\n", c+1);
			}
		}
		

	}
	return 0;
}