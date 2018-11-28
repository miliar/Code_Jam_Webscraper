#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int main(int argc, const char* argv[])
{
	int T;
	string line;
	ifstream file(argv[1]);
	ofstream file2("result.txt");

    map<char, char> corr;
    corr['a'] = 'y';
    corr['b'] = 'h';
    corr['c'] = 'e';
    corr['d'] = 's';
    corr['e'] = 'o';
    corr['f'] = 'c';
    corr['g'] = 'v';
    corr['h'] = 'x';
    corr['i'] = 'd';
    corr['j'] = 'u';
    corr['k'] = 'i';
    corr['l'] = 'g';
    corr['m'] = 'l';
    corr['n'] = 'b';
    corr['o'] = 'k';
    corr['p'] = 'r';
    corr['q'] = 'z';
    corr['r'] = 't';
    corr['s'] = 'n';
    corr['t'] = 'w';
    corr['u'] = 'j';
    corr['v'] = 'p';
    corr['w'] = 'f';
    corr['x'] = 'm';
    corr['y'] = 'a';
    corr['z'] = 'q';
    corr[' '] = ' ';
    // Obtained thanks to the input/output examples and the hint z -> q

    file >> T;
    getline(file, line);
	for(int it = 0; it < T; ++it)
	{
	    file2 << "Case #" << it+1 << ": ";
	    cout << "Case #" << it+1 << ": ";
		getline(file, line);
        for(int i = 0; i < line.size(); ++i)
        {
            file2 << corr[line.at(i)];
            cout << corr[line.at(i)];
        }

        file2  << endl;
        cout << endl;
	}

	return 0;
}
