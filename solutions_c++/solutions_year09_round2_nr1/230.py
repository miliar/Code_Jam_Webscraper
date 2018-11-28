#include <stdio.h>
#include <string.h>

FILE *fin = fopen ("input.txt","r");
FILE *fout = fopen ("output.txt","w");

struct node{
	double P;
	char F[12];
	int L,R;
}F[100];

int T,L,A,N,C,U;
char M[111][12],AN[111];

int in()
{
	int c = C;

	char NAME[111], *t;

	while (1){
		fgets(NAME,111,fin); U++;
		t = strtok(NAME,"() \n");
		if (t != NULL) break;
	}

	double p;
	sscanf (t,"%lf",&p);
	F[c].P = p;

	t = strtok(NULL,"() \n");

	if (t != NULL){
		strcpy(F[c].F,t);
		C++; F[c].L = in();
		C++; F[c].R = in();
	}
	else F[c].L = F[c].R = -1;

	return c;
}

int main()
{
	int i;

	fscanf (fin,"%d\n",&T);

	int CASE = 0; double CUTE;

	while (T--){
		fscanf (fin,"%d\n",&L); C = U = 0; in();
		for (U;U<L;U++) fgets(AN,12,fin);
		fscanf (fin,"%d\n",&A);
		fprintf (fout,"Case #%d:\n",++CASE);

		for (U=0;U<A;U++){
			CUTE = 1.0000; fscanf (fin,"%s %d",&AN,&N);
			for (i=0;i<N;i++) fscanf (fin,"%s",M[i]);
			int S = 0;

			bool go;

			while (1){
				CUTE *= F[S].P;

				go = false;
				for (i=0;i<N;i++){
					if (strcmp(F[S].F,M[i]) == 0){go = true; break;}
				}

				if (go) S = F[S].L;
				else S = F[S].R;

				if (S == -1) break;
			}

			fprintf (fout,"%.7lf\n",CUTE);
		}
	}

	return 0;
}