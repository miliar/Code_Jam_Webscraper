//
//  main.cpp
//  codejam
//
//  Created by Michelangelo Partipilo on 14-04-12.
//  Copyright (c) 2012. All rights reserved.
//

#include <iostream>
#include <string>
#include <map>

using namespace std;

class problemACase
{
    map<char, char> mapping;
public:
    void ParseInput()
    {
        getline(cin, _line);
    }
    
    string _line;
    string _lineResult;
    
    problemACase()
    {
        ParseInput();
        
        mapping['a'] = 'y';
        mapping['b'] = 'h';
        mapping['c'] = 'e';
        mapping['d'] = 's';
        mapping['e'] = 'o';
        mapping['f'] = 'c';
        mapping['g'] = 'v';
        mapping['h'] = 'x';
        mapping['i'] = 'd';
        mapping['j'] = 'u';
        mapping['k'] = 'i';
        mapping['l'] = 'g';
        mapping['m'] = 'l';
        mapping['n'] = 'b';
        mapping['o'] = 'k';
        mapping['p'] = 'r';
        mapping['q'] = 'z';
        mapping['r'] = 't';
        mapping['s'] = 'n';
        mapping['t'] = 'w';
        mapping['u'] = 'j';
        mapping['v'] = 'p';
        mapping['w'] = 'f';
        mapping['x'] = 'm';
        mapping['y'] = 'a';
        mapping['z'] = 'q';
        mapping[' '] = ' ';
    }
    
    void Solve()
    {
        _lineResult = _line;
        for (int i=0; i<_line.length(); i++) {
            if (mapping.find(_lineResult[i]) != mapping.end())
            {
                _lineResult[i] = mapping[_lineResult[i]];
            }
        }
    }
    
    string Result()
    {
        return _lineResult;
    }
};

int main(int argc, const char * argv[])
{
    int N = 0;
    string dummy;
    cin >> N;
    getline(cin, dummy);
    for (int i=1; i<=N; i++)
    {
        problemACase problem;
        problem.Solve();
        cout << "Case #" << i << ": " << problem.Result() << endl;
    }
    return 0;
}

