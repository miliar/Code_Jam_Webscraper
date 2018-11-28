#include <stdio.h>

char m[10][10];
FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

bool check(char c){
	int i;
	for(i=0;i<4;i++){
		if(((m[i][0] == c) || (m[i][0] == 'T')) && ((m[i][1] == c) || (m[i][1] == 'T')) && ((m[i][2] == c) || (m[i][2] == 'T')) && ((m[i][3] == c) || (m[i][3] == 'T')))
			return true;
		if(((m[0][i] == c) || (m[0][i] == 'T')) && ((m[1][i] == c) || (m[1][i] == 'T')) && ((m[2][i] == c) || (m[2][i] == 'T')) && ((m[3][i] == c) || (m[3][i] == 'T')))
			return true;
	}
	if(((m[0][0] == c) || (m[0][0] == 'T')) && ((m[1][1] == c) || (m[1][1] == 'T')) && ((m[2][2] == c) || (m[2][2] == 'T')) && ((m[3][3] == c) || (m[3][3] == 'T')))
		return true;
	if(((m[3][0] == c) || (m[3][0] == 'T')) && ((m[2][1] == c) || (m[2][1] == 'T')) && ((m[1][2] == c) || (m[1][2] == 'T')) && ((m[0][3] == c) || (m[0][3] == 'T')))
		return true;
	return false;
}


void main()
{
	int n,i,j,count=0;
		
	fscanf(in,"%d",&n);
	while(count<n)
	{
		count++;
		int com=0;
		for(i=0;i<4;i++){
			fscanf(in,"%s",m[i]);
			for(j=0;j<4;j++){
				if(m[i][j]=='.')
					com++;
			}
		}	
		if(check('X')){
			fprintf(out,"Case #%d: X won\n",count);
		}
		else if(check('O')){
			fprintf(out,"Case #%d: O won\n",count);
		}
		else if(com!=0){
			fprintf(out,"Case #%d: Game has not completed\n",count);
		}
		else{
			fprintf(out,"Case #%d: Draw\n",count);
		}
	}
}