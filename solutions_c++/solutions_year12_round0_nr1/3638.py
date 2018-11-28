//q1
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int main () {
    string line1, g, s;
    ifstream file ("test.txt");
    ofstream output ("output.txt");
    
    getline (file, line1);
    int t = atoi(line1.c_str());

    for (int i = 0;i < t; ++i) {
        getline(file, g);
	s.resize(g.length());
            for(int j = 0; j < g.length(); ++j){
                if (g[j] == ' '){
			s[j] = ' ';
                } else if (g[j] == 'a') {
                	s[j] = 'y';
		} else if (g[j] == 'b') {
			s[j] = 'h';
                } else if (g[j] == 'c') {
                	s[j] = 'e';
		} else if (g[j] == 'd') {
			s[j] = 's';
                } else if (g[j] == 'e') {
                	s[j] = 'o';
		} else if (g[j] == 'f') {
			s[j] = 'c';
                } else if (g[j] == 'g') {
                	s[j] = 'v';
		} else if (g[j] == 'h') {
			s[j] = 'x';
                } else if (g[j] == 'i') {
                	s[j] = 'd';
		} else if (g[j] == 'j') {
			s[j] = 'u';
                } else if (g[j] == 'k') {
                	s[j] = 'i';
		} else if (g[j] == 'l') {
			s[j] = 'g';
                } else if (g[j] == 'm') {
                	s[j] = 'l';
		} else if (g[j] == 'n') {
			s[j] = 'b';
                } else if (g[j] == 'o') {
                	s[j] = 'k';
		} else if (g[j] == 'p') {
			s[j] = 'r';
                } else if (g[j] == 'q') {
                	s[j] = 'z';
		} else if (g[j] == 'r') {
			s[j] = 't';
                } else if (g[j] == 's') {
                	s[j] = 'n';
		} else if (g[j] == 't') {
			s[j] = 'w';
                } else if (g[j] == 'u') {
                	s[j] = 'j';
		} else if (g[j] == 'v') {
			s[j] = 'p';
                } else if (g[j] == 'w') {
                	s[j] = 'f';
		} else if (g[j] == 'x') {
			s[j] = 'm';
                } else if (g[j] == 'y') {
                	s[j] = 'a';
		} else if (g[j] == 'z') {
			s[j] = 'q';
                } 
            }
        output << "Case #" << i+1 << ": ";
        output << s << endl;
    }

return 0;
}
