// Dancing.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"

int _tmain(int argc, _TCHAR* argv[])
{
	int i=0;
	int j=0;
	int k=0;
	int n=0;
	int s=0;
	int m=0;
	int score[100];
	int solution[100];
	int y=0;

	FILE *fi;
	FILE *fo;

	fi = fopen("input.txt", "r");
	fo = fopen("output.txt","w");
	
	for(i=0;i<100;i++){
		score[i] = 0;
		solution[i] = 0;
	}

	fscanf(fi,"%d\n", &k);
	for(i=0;i<k;i++){
		fscanf(fi, "%d %d %d ",&n, &s, &m);
		for(j=0;j<n;j++)
			fscanf(fi, "%d", &score[j]);
		if(m == 0){
			solution[i] = n;
			continue;
		}


		for(y=0,j=0;j<n;j++)
			if(score[j] == 0){
				if(m == 0)
					y++;
			}
			else if(score[j]-m-(m-1)  >= m-1)
				y++;
			else if(s>0 && score[j]-m-(m-2) >=m-2)
				y++, s--;
		solution[i] = y;

	}
	for(i=0;i<k;i++)
		fprintf(fo, "Case #%d: %d\n", i+1, solution[i]);
	

	return 0;
}

