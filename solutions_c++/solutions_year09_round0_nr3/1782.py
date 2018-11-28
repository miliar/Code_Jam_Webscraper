#include <stdio.h>
#include <string.h>

FILE *fin = fopen ("input.txt","r");
FILE *fout = fopen ("output.txt","w");

int T,CASE,L,SL;
char S[555],W[555];
int P[555][3],C[555][3];

int main()
{
	int i,j;

	fscanf (fin,"%d\n",&T);
	while (T--){
		CASE++; fprintf (fout,"Case #%d: ",CASE);
		fgets(S,555,fin); SL = strlen(S); L = 0;

		for (i=SL-1;i>=0;i--){
			if (S[i] == ' ' || S[i] == 'a' || S[i] == 'c' || S[i] == 'd' ||
				S[i] == 'e' || S[i] == 'j' || S[i] == 'l' || S[i] == 'm' ||
				S[i] == 'o' || S[i] == 't' || S[i] == 'w'){
				P[L][0] = P[L][1] = P[L][2] = 0;
				C[L][0] = C[L][1] = C[L][2] = -1;
				W[L++] = S[i];
			}
		} W[L] = '\0';

		for (i=0;i<L;i++){
			if (W[i] == 'm'){C[i][0] = 1; P[i][0] = 1;}

			for (j=i-1;j>=0;j--){
				if (false){}
				else if (W[i] == ' '){
					if (C[j][0] != -1 && W[j] == 'j'){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][0]) % 10000;}
					if (C[j][0] != -1 && W[j] == 'c'){C[i][1] = 1; P[i][1] = (P[i][1] + P[j][0]) % 10000;}
					if (C[j][0] != -1 && W[j] == 't'){C[i][2] = 1; P[i][2] = (P[i][2] + P[j][0]) % 10000;}
				}
				else if (W[i] == 'a'){
					if (C[j][0] != -1 && W[j] == 'm'){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][0]) % 10000;}
				}
				else if (W[i] == 'c'){
					if (C[j][0] != -1 && W[j] == 'o'){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][0]) % 10000;}
					if (C[j][2] != -1 && W[j] == 'o'){C[i][1] = 1; P[i][1] = (P[i][1] + P[j][2]) % 10000;}
				}
				else if (W[i] == 'd'){
					if (C[j][0] != -1 && W[j] == 'e'){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][0]) % 10000;}
				}
				else if (W[i] == 'e'){
					if (C[j][0] != -1 && W[j] == ' '){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][0]) % 10000;}
					if (C[j][2] != -1 && W[j] == ' '){C[i][1] = 1; P[i][1] = (P[i][1] + P[j][2]) % 10000;}
					if (C[j][0] != -1 && W[j] == 'l'){C[i][2] = 1; P[i][2] = (P[i][2] + P[j][0]) % 10000;}
				}
				else if (W[i] == 'j'){
					if (C[j][0] != -1 && W[j] == 'a'){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][0]) % 10000;}
				}
				else if (W[i] == 'l'){
					if (C[j][1] != -1 && W[j] == 'c'){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][1]) % 10000;}
				}
				else if (W[i] == 'm'){
					if (C[j][1] != -1 && W[j] == 'e'){C[i][1] = 1; P[i][1] = (P[i][1] + P[j][1]) % 10000;}
				}
				else if (W[i] == 'o'){
					if (C[j][0] != -1 && W[j] == 'd'){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][0]) % 10000;}
					if (C[j][1] != -1 && W[j] == ' '){C[i][1] = 1; P[i][1] = (P[i][1] + P[j][1]) % 10000;}
					if (C[j][1] != -1 && W[j] == 'm'){C[i][2] = 1; P[i][2] = (P[i][2] + P[j][1]) % 10000;}
				}
				else if (W[i] == 't'){
					if (C[j][1] != -1 && W[j] == 'o'){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][1]) % 10000;}
				}
				else if (W[i] == 'w'){
					if (C[j][2] != -1 && W[j] == 'e'){C[i][0] = 1; P[i][0] = (P[i][0] + P[j][2]) % 10000;}
				}
			}
		}

		int SS = 0;
		for (i=0;i<L;i++){
			if (W[i] == 'w' && C[i][0] != -1) SS = (SS + P[i][0]) % 10000;
		}

		fprintf (fout,"%04d\n",SS);
	}

	return 0;
}

/*
"welcome to code jam"
' ' : 0 1 2
'a' : 0
'c' : 0 1
'd' : 0
'e' : 0 1 2
'j' : 0
'l' : 0
'm' : 0 1
'o' : 0 1 2
't' : 0
'w' : 0
*/