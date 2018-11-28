// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int numCases ; 
	FILE *in = fopen("A-large.in","r");
	FILE *out = fopen("output.txt","w");

	fscanf(in,"%d",&numCases);

	for(int i=0;i<numCases;i++) {
		fprintf(out,"Case #%d:",i+1);
		char buf[10][10];
		for(int j=0;j<4;j++) {
			fscanf(in,"%s",buf[j]);
		}
		fscanf(in,"\n");

		bool Xwon = false, Ywon = false ; 
		bool xwon = true, ywon =true ; 

		// check row
		for(int j=0;j<4;j++) {
			xwon = true; ywon =true ; 
			for(int k=0;k<4;k++) {
				if (buf[j][k] == 'X') { ywon = false ; }
				else if (buf[j][k] == 'O' ) { xwon = false ; }
				else if (buf[j][k] == '.' ) { xwon = false ; ywon=false; }
			}
			if (xwon) { Xwon = true ; }
			if (ywon) { Ywon = true ; }
		}

		// check column 
		for(int j=0;j<4;j++) {
			xwon = true; ywon =true ; 
			for(int k=0;k<4;k++) {
				if (buf[k][j] == 'X') { ywon = false ; }
				else if (buf[k][j] == 'O' ) { xwon = false ; }
				else if (buf[k][j] == '.' ) { xwon = false ; ywon=false; }
			}
			if (xwon) { Xwon = true ; }
			if (ywon) { Ywon = true ; }
		}

		// check diagonal 
		xwon = true; ywon =true ; 
		for(int j=0 ;j<4;j++) {
			if (buf[j][j] == 'X') { ywon = false ; }
			else if (buf[j][j] == 'O' ) { xwon = false ; }
			else if (buf[j][j] == '.' ) { xwon = false ; ywon=false; }
		}
		if (xwon) { Xwon = true ; }
		if (ywon) { Ywon = true ; }

		xwon = true; ywon =true ; 
		for(int j=0 ;j<4;j++) {
			if (buf[j][3-j] == 'X') { ywon = false ; }
			else if (buf[j][3-j] == 'O' ) { xwon = false ; }
			else if (buf[j][3-j] == '.' ) { xwon = false ; ywon=false; }
		}
		if (xwon) { Xwon = true ; }
		if (ywon) { Ywon = true ; }

		if (Xwon && !Ywon) { fprintf(out," X won\n"); continue; }
		if (Ywon && !Xwon) { fprintf(out," O won\n"); continue; }
		if (Xwon && Ywon) {fprintf(out," Draw\n"); continue; }
		
		bool iscompleted = true; 
		for(int j=0;j<4;j++) {
			for(int k=0;k<4;k++) {
				if ( buf[j][k] == '.' ) { iscompleted = false ; break; }
			}
		}

		if (iscompleted ) {fprintf(out," Draw\n"); continue; }
		fprintf(out," Game has not completed\n");
	

	}

	fclose(in);
	fclose(out);
	return 0;
}

