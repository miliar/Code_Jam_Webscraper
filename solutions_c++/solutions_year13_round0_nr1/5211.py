#include <iostream>

void main(){
	FILE *ulaz = fopen("A-large.in","r");
	FILE *izlaz = fopen("A-large.out","w");
	int n;
	fscanf(ulaz,"%d",&n);
	int popunjeno = 1;
	fgetc(ulaz);
	char polje[4][4];
	for( int k = 1; k < n+1; k++ ){
		popunjeno = 1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				polje[i][j] = fgetc(ulaz);
				if ( polje[i][j] == '.')
					popunjeno = 0;
			}
			fgetc(ulaz);
		}
		fgetc(ulaz);
		//x horiyontalno
		if ( ((polje[0][0]=='X')||(polje[0][0]=='T'))&&((polje[0][1]=='X')||(polje[0][1]=='T'))&&((polje[0][2]=='X')||(polje[0][2]=='T'))&&((polje[0][3]=='X')||(polje[0][3]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}
		if ( ((polje[1][0]=='X')||(polje[1][0]=='T'))&&((polje[1][1]=='X')||(polje[1][1]=='T'))&&((polje[1][2]=='X')||(polje[1][2]=='T'))&&((polje[1][3]=='X')||(polje[1][3]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}
		if ( ((polje[2][0]=='X')||(polje[2][0]=='T'))&&((polje[2][1]=='X')||(polje[2][1]=='T'))&&((polje[2][2]=='X')||(polje[2][2]=='T'))&&((polje[2][3]=='X')||(polje[2][3]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}
		if ( ((polje[3][0]=='X')||(polje[3][0]=='T'))&&((polje[3][1]=='X')||(polje[3][1]=='T'))&&((polje[3][2]=='X')||(polje[3][2]=='T'))&&((polje[3][3]=='X')||(polje[3][3]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}
		//x vertikalno
		if ( ((polje[0][0]=='X')||(polje[0][0]=='T'))&&((polje[1][0]=='X')||(polje[1][0]=='T'))&&((polje[2][0]=='X')||(polje[2][0]=='T'))&&((polje[3][0]=='X')||(polje[3][0]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}
		if ( ((polje[0][1]=='X')||(polje[0][1]=='T'))&&((polje[1][1]=='X')||(polje[1][1]=='T'))&&((polje[2][1]=='X')||(polje[2][1]=='T'))&&((polje[3][1]=='X')||(polje[3][1]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}
		if ( ((polje[0][2]=='X')||(polje[0][2]=='T'))&&((polje[1][2]=='X')||(polje[1][2]=='T'))&&((polje[2][2]=='X')||(polje[2][2]=='T'))&&((polje[3][2]=='X')||(polje[3][2]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}
		if ( ((polje[0][3]=='X')||(polje[0][3]=='T'))&&((polje[1][3]=='X')||(polje[1][3]=='T'))&&((polje[2][3]=='X')||(polje[2][3]=='T'))&&((polje[3][3]=='X')||(polje[3][3]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}
		//x koso
		if ( ((polje[0][0]=='X')||(polje[0][0]=='T'))&&((polje[1][1]=='X')||(polje[1][1]=='T'))&&((polje[2][2]=='X')||(polje[2][2]=='T'))&&((polje[3][3]=='X')||(polje[3][3]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}
		if ( ((polje[0][3]=='X')||(polje[0][3]=='T'))&&((polje[1][2]=='X')||(polje[1][2]=='T'))&&((polje[2][1]=='X')||(polje[2][1]=='T'))&&((polje[3][0]=='X')||(polje[3][0]=='T')) ){
			fprintf(izlaz,"Case #%d: X won\n",k);
			continue;
		}

		//O horiyontalno
		if ( ((polje[0][0]=='O')||(polje[0][0]=='T'))&&((polje[0][1]=='O')||(polje[0][1]=='T'))&&((polje[0][2]=='O')||(polje[0][2]=='T'))&&((polje[0][3]=='O')||(polje[0][3]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		if ( ((polje[1][0]=='O')||(polje[1][0]=='T'))&&((polje[1][1]=='O')||(polje[1][1]=='T'))&&((polje[1][2]=='O')||(polje[1][2]=='T'))&&((polje[1][3]=='O')||(polje[1][3]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		if ( ((polje[2][0]=='O')||(polje[2][0]=='T'))&&((polje[2][1]=='O')||(polje[2][1]=='T'))&&((polje[2][2]=='O')||(polje[2][2]=='T'))&&((polje[2][3]=='O')||(polje[2][3]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		if ( ((polje[3][0]=='O')||(polje[3][0]=='T'))&&((polje[3][1]=='O')||(polje[3][1]=='T'))&&((polje[3][2]=='O')||(polje[3][2]=='T'))&&((polje[3][3]=='O')||(polje[3][3]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		//O vertikalno
		if ( ((polje[0][0]=='O')||(polje[0][0]=='T'))&&((polje[1][0]=='O')||(polje[1][0]=='T'))&&((polje[2][0]=='O')||(polje[2][0]=='T'))&&((polje[3][0]=='O')||(polje[3][0]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		if ( ((polje[0][1]=='O')||(polje[0][1]=='T'))&&((polje[1][1]=='O')||(polje[1][1]=='T'))&&((polje[2][1]=='O')||(polje[2][1]=='T'))&&((polje[3][1]=='O')||(polje[3][1]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		if ( ((polje[0][2]=='O')||(polje[0][2]=='T'))&&((polje[1][2]=='O')||(polje[1][2]=='T'))&&((polje[2][2]=='O')||(polje[2][2]=='T'))&&((polje[3][2]=='O')||(polje[3][2]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		if ( ((polje[0][3]=='O')||(polje[0][3]=='T'))&&((polje[1][3]=='O')||(polje[1][3]=='T'))&&((polje[2][3]=='O')||(polje[2][3]=='T'))&&((polje[3][3]=='O')||(polje[3][3]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		//O koso
		if ( ((polje[0][0]=='O')||(polje[0][0]=='T'))&&((polje[1][1]=='O')||(polje[1][1]=='T'))&&((polje[2][2]=='O')||(polje[2][2]=='T'))&&((polje[3][3]=='O')||(polje[3][3]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		if ( ((polje[0][3]=='O')||(polje[0][3]=='T'))&&((polje[1][2]=='O')||(polje[1][2]=='T'))&&((polje[2][1]=='O')||(polje[2][1]=='T'))&&((polje[3][0]=='O')||(polje[3][0]=='T')) ){
			fprintf(izlaz,"Case #%d: O won\n",k);
			continue;
		}
		if (popunjeno == 0){
			fprintf(izlaz,"Case #%d: Game has not completed\n",k);
			continue;
		}
		else
			fprintf(izlaz,"Case #%d: Draw\n",k);

	}
	fclose(izlaz);
	fclose(ulaz);
}