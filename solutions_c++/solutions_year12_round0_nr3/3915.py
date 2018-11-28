// codejam_sara_c.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin = fopen("infil.txt", "r");
	FILE *fout = fopen("utfil.txt", "w");
	int x=0;
	int y=0;
	int i=0;
	int j=0;
	int antalcase=0;
	int par=0;
	int ten=0;
	int jprim=0;

if (fin==NULL){ 
	perror ("Error opening input file");
	return 0;
}
if (fout ==NULL) {
	perror ("Error opening output file");
	return 0;
}
	fscanf(fin,"%d\n", &antalcase);
	for (i=0; i<antalcase; i++) {
		fscanf(fin,"%d", &x);
		fscanf(fin,"%d", &y);
		if (x > 9)
			x=x;
		for (j=x; j < y+1; j++) {
			jprim = j;
//			if (j== 112)
			do {
				for(ten=1; ten*10 <= j; ten *= 10);
				jprim=jprim/10+(jprim%10)*ten;
				if (j < jprim && jprim <=y) par++;
				else if (jprim == j) ten = j+1;
			} while (jprim != j);
		}
		fprintf(fout, "Case #%d: %d\n",i+1, par);
		par=0;
	}



	return 0;
}

