#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

inline int f(char ch) {
 	return (int(ch)-int('a'));
}

int main() {

	int i, j, k;

	int T;

	char mapping[26]={'-'};
	bool yes[26]={0};

	mapping[f('a')]='y';
	mapping[f('o')]='e';
	mapping[f('z')]='q';
	mapping[f('q')]='z';

	const char *out[]={
	 	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
	};

	const char *in[]={
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"
	};


	for (i = 0; i < 3; i++) {
		for (j = 0; j < strlen(in[i]); j++) {
			if(out[i][j] != ' ')	{
			 	yes[f(in[i][j])]=true;
				mapping[f(out[i][j])]=in[i][j];
			}
		}
	}

	for (i = 0; i < 26; i++) {
		cout << char(i+'a') << " : " << mapping[i] << endl;
	}

	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small.out");


	i=0;
	string str;
	fin >> T;
	getline(fin, str, '\n');

	while(i<T) {
	 	cout << i << " " << T << endl;
		getline(fin, str, '\n');
		cout << str;
		for (j = 0; j < str.length(); j++) {
			if(str[j] != ' ')	str[j]=mapping[f(str[j])];
		}
		fout << "Case #" << i+1 << ": " << str << endl;
		//cout << "Case #" << i+1 << ": " << str << endl;

		i++;
	}
	fin.close();
	fout.close();

	return 0;
}
