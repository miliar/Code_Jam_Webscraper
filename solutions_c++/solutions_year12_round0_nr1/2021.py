//============================================================================
// Name        : cj_1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>

using namespace std;

int main() {
    std::map<char, char> mapka;
    mapka['a'] = 'y';
    mapka['b'] = 'h';
    mapka['c'] = 'e';
    mapka['d'] = 's';
    mapka['e'] = 'o';
    mapka['f'] = 'c';
    mapka['g'] = 'v';
    mapka['h'] = 'x';
    mapka['i'] = 'd';
    mapka['j'] = 'u';
    mapka['k'] = 'i';
    mapka['l'] = 'g';
    mapka['m'] = 'l';
    mapka['n'] = 'b';
    mapka['o'] = 'k';
    mapka['p'] = 'r';
    mapka['q'] = 'z';
    mapka['r'] = 't';
    mapka['s'] = 'n';
    mapka['t'] = 'w';
    mapka['u'] = 'j';
    mapka['v'] = 'p';
    mapka['w'] = 'f';
    mapka['x'] = 'm';
    mapka['y'] = 'a';
    mapka['z'] = 'q';
    mapka[' '] = ' ';

	int cnt = 0;
	cin >> cnt;
    cin.ignore(1000,'\n');

    for(int i = 0 ; i < cnt; ++i)
    {
        string inputLine;
        getline(cin, inputLine);
        string outputLine;

        for(size_t c = 0 ; c < inputLine.size(); ++c)
        {
            outputLine.push_back(mapka[inputLine[c]]);
        }
        cout << "Case #" << (i+1) << ": " << outputLine << endl;
    }

	return 0;
}
