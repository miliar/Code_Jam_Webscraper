#include <iostream>
#include <sstream>
#include <stdio.h>
#include <cstdlib>
#include <string>
using namespace std;

int main() {
	int count;
	scanf("%d", &count);
	string junk;
	getline(cin, junk);
	char map[26] = {'y' ,'h' ,'e' ,'s' ,'o' ,'c' ,'v' ,'x' ,'d' ,'u' ,'i' ,'g' ,'l' ,'b' ,'k' ,'r' ,'z' ,'t' ,'n' ,'w' ,'j' ,'p' ,'f' ,'m' ,'a' ,'q'};

	for(int i=1; i<=count; ++i) {
		string line;
		getline(cin, line);
		printf("Case #%d: ", i);
		istringstream iss(line);
		
		do {
			string word;
			iss >> word;
			for(int j=0; j<word.length(); ++j)
				printf("%c", map[(int)word[j]-97]);
			printf(" ");
		} while(iss);
		printf("\n");
	}
	return 0;
}
