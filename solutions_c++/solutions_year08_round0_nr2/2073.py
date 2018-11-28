#include <iostream>
#include <string>
#include <math.h>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i, a, b) for(int i=a; i<b; i++)
#define FORE(i, a, b) for(int i=a; i<=b; i++)
#define FORD(i, a, b) for(int i=a; i>b; i--)
#define FORDE(i, a, b) for(int i=a; i>=b; i--)
#define debug false

int n, t, na, nb;

int ***a, ***b;		// [trip][start/end][h/m]
int **list, listi;	// [list posn][ [ab][trip][start/end] ]

// t1 vs t2
int cmp(int *i1, int *i2) {	// compare times. i[ab][trip][start/end]
	int t1[2], t2[2];
	if(!i1[0]) 	{ t1[0]=a[i1[1]][i1[2]][0]; t1[1]=a[i1[1]][i1[2]][1]; }
	else 		{ t1[0]=b[i1[1]][i1[2]][0]; t1[1]=b[i1[1]][i1[2]][1]; }
	if(!i2[0]) 	{ t2[0]=a[i2[1]][i2[2]][0]; t2[1]=a[i2[1]][i2[2]][1]; }
	else 		{ t2[0]=b[i2[1]][i2[2]][0]; t2[1]=b[i2[1]][i2[2]][1]; }
	if(t1[0]!=t2[0]) { if(t1[0]<t2[0]) return -1; return 1; }
	else { if(t1[1]==t2[1]) return 0; if(t1[1]<t2[1]) return -1; return 1; }
}
bool equals(int *i1, int *i2) {	// compare times. i[ab][trip][start/end]
	int t1[2], t2[2];
	if(!i1[0]) 	{ t1[0]=a[i1[1]][i1[2]][0]; t1[1]=a[i1[1]][i1[2]][1]; }
	else 		{ t1[0]=b[i1[1]][i1[2]][0]; t1[1]=b[i1[1]][i1[2]][1]; }
	if(!i2[0]) 	{ t2[0]=a[i2[1]][i2[2]][0]; t2[1]=a[i2[1]][i2[2]][1]; }
	else 		{ t2[0]=b[i2[1]][i2[2]][0]; t2[1]=b[i2[1]][i2[2]][1]; }
	return (t1[0]==t2[0] && t1[1]==t2[1]);
}

// insert entry after posn
void insert(int *in, int posn) {
	FORD(i, listi, posn) FOR(j, 0, 3) list[i+1][j]=list[i][j];
	FOR(j, 0, 3) list[posn+1][j]=in[j];
	listi++;
}

// shelter homeless entries
void place(int *in) {
	if(listi==0) { insert(in, -1); return; }		// list is empty, yay
	int curr[3]; FOR(i, 0, 3) curr[i]=-1;
	FORDE(i, listi-1, 0) {
		FOR(j, 0, 3) curr[j]=list[i][j]; int comp=cmp(in, curr);
		if(comp==0) return;							// if it's already there, drop
		else if(comp>0) { insert(in, i); return; }	// insert
	}
	insert(in, -1);	// it belongs at the beginning
}

int main() {
	FILE *fin, *fout;
    fin = fopen("B-large.in", "r"); fout = fopen("B.out", "w");

	fscanf(fin, "%d\n", &n);

	FORE(cases, 1, n) {
		fscanf(fin, "%d\n%d %d\n", &t, &na, &nb);
	// inits
		a = new int**[na]; b = new int**[nb];
		FOR(i, 0, na) { a[i] = new int*[2]; FOR(j, 0, 2) a[i][j]=new int[2]; }
		FOR(i, 0, nb) { b[i] = new int*[2]; FOR(j, 0, 2) b[i][j]=new int[2]; }
		list = new int*[2*(na+nb)+1]; FOR(i, 0, 2*(na+nb)+1) { list[i] = new int[3]; FOR(j, 0, 3) list[i][j]=-1; listi=0; }

	// input && list insertion
		FOR(i, 0, na) {
			fscanf(fin, "%d:%d %d:%d\n", &a[i][0][0], &a[i][0][1], &a[i][1][0], &a[i][1][1]);
			a[i][1][1]+=t;	// add turnaround to arrival
			if(a[i][1][1]>=60) { a[i][1][0]+=a[i][1][1]/60; a[i][1][1]=a[i][1][1]%60; }	// overflow
			int in[3]; in[0]=0; in[1]=i; in[2]=0; place(in); in[2]=1; place(in);		// list insert
		}
		FOR(i, 0, nb) {
			fscanf(fin, "%d:%d %d:%d\n", &b[i][0][0], &b[i][0][1], &b[i][1][0], &b[i][1][1]);
			b[i][1][1]+=t;	// add turnaround to arrival
			if(b[i][1][1]>=60) { b[i][1][0]+=b[i][1][1]/60; b[i][1][1]=b[i][1][1]%60; }	// overflow
			int in[3]; in[0]=1; in[1]=i; in[2]=0; place(in); in[2]=1; place(in);		// list insert
		}

/*	// checkkkk
		FOR(i, 0, listi) {
			if(!list[i][0]) printf("%d:%d\n", a[list[i][1]][list[i][2]][0], a[list[i][1]][list[i][2]][1]);
			else			printf("%d:%d\n", b[list[i][1]][list[i][2]][0], b[list[i][1]][list[i][2]][1]);
		}
*/
		int at=0, bt=0;		// train count
		int atmin=0, btmin=0;
		FOR(i, 0, listi) {
			int curr[3], in[3]; FOR(j, 0, 3) curr[j]=list[i][j];
//			if(!curr[0])	printf("%d:%d\t", a[curr[1]][curr[2]][0], a[curr[1]][curr[2]][1]);
//			else			printf("%d:%d\t", b[curr[1]][curr[2]][0], b[curr[1]][curr[2]][1]);
			in[0]=0; FOR(i, 0, na) { in[1]=i;
				FOR(j, 0, 2) { in[2]=j;
					if(equals(curr, in)) {
						if(!j) 	at--;	// depart
						else	bt++;	// arrive
					}
				}
			}
			in[0]=1; FOR(i, 0, nb) { in[1]=i;
				FOR(j, 0, 2) { in[2]=j;
					if(equals(curr, in)) {
						if(!j) 	bt--;	// depart
						else	at++;	// arrive
					}
				}
			}
//			printf("%d\t%d\n", at, bt);
			if(at<atmin) atmin=at;
			if(bt<btmin) btmin=bt;
		}
		atmin*=-1; btmin*=-1;
//		printf("Case #%d: %d %d\n", cases, atmin, btmin);
		fprintf(fout, "Case #%d: %d %d\n", cases, atmin, btmin);

	}

	fclose(fin);
	fclose(fout);
	system("pause");
    return 0;
}
