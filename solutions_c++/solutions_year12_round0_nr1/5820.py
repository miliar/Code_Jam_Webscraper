#include <iostream>
#include <fstream>
#include <string>
using namespace std;


char inEnglish(char a){
switch (a)
				{
					case 'a':
						return 'y';
						break;
					case 'b':
						return 'h';
						break;
					case 'c':
						return 'e';
						break;
					case 'd':
						return 's';
						break;
					case 'e':
						return 'o';
						break;
					case 'f':
						return 'c';
						break;
					case 'g':
						return 'v';
						break;
					case 'h':
						return 'x';
						break;
					case 'i':
						return 'd';
						break;
					case 'j':
						return 'u';
						break;
					case 'k':
						return 'i';
						break;
					case 'l':
						return 'g';
						break;
					case 'm':
						return 'l';
						break;
					case 'n':
						return 'b';
						break;
					case 'o':
						return 'k';
						break;
					case 'p':
						return 'r';
						break;
					case 'q':
						return 'z';
						break;
					case 'r':
						return 't';
						break;
					case 's':
						return 'n';
						break;
					case 't':
						return 'w';
						break;
					case 'u':
						return 'j';
						break;
					case 'v':
						return 'p';
						break;
					case 'w':
						return 'f';
						break;
					case 'x':
						return 'm';
						break;
					case 'y':
						return 'a';
						break;
					case 'z':
						return 'q';
						break;
					case ' ':
						return ' ';
						break;
				}
}


int main()
{
	int T;
	string str;
	ifstream in("input.txt");
	ofstream out("out.txt");

		in >> T;
		getline(in, str);

		for(int i=1; i<=T; i++){
			getline(in, str);
			int len = str.length();
			out << "Case #" << i << ": ";
			for (int j=0; j<len; j++){
				out << inEnglish(str[j]);
			}
		out << endl;
		}

	out.close();
	in.close();
	return 0;
}
