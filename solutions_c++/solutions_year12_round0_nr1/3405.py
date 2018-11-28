////////////////////////////////////////////////////////////////////////////////
// ProblemA.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//        Solves Problem A:Speaking in Tongues
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//  Created:  04/14/2012 00:42:02
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <cstring>
#include <cassert>
#include <vector>

using namespace std;

int char_to_int(char c)
{
    if (c == ' ')
        return 26;
    return ((int) c - (int) 'a');
}

char int_to_char(int i)
{
    if (i == 26)
        return ' ';
    return ('a' + (char) i);
}

////////////////////////////////////////////////////////////////////////////////
/*! Program entry point
//  @param[in]  argc    Number of arguments
//  @param[in]  argv    Argument strings
//  @return     status  (0 on sucess)
*///////////////////////////////////////////////////////////////////////////////
int main(int argc, const char *argv[])
{
    int map[27];
    for (int i = 0; i < 27; ++i) {
        map[i] = -1;
    }

    // Gimmes
    map[char_to_int('y')] = char_to_int('a');
    map[char_to_int('e')] = char_to_int('o');
    map[char_to_int('q')] = char_to_int('z');

    // Train
    const char *cryptSample = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    const char *plainSample = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    for (int i = 0; i < strlen(cryptSample); ++i)
        map[char_to_int(cryptSample[i])] = char_to_int(plainSample[i]);

    vector<bool> mapped(27, false);
    // At this point, only z is undecypted. Find what mapps to it (it's the
    // unmapped character)
    for (int i = 0; i < 26; ++i) {
        if (map[i] != -1)
            mapped[map[i]] = true;
    }
    for (int i = 0; i < 26; ++i) {
        if (!mapped[i]) {
            map[char_to_int('z')] = i;
        }
    }


    int numTests;
    cin >> numTests;
    string dummy;
    getline(cin, dummy);
    for (int t = 1; t <= numTests; ++t)  {
        string cryptLine;
        getline(cin, cryptLine);
        cout << "Case #" << t << ": ";
        for (unsigned int i = 0; i < cryptLine.length(); ++i)
            cout << int_to_char(map[char_to_int(cryptLine[i])]);
        cout << endl;
    }

    return 0;
}
