#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <regex.h>
using namespace std;

int main (int argc, char * const argv[]) {
	
    // HANDLE COMMAND-LINE ARGUMENTS
	// freopen("example.in", "rt", stdin);
	
	freopen(argv[1], "rt", stdin);
	if(argc == 3){
		freopen(argv[2], "wt", stdout);
	}
	else if(argc==2){
		string out = argv[1];
		out = out.substr(0, out.size() - 2);
		out += "out";
		cout << "Result file: " << out << endl;
		freopen(out.c_str(), "wt", stdout);
	}
	else {
		cout << "Input file required!\nUsage: ./" << argv[0] << " example.in [example.out]" << endl;
		return 0;	
	}
	
	int N = 0;	
	cin >> N;
	cin.ignore(1, '\n');
	
	for(int testCaseNum=0; testCaseNum<N; ++testCaseNum){		
		cout << "Case #" << testCaseNum+1 << ": ";
		string lineIn;

		getline(cin, lineIn);
		
		string lineOut = lineIn;
		
		for (int i=0; i<lineIn.length(); ++i) {
			switch (lineIn[i]) {
				case 'a':lineOut[i] = 'y'; break;
				case 'b':lineOut[i] = 'h'; break;
				case 'c':lineOut[i] = 'e'; break;
				case 'd':lineOut[i] = 's'; break;
				case 'e':lineOut[i] = 'o'; break;
				case 'f':lineOut[i] = 'c'; break;
				case 'g':lineOut[i] = 'v'; break;
				case 'h':lineOut[i] = 'x'; break;
				case 'i':lineOut[i] = 'd'; break;
				case 'j':lineOut[i] = 'u'; break;
				case 'k':lineOut[i] = 'i'; break;
				case 'l':lineOut[i] = 'g'; break;
				case 'm':lineOut[i] = 'l'; break;
				case 'n':lineOut[i] = 'b'; break;
				case 'o':lineOut[i] = 'k'; break;
				case 'p':lineOut[i] = 'r'; break;
				case 'q':lineOut[i] = 'z'; break;
				case 'r':lineOut[i] = 't'; break;
				case 's':lineOut[i] = 'n'; break;
				case 't':lineOut[i] = 'w'; break;
				case 'u':lineOut[i] = 'j'; break;
				case 'v':lineOut[i] = 'p'; break;
				case 'w':lineOut[i] = 'f'; break;
				case 'x':lineOut[i] = 'm'; break;
				case 'y':lineOut[i] = 'a'; break;
				case 'z':lineOut[i] = 'q'; break;
				case ' ':lineOut[i] = ' '; break;
				default: break;
			}
		}
		cout << lineOut << endl;
	}
	return 0;
}
