//============================================================================
// Name        : GCJ2012_A.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
using namespace std;

static char map[26] =  {'y', 'h', 'e', 's', 'o',
						'c', 'v', 'x', 'd', 'u',
						'i', 'g', 'l', 'b', 'k',
						'r', 'z', 't', 'n', 'w',
						'j', 'p', 'f', 'm', 'a',
						'q'};
char trans(char c){
	int index = c - 'a';
	char x = map[index];
	return x;
}
int main() {
	int testcase_num = 0;
	std::cin >> testcase_num;
	char d;
	cin.get(d);

	for(int i = 0; i < testcase_num; ++i){

		string text;

		while(true){

			char c;
			cin.get(c);

			if(c == ' '){
				text += c;
			}else if(c == '\n'){
				cout << "Case #" << i+1 << ": " << text << endl;
				break;
			}else{
				text += trans(c);
			}
		}

	}

	return 0;

}
