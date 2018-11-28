/*
 * main.cpp
 *
 *  Created on: 2011-04-28
 *      Author: ronanrmo
 */
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <map>

using namespace std;

#define F0(i,n) for(int i=0; i<n; i++)
#define F1(i,n) for(int i=1; i<n; i++)
#define clearfloat(array, size) memset(array, 0, sizeof(float)*size);
#define clearint(array, size) memset(array, 0, sizeof(int)*size);

char c0[] = " qazejp mysljylc kd kxveddknmc re jsicpdrysi";
char s0[] = " zyqour language is impossible to understand";

char c1[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char s1[] = "there are twenty six factorial possibilities";

char c2[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
char s2[] = "so it is okay if you want to just give up";


std::map<char, char> buildDict(){
	std::map<char,char> dict;
	int si0 = strlen(c0);
	int si1 = strlen(c1);
	int si2 = strlen(c2);

	for(int i =0; i <si0; i++){
		if(dict.find(c0[i]) == dict.end())
			dict.insert(std::pair<char, char>(c0[i], s0[i]));
	}

	for(int i =0; i <si1; i++){
		if(dict.find(c1[i]) == dict.end())
			dict.insert(std::pair<char, char>(c1[i], s1[i]));
	}

	for(int i =0; i <si2; i++){
		if(dict.find(c2[i]) == dict.end())
			dict.insert(std::pair<char, char>(c2[i], s2[i]));
	}
	return dict;
}


int main(int argc, char **argv)
{

	FILE *file_in, *file_out;


	// OPENING FILES ////////////////////////////////////////////////////////////////////

	// checking if first argument is not provided than redirect to stdin
	if(argc == 1){
		file_in = stdin;
	}
	// otherwise open file to write
	else{
		file_in   = fopen(argv[1], "r");
	}

	// checking if second argument is not provided than redirect to stdout
	if(argc < 3){
		file_out = stdout;
	}
	// otherwise open file to write
	else{
		file_out = fopen(argv[2], "w");
	}
	// END OPENING FILES ////////////////////////////////////////////////////////////////

	int T;
	char lb;
	fscanf(file_in, "%d", &T);



	std::map<char, char> dict;

	dict = buildDict();


	F0(t,T){
		char c;

		do{
			fscanf(file_in, "%c", &c);
		}while(c == '\n');

		std::vector<char> trn;

		fprintf(file_out, "Case #%d: ", t+1);
		while(c!='\n'){

			std::map<char,char>::iterator it = dict.find(c);
			if(it == dict.end()){
				fprintf(stderr, "Character [%c] not in dictionary\n", c);
				exit(0);
			}
			char t = it->second;

			fprintf(file_out, "%c", t);
			fflush(file_out);

			fscanf(file_in, "%c", &c);
		}
		fprintf(file_out, "\n")	;
	}


//	fprintf(file_out, "num %d\n", num);



	return 0;
}


