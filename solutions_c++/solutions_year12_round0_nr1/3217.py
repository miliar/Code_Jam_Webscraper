#include <iostream>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include "assert.h"

using namespace std;

void set_googlerese_to_english_dictionary(map<char, char>& g_to_e_dictionary)
{
    //{ 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v',
    //  'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l',
    //  'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n',
    //  'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
    //  'x': 'm', 'z': 'q'}
    g_to_e_dictionary['a'] = 'y';
    g_to_e_dictionary['b'] = 'h';
    g_to_e_dictionary['c'] = 'e';
    g_to_e_dictionary['d'] = 's';
    g_to_e_dictionary['e'] = 'o';
    g_to_e_dictionary['f'] = 'c';
    g_to_e_dictionary['g'] = 'v';
    g_to_e_dictionary['h'] = 'x';
    g_to_e_dictionary['i'] = 'd';
    g_to_e_dictionary['j'] = 'u';
    g_to_e_dictionary['k'] = 'i';
    g_to_e_dictionary['l'] = 'g';
    g_to_e_dictionary['m'] = 'l';
    g_to_e_dictionary['n'] = 'b';
    g_to_e_dictionary['o'] = 'k';
    g_to_e_dictionary['p'] = 'r';
    g_to_e_dictionary['q'] = 'z';
    g_to_e_dictionary['r'] = 't';
    g_to_e_dictionary['s'] = 'n';
    g_to_e_dictionary['t'] = 'w';
    g_to_e_dictionary['u'] = 'j';
    g_to_e_dictionary['v'] = 'p';
    g_to_e_dictionary['w'] = 'f';
    g_to_e_dictionary['x'] = 'm';
    g_to_e_dictionary['y'] = 'a';
    g_to_e_dictionary['z'] = 'q';

    g_to_e_dictionary[' '] = ' ';
}

string translate(const string& to_translate, map<char,char>& dict)
{
    string translatedString;
    typedef string::const_iterator CI;
    for(CI iter = to_translate.begin(); iter != to_translate.end(); ++iter){
        translatedString += dict[*iter];
    }
    return translatedString;
}

int main()
{
    map<char, char> googlerese_to_english_dictionary;
    set_googlerese_to_english_dictionary(googlerese_to_english_dictionary);

    ifstream input("A-small.in");
    ofstream output("A-small.out");

    string first_line;
    getline(input, first_line);
    istringstream string_input(first_line);
    int T;
    string_input >> T;
    assert(1 <= T && T <= 30);

    for(int currentCase = 1; currentCase <= T; currentCase++){
        string line = "";
        getline(input, line);
        output << "Case #" << currentCase << ": " << translate(line, googlerese_to_english_dictionary) << endl;
    }

    return 0;
}
