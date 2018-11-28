#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void){
	int T;
	FILE *fp_in,*fp_out;
	char arr[4][6];
	int i,j,k,n;
	int o_chk,x_chk,d_chk,c_num =0;
	int won=-1;

	fp_in = fopen("A-large.in","r");
	fp_out = fopen("A-large.out","w");

	fscanf(fp_in,"%d\n",&T);
	for(n=0;n<T;n++){
		if(c_num != 0)
			fgetc(fp_in);

		c_num +=1;
		won =-1;
		for(i=0;i<4;i++){
			fgets(arr[i],6,fp_in);
		}

		d_chk =0;


		//가로
		for(i=0;i<4;i++){
			o_chk = 0;
			x_chk = 0;
			
			for(j=0;j<4;j++){
				switch(arr[i][j]){
				case 'T':
					o_chk++;
					x_chk++;
					break;
				case 'X':
					x_chk++;
					break;
				case 'O':
					o_chk++;
					break;
				case '.':
					d_chk ++;

				}
			}
			if(x_chk ==4){
				fprintf(fp_out,"Case #%d: X won\n",c_num);
				won = 0;
				break;
			}
			if(o_chk ==4){
				won = 1;
				fprintf(fp_out,"Case #%d: O won\n",c_num);
				break;;
			}
			
		}
		if(won != -1)
			continue;
		

		//세로


		for(i=0;i<4;i++){
			o_chk = 0;
			x_chk = 0;
			
			for(j=0;j<4;j++){
				switch(arr[j][i]){
				case 'T':
					o_chk++;
					x_chk++;
					break;
				case 'X':
					x_chk++;
					break;
				case 'O':
					o_chk++;
					break;
				case '.':
					d_chk ++;

				}
			}
			if(x_chk ==4){
				fprintf(fp_out,"Case #%d: X won\n",c_num);
				won =0;
				break;
			}
			if(o_chk ==4){
				fprintf(fp_out,"Case #%d: O won\n",c_num);
				won = 1;
				break;
			}
		}
		if(won != -1)
			continue;
		

		o_chk=0;
		x_chk=0;
			

		for(i=0;i<4;i++){

			switch(arr[i][i]){
			case 'T':
				o_chk++;
				x_chk++;
				break;
			case 'X':
				x_chk++;
				break;
			case 'O':
				o_chk++;
				break;
			case '.':
				d_chk ++;
			}
		}

		if(x_chk ==4){
			fprintf(fp_out,"Case #%d: X won\n",c_num);
			continue;
		}
		if(o_chk ==4){
			fprintf(fp_out,"Case #%d: O won\n",c_num);
			continue;
		}



		o_chk=0;
		x_chk=0;
			

		for(i=0;i<4;i++){

			switch(arr[i][3-i]){
			case 'T':
				o_chk++;
				x_chk++;
				break;
			case 'X':
				x_chk++;
				break;
			case 'O':
				o_chk++;
				break;
			case '.':
				d_chk ++;
			}
			
		}

		if(x_chk ==4){
			fprintf(fp_out,"Case #%d: X won\n",c_num);
			continue;
		}
		if(o_chk ==4){
			fprintf(fp_out,"Case #%d: O won\n",c_num);
			continue;
		}
		
		


		//무승부
		
		if(d_chk == 0){
			fprintf(fp_out,"Case #%d: Draw\n",c_num);
		}
		else if(d_chk != 0){
			fprintf(fp_out,"Case #%d: Game has not completed\n",c_num);
		}
	}

	return 0;
}