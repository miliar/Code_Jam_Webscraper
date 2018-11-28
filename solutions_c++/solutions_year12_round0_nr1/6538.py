#include <string.h>
#include <stdlib.h>

#include <iostream>
#include <string>

char tbl[26] = {0, };
	
void makeTable()
{
	char *strInput = 
		"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";

	char *strOut = 
		"our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

	char *p0 = strInput;
	char *p1 = strOut;

	for(int i = 0; i < 26; i++) {
		tbl[i] = ' ';
	}

	int used[26] = {0, };

	tbl['a'-'a'] = 'y'; used['y'-'a'] = 1;
	tbl['o'-'a'] = 'e'; used['e'-'a'] = 1;
	tbl['z'-'a'] = 'q'; used['q'-'a'] = 1;

	int N = strlen(strInput);

	for(int i = 0; i < N; i++) {
		if(*p0 != ' ') {
			tbl[*p0 -'a'] = *p1;
			used[*p0 - 'a'] = 1;
		}
		p0++;
		p1++;
	}

	for(int i = 0; i < 26; i++) {
		if(used[i] == 0) {
			for(int j = 0; j < 26; j++) {
				if(tbl[j] == ' ') {
					tbl[j] = i+'a';
					break;
				}
			}
		}
	}

	for(int i = 0; i < 26; i++) {
		std::cout << (char)('a'+i) << ": " << tbl[i] << " " << used[i] << std::endl;
	}
}

int main(int argc, char *argv[])
{
	makeTable();

	int testCase;

	std::string tmp;
	getline(std::cin, tmp);
	testCase = atoi(tmp.c_str());

	for(int cnt = 1; cnt <= testCase; cnt++) {
		std::string strIn;
		std::string strOut;

		getline(std::cin, strIn);

		int n = strIn.size();

		for(int i = 0; i < n; i++) {
			char c = ' ';
			if(strIn[i] != ' ') {
				c = tbl[strIn[i] - 'a'];
			}
			strOut += c;
		}

		std::cout 
			<< "Case #" << cnt << ": " 
			<< strOut << std::endl;
	}
}
