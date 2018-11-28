#include<cstdlib>
#include<iostream>

using namespace std;

void debug_read(int map[4][4],char map_2[4][4]){
	for(int j=0; j<4; j++){
		for(int i=0; i<4; i++){
			cout<<map[j][i]<<",";		
		}
		cout<<endl;
	}	
}

void compute(int map[4][4], int arr[])
{
	int arridx = 0;
	int sum_row, sum_col;
	for(int idx=0; idx<4; idx++){
		sum_row = 0;
		sum_col = 0;
		for(int idx_row=0; idx_row<4; idx_row++){
				sum_row += map[idx][idx_row];
		}
		arr[arridx] = sum_row;
		arridx++;
		for(int idx_col=0; idx_col<4; idx_col++){
				sum_col += map[idx_col][idx];	
		}	
		arr[arridx] = sum_col;
		arridx++;
	}
	arr[8]=map[0][0]+map[1][1]+map[2][2]+map[3][3];
	arr[9]=map[0][3]+map[1][2]+map[2][1]+map[3][0];
}

void convert(char map[4][4], int convert_map[4][4]){
	for(int j=0; j<4; j++){
		for(int i=0; i<4; i++)
			switch(map[j][i]){
				case 'X':
					convert_map[j][i]=-1;
					break;
				case 'O':
					convert_map[j][i]=1;
					break;
				case 'T':
					convert_map[j][i]= 13;
					break;
				default:
					convert_map[j][i]=0;
			}	
	}
}

int main()
{
	FILE *fp;
	FILE *wfp;
	fp = fopen("A-large.in","r");
	wfp = fopen("A-large.out","w");
	int case_number;
	int output_case=1;
	char map[4][4];
	int convert_map[4][4];		
	fscanf(fp,"%d\n",&case_number);
	while(case_number>0){
		int convert_arr[10];
		int opflag = -1;
		bool isdraw = true;
		fprintf(wfp,"Case #%d: ",output_case);
		for(int rd = 0; rd<4; rd++){
			int scan = 4;
			fscanf(fp,"%c %c %c %c\n",&map[rd][0],&map[rd][1],&map[rd][2],&map[rd][3]);
		}
		convert(map, convert_map);
		for(int j=0; j<4; j++){
			for(int i=0; i<4; i++)
				if(map[j][i]=='.'){
					isdraw = false ;
					break;
				}
		}	
		compute(convert_map,convert_arr);
		for(int i=0;i<10;i++)
		{
			if(convert_arr[i]==4 || convert_arr[i]==16){
				opflag=1;
				break;
			}
			else if(convert_arr[i]==-4 || convert_arr[i]==10){
				opflag=0;
				break;
			}
			else
				opflag=-1;
		}	
		if(opflag==0){
			fprintf(wfp,"X won\n");
		}
		else if(opflag==1){
			fprintf(wfp,"O won\n");
		}
		else if(isdraw){
			fprintf(wfp,"Draw\n");
		}
		else{
			fprintf(wfp,"Game has not completed\n");
		}
		output_case++;
		case_number--;
	}
	fclose(fp);
	fclose(wfp);
	//cout<<case_number; //debug
	return 0;
}
