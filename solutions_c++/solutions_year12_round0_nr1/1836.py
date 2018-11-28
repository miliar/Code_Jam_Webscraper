// Speaking.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>
#include <conio.h>
char mappingTable[26][2] = {'!'};
FILE *fin,*fout;


void GenMapping(char *input, char *output) {
	for (int i=0;i< strlen(input);i++) {
		if (input[i] != ' ') {
			mappingTable[input[i]-'a'][1] = output[i];
			mappingTable[input[i]-'a'][0] = input[i];
		}
	}
}

bool verifyMappingIsOK() {
	bool result = true;
	for (int i=0;i<26;i++) {
		if (mappingTable[i][0]=='!' || mappingTable[i][1]=='!') {
			printf("%c is not found\n", 'a'+i);
			result = false;
		}
	}
	return result;
}

void findMissing() {
	int x[26],m;
	memset(x,0,sizeof(x));
	for (int i=0;i<26;i++) {
		x[ mappingTable[i][1]-'a' ] = 1;
	}
	for (int i=0;i<26;i++)
		if (x[i]==0)
			printf("%c is missing\n", i+'a');
}

void init() {
	memset(mappingTable,'!',sizeof(mappingTable));
	
	GenMapping("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
	GenMapping("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities");
	GenMapping("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up");
	GenMapping("q","z");
	GenMapping("z","q");

	findMissing();

	if ( !verifyMappingIsOK()) {
		printf("ERROR !\n");
	}

}

void process(char dataInput[200],int i) {
	fprintf(fout,"Case #%d: ",i);

	for (int i=0;i<strlen(dataInput);i++) {
		if (dataInput[i]== ' ')
			fprintf(fout," ");
		else if (dataInput[i]== '\n')
			fprintf(fout,"\n");
		else
			fprintf(fout,"%c", mappingTable[dataInput[i]-'a'][1]);
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	int N;

	fin = fopen("Speaking.txt","r");
	fout= fopen("Speaking.out","w");

	if (fin==NULL || fout==NULL) {
		printf("file error");
		getch();
		return 0;
	}

	init();

	fscanf(fin,"%d\n",&N);
	for (int i=1;i<=N;i++) {
		char dataInput[200];
		fgets(dataInput,sizeof(dataInput),fin);
		process(dataInput,i);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}

