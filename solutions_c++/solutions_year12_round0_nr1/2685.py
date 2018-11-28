#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char data[30] = {
    'y', 'h', 'e', 's', 'o', 'c', 'v',
    'x', 'd', 'u', 'i', 'g', 'l', 'b',
    'k', 'r', 'z', 't', 'n', 'w',
    'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
    ifstream in("A.in");
    ofstream out("A.out");

    int T;
    in >> T;
    string line;
    getline(in, line);
    char ch;
    for (int i=1; i<=T; ++i) {
	getline(in, line);
	for (int j=0; j<line.size(); ++j) {
	    ch = line[j];
	    if (ch == ' ') continue;
	    ch = data[ch-'a'];
	    line[j] = ch;
	}
	out << "Case #" << i << ": " << line << endl;
    }

    out.close();
    in.close();

    return 0;
}
