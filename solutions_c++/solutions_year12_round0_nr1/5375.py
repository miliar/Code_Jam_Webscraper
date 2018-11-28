#include <fstream>
#include <cstdio>
#include <iostream>

using namespace std;

ifstream fin("A-small-attempt3.in");
ofstream fout("A-small-attempt3.out");

char themap[26];
bool mappedFrom[26];
bool mappedTo[26];

string from[] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	"y qee"};

string to[] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
	"a zoo"};

int main() {
	// find the mapping
	for (int i=0; i<26; i++){ 
		mappedFrom[i] = false;
		mappedTo[i] = false;
	}

	for (int i=0; i<4; i++) {
		for (int j=0; j<from[i].length(); j++) {
			if (from[i][j] == ' ') continue;
			char k = from[i][j] - 'a';
			themap[k] = to[i][j] - 'a';
			mappedFrom[k] = true;
			mappedTo[to[i][j]-'a'] = true;
		}
	}

	int mapFrom=-1, mapTo=-1;
	for (int i=0; i<26; i++) {
		if (!mappedFrom[i]) {
			mapFrom = i;
			//printf("From: %c\n", 'a'+i);
		}
		if (!mappedTo[i]) {
			mapTo = i;
			//printf("To: %c\n", 'a'+i);
		}
	}

	themap[mapFrom] = mapTo;

	/*
	for (int i=0; i<26; i++) {
		printf("%c -> %c\n", 'a'+i, themap[i]+'a');
	}
	*/


	int T;
	fin >> T;
	string str;
	getline(fin, str);
	for (int test=1;test<=T;test++) {
		getline(fin, str);
		for (int i=0; i<str.length(); i++) {
			if (str[i] == ' ') continue;
			str[i] = themap[str[i]-'a'] + 'a';
		}

		fout << "Case #" << test << ": " << str << endl;
	}
}


