#include <iostream>

using namespace std;

int n;
char b[4][4];

bool over;

bool com(char a, char b){
	if((a == '.')||(b == '.'))
		over = 0;
	if(((a == b)||(a == 'T')||(b == 'T'))&&(a != '.')&&(b != '.'))
		return 1;
	return 0;
}

int w;

int main(){
	FILE * inp;
	FILE * outp;
	inp = fopen("input.in", "r");
	outp = fopen("output.txt", "w");
	fscanf(inp, "%d\n", &n);
	for(int i = 0; i < n; i++){
		//cout<<i;
		for(int j = 0; j < 3; j++){
			fscanf(inp,"%c%c%c%c\n", &b[j][0],&b[j][1],&b[j][2],&b[j][3]);
		}
		fscanf(inp,"%c%c%c%c\n \n", &b[3][0],&b[3][1],&b[3][2],&b[3][3]);
		w = 0;
		over = 1;
		for(int j = 0; j < 4; j++){
			if((com(b[j][0],b[j][1])&&com(b[j][1],b[j][2])&&com(b[j][2],b[j][3]))){
				if(b[j][0] == 'T'){
					w = (b[j][1] == 'X')?1:2;
					break;
				}
				else{
					w = (b[j][0] == 'X')?1:2;
					break;
				}
			}
		}
		if(w > 0){
			if(w == 1)
				fprintf(outp,"Case #%d: X won\n",i+1);
			if(w == 2)
				fprintf(outp,"Case #%d: O won\n",i+1);
			continue;
		}
		for(int j = 0; j < 4; j++){
			if((com(b[0][j],b[1][j])&&com(b[1][j],b[2][j])&&com(b[2][j],b[3][j]))){
				if(b[0][j] == 'T'){
					w = (b[1][j] == 'X')?1:2;
					break;
				}
				else{
					w = (b[0][j] == 'X')?1:2;
					break;
				}
			}
		}
		if(w > 0){
			if(w == 1)
				fprintf(outp,"Case #%d: X won\n",i+1);
			if(w == 2)
				fprintf(outp,"Case #%d: O won\n",i+1);
			continue;
		}
		if((com(b[0][0],b[1][1])&&com(b[1][1],b[2][2])&&com(b[2][2],b[3][3]))){
			if(b[0][0] == 'T'){
					w = (b[1][1] == 'X')?1:2;
				}
				else{
					w = (b[0][0] == 'X')?1:2;
				}
		}
		if((com(b[0][3],b[1][2])&&com(b[1][2],b[2][1])&&com(b[2][1],b[3][0]))){
			if(b[0][3] == 'T'){
					w = (b[1][2] == 'X')?1:2;
					
				}
				else{
					w = (b[0][3] == 'X')?1:2;
					
				}
		}
		if(w > 0){
			if(w == 1)
				fprintf(outp,"Case #%d: X won\n",i+1);
			if(w == 2)
				fprintf(outp,"Case #%d: O won\n",i+1);
			continue;
		}
		if(over == 1)
			fprintf(outp,"Case #%d: Draw\n",i+1);
		else fprintf(outp,"Case #%d: Game has not completed\n",i+1);
	}
	fclose(inp);
	fclose(outp);
	//while(1){}
	return 0;
}