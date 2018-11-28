#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main()
{
	fstream in, out;
	int T;
	string gString;
	char c;
	char maps[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	
	in.open("A-small-attempt0.in", ios::in);
	out.open("A-small-attempt0.out", ios::out);
	in >> T;
	getline(in, gString);
	
	for(int i=0; i<T; i++) {
		getline(in,gString);
		out << "Case #" << i+1 << ": ";
		for(int j=0; j<(int)gString.size(); j++)
		{
			c = gString.at(j);
			if(c == ' ') out << ' ';
			else {
				out << maps[c-97];
			}
		}
		out << endl;
	}
	
	return 0;
}
