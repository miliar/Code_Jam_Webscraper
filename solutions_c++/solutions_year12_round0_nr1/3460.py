#include <iostream>
#include <map>
#include <iterator>
#include <sstream>

using namespace std;


int main(int argc, char **argv) {
    map<char,char> tmap;

    // initalize the script generated translate map ;)
    tmap['a'] = 'y';
    tmap['b'] = 'h';
    tmap['c'] = 'e';
    tmap['d'] = 's';
    tmap['e'] = 'o';
    tmap['f'] = 'c';
    tmap['g'] = 'v';
    tmap['h'] = 'x';
    tmap['i'] = 'd';
    tmap['j'] = 'u';
    tmap['k'] = 'i';
    tmap['l'] = 'g';
    tmap['m'] = 'l';
    tmap['n'] = 'b';
    tmap['o'] = 'k';
    tmap['p'] = 'r';
    tmap['q'] = 'z';
    tmap['r'] = 't';
    tmap['s'] = 'n';
    tmap['t'] = 'w';
    tmap['u'] = 'j';
    tmap['v'] = 'p';
    tmap['w'] = 'f';
    tmap['x'] = 'm';
    tmap['y'] = 'a';
    tmap['z'] = 'q';
    tmap[' '] = ' ';
    int cases;
    // read the number of cases
    string tmp;
    getline(cin,tmp);
    stringstream ss(tmp);
    ss >> cases;

    // loop over all cases
    for( int i = 0; i < cases; ++i)
    {
      string in;
      // read the line with the testcase
      getline(cin,in);
      // output the line start
      cout << "Case #" << i+1 << ": ";
      // iterate over each map and output the translatet char
      for(string::iterator it = in.begin(); it != in.end(); ++it)
        cout << tmap[*it];
      // output the newline
      cout << endl;
    }
    // done

    return 0;
}
