#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

FILE *fin = fopen ("input.txt","r");
FILE *fout = fopen ("output.txt","w");

int T,L,I;
char V[22],P[22],m,t;

int main()
{
	int i,j,k,f;

	fscanf (fin,"%d",&T);

	int CASE = 0;

	while (T--){
		fscanf (fin,"%s",&V); L = strlen(V);
		fprintf (fout,"Case #%d: ",++CASE);

		f = 1;
		for (i=0;i<L-1;i++){
			if (V[i] < V[i+1]){f = 0; break;}
		}

		if (f){
			for (i=L-1;i>=0;i--){
				if (V[i] != '0'){
					fprintf (fout,"%c",V[i]); I = i;
					break;
				}
			}

			for (i=L-1;i>=0;i--){
				if (V[i] != '0') break;
				fprintf (fout,"0");
			}fprintf (fout,"0");

			
			for (i=I-1;i>=0;i--) fprintf (fout,"%c",V[i]);
			fprintf (fout,"\n"); continue;
		}

		for (k=1;k<L;k++){
			f = 1;
			for (i=k;i<L-1;i++){
				if (V[i] < V[i+1]){f = 0; break;}
			}
			
			if (f){
				m = char(100);
				for (i=k;i<L;i++){
					if (V[i] > V[k-1] && m > V[i]){m = V[i]; I = i;}
				}

				t = V[k-1]; V[k-1] = V[I]; V[I] = t;

				for (i=k;i<L;i++){
					for (j=i+1;j<L;j++){
						if (V[i] > V[j]){
							t = V[i]; V[i] = V[j]; V[j] = t;
						}
					}
				}

				break;
			}
		}

		fprintf (fout,"%s\n",V);
	}

	return 0;
}