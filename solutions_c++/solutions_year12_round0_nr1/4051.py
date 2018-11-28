// SpeakingInTongues.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int _tmain(int argc, _TCHAR* argv[])
{
	char cypher[] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq";
	char plain[] =  "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz";
	char reference[27] = "";
	char google[31][102];
	char solution[31][102];
	FILE *fi;
	FILE *fo;

	int i=0;
	int j=0;
	int k=0;
	int l=0;

	fi=fopen("input.txt","r");
	fo=fopen("output.txt","w");

//	printf("Input\n");
	fscanf(fi,"%d\n", &k);
	if(k<1 || k>30){
		printf("Error\n");
		return 0;
	}

	for(i=0;i<sizeof(cypher);i++){
		l=cypher[i]-'a';
		reference[l] = plain[i];

	}

	for(i=0;i<30;i++){
		google[i][0] = '\0';
		solution[i][0] = '\0';

	}
	for(i=0;i<k;i++){
		fgets(google[i], sizeof(google[i]),fi);
	//	if(strlen(google[i])>=100){
	//		strcpy(solution[i],"Too long string");
	//		continue;
	//	}
		
		for(j=0;j<strlen(google[i])-1;j++){
			if(google[i][j] != ' '){
				l=google[i][j] - 'a';
				solution[i][j] = reference[l];
			}
			else if(google[i][j] == ' ')
				solution[i][j] = ' ';
		}
		solution[i][j] = '\0';

	}
	
	for(i=0;i<k;i++)
		fprintf(fo,"Case #%d: %s\n", i+1, solution[i]);
	

	return 0;
}

