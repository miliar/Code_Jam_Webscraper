#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>

using namespace std;

const char
mapto(char a) {

	switch (a) {
	  case 'a': return 'y';
	  case 'b': return 'h';
	  case 'c': return 'e';
	  case 'd': return 's';
	  case 'e': return 'o';
	  case 'f': return 'c';
	  case 'g': return 'v';
	  case 'h': return 'x';
	  case 'i': return 'd';
	  case 'j': return 'u';
	  case 'k': return 'i';
	  case 'l': return 'g';
	  case 'm': return 'l';
	  case 'n': return 'b';
	  case 'o': return 'k';
	  case 'p': return 'r';
	  case 'q': return 'z';
	  case 'r': return 't';
	  case 's': return 'n';
	  case 't': return 'w';
	  case 'u': return 'j';
	  case 'v': return 'p';
	  case 'w': return 'f';
	  case 'x': return 'm';
	  case 'y': return 'a';
       case 'z': return 'q';
	  default : return a;
	}
}

int main(int argc, char **argv) {
	int case_num = 1;
	char buffer[100];
	string str, s;
	bool first = 0;
	int total_cases;
	int TC_num = 0;
	
	ifstream read_file (argv[1]);

	if (read_file.is_open()) {
	    while (getline(read_file, str)) {
			 if (!first) {
				 total_cases = atoi(str.c_str());
				 first = 1;
			 } else {
				 s.clear();

				 string::iterator it = str.begin();
				 while (it != str.end()) {
					 s.push_back(mapto(*it));
					 it++;
				 }

				 cout << "Case #"<< ++TC_num << ": ";

				 it = s.begin();
				 for (; it != s.end(); it++) {
					 cout << *it;
				 }
				 cout << endl;
			 }
	    }
	    read_file.close();
	}
}
