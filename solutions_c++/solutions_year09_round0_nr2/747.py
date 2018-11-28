#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>

FILE *f, *g;
int nr_test;

int t;
int w, h;

int a[100][100];	// altitudine
int b[100][100]; 	// bazin
int d[100][100]; 	// directie


int qi[10010];
int qj[10010];
char coresp[32];
int stq=0, sfq=0;

void calculeaza_dir() {

	int i, j;

	for (i=0; i<h; i++) {
		for (j=0; j<w; j++) {
			int crt = a[i][j];
			// n, v, e, s
			int dir = 0;
			int min = crt;

			if ((i-1 >= 0) && (a[i-1][j] < min)) {
				dir = 1;	// n
				min = a[i-1][j];
			}
			if (( j-1 >= 0) && (a[i][j-1] < min)) {
				dir = 2;	// v
				min = a[i][j-1];
			}
			if ((j+1 < w) && (a[i][j+1] < min)) {
				dir = 3;	// e
				min = a[i][j+1];
			}
			if ((i+1 < h) && (a[i+1][j] < min)) {
				dir = 4;	// s
				min = a[i+1][j];
			}

			d[i][j] = dir;
		}
	}

}

void afi_q() {
     int i, j, k;
     
     printf("Q: ");
     for (k=stq; k<sfq; k++) {
         i = qi[k];
         j = qj[k];
         
         printf("(%i %i) ", i, j);
     
     }
     printf("\n");
}

void afi_dir(char* s) {
     int i, j;
     
     printf("%s\n",s );
     for (i=0; i<h; i++) {
         for (j=0; j<w; j++) {
             printf("%i", d[i][j]);
         }
         printf("\n");
     }

     printf("Bazin\n",s );
     for (i=0; i<h; i++) {
         for (j=0; j<w; j++) {
             printf("%i", b[i][j]);
         }
         printf("\n");
     }

}
void rezolva() {
	int i, j;
    stq = 0;
    sfq = 0;


	fscanf(f, "%i%i", &h, &w);

	for (i=0; i<h; i++){
		for (j=0; j<w; j++) {
			fscanf(f, "%i", &(a[i][j]));
			b[i][j] = 0;

		}
	}

	calculeaza_dir();


	int nrb=0;

	// pun in coada punctele care nu se varsa mai departe
	for (i=0; i<h; i++){
		for (j=0; j<w; j++) {

			if (d[i][j] == 0) {
				qi[sfq] = i;
				qj[sfq] = j;
				nrb++;
				b[i][j] = nrb;
				sfq++;
			}
		}
	}
//    afi_q();
//    afi_dir("Directii:");
	while(1) {
		i = qi[stq];
		j = qj[stq];
		int bazin = b[i][j];
		stq++;

		if ((i-1 >= 0) && (d[i-1][j] == 4)) {
			qi[sfq] = i-1;
			qj[sfq] = j;
			b[i-1][j] = bazin;
			sfq++;
		}
		if ((i+1 < h) && (d[i+1][j] == 1)) {
			qi[sfq] = i+1;
			qj[sfq] = j;
			b[i+1][j] = bazin;
			sfq++;
		}
		if ((j-1 >= 0) && (d[i][j-1] == 3)) {
			qi[sfq] = i;
			qj[sfq] = j-1;
			b[i][j-1] = bazin;
			sfq++;
		}
		if ((j+1 < w) && (d[i][j+1] == 2)) {
			qi[sfq] = i;
			qj[sfq] = j+1;
			b[i][j+1] = bazin;
			sfq++;
		}

//      afi_q();
        //getch();
		if (stq==sfq)
			break;
	}
	// TODO: verifica daca au fost setate toate
        //afi_dir("Directii");
        //getch();

	fprintf(g, "Case #%i:\n", nr_test);
	for (i=0; i<=nrb; i++) {
		coresp[i] = 0;
	}
	char next_ch = 'a';


	for (i=0; i<h; i++){
		for (j=0; j<w; j++) {
			int bazin = b[i][j];

			if (bazin == 0) {
				printf("Bazin = 0  [%i %i]\n", i, j); fflush(stdout);
				getch();
			}

			if (coresp[bazin] == 0) {
				coresp[bazin] = next_ch;
				next_ch++;
			}

			fprintf(g, "%c", coresp[bazin]);
			if (j<w-1) fprintf(g, " ");
		}
		fprintf(g, "\n");
	}


}

int main() {

/*
	int i, j;
	g = fopen("auxx.in", "wt");
	fprintf(g, "%i\n", 100);

	for (int k=0; k<100; k++) {
		fprintf(g, "100 100\n");
		for (i=0; i<100; i++) {
			for (j=0; j<100; j++) {
				if (i%2 == 0)
					fprintf(g, "%i ", 100*i+j);
				else
					fprintf(g, "%i ", 100*i+99-j);
			}
			fprintf(g, "\n");
		}
	}
	fclose(g);

	exit(0);
	// aux
*/





	f=fopen("b.in", "rt");

	if (!f) {
		printf("Nu\n");
		fflush(stdout);
		getch();
	}
	g=fopen("b.out", "wt");





	fscanf(f, "%i", &t);
	for (nr_test=1; nr_test<=t; nr_test++) {
		rezolva();
	}
	fclose(f);
	fclose(g);
}
