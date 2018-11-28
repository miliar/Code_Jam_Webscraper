// Recycled.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <conio.h>
#include <stdlib.h>
FILE *fin,*fout;

int T,A,B;
int check[10];

bool notfound(int key) {
	for (int i=1;i<=check[0];i++) {
		if (key==check[i])
			return false;
	}
	return true;
}

long long process() {
	long long count = 0;
	int i,k;

//	A = B = 4562008;

	
	for (int n=A;n<=B;n++) {
		char s[20],t[20];
		//fprintf(fout,"[%d]\n",n);
		sprintf_s(s, "%d",n);
		memset(t,0,sizeof(t));
		memset(check,0,sizeof(check));
		for (i=1;i<strlen(s);i++) {
			

			for (int j=i , k=0 ; k<strlen(s) ;k++) {
				t[k] = s[j];
				j++;
				if (j==strlen(s))
					j = 0;
			}
			
			// calculate here

			int tt = atoi(t);

			if (strcmp(t,s)>0 && tt <=B) {
				//fprintf(fout,"%s",t);
				//fprintf(fout," OK\n");
				
				if (notfound(tt)) {
					check[++check[0]] = tt;
					count++;
				}
				
				
			}
			
		}
	}



	return count;
}

int _tmain(int argc, _TCHAR* argv[])
{
	fin = fopen("Recycled.in","r");
	fout= fopen("Recycled.out","w");

	fscanf(fin, "%d", &T);

	for (int t = 1 ;t<=T;t++) {
		fscanf(fin, "%d %d\n", &A,&B);
		
		fprintf(fout,"Case #%d: %lld\n",t,process());


		
	}
	
	fclose(fin);
	fclose(fout);
	return 0;
}

