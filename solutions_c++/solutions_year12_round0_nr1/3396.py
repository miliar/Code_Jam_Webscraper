#include <iostream>
#include <map>
#include <fstream>
#include <cstdlib>
using namespace std;

typedef map< char, char > Mapping;

int main(int argc, char **argv) {
    Mapping mapping;

    // insert mapping
    mapping.insert(Mapping::value_type('y', 'a'));
    mapping.insert(Mapping::value_type('n', 'b'));
    mapping.insert(Mapping::value_type('f', 'c'));
    mapping.insert(Mapping::value_type('i', 'd'));
    mapping.insert(Mapping::value_type('c', 'e'));
    mapping.insert(Mapping::value_type('w', 'f'));
    mapping.insert(Mapping::value_type('l', 'g'));
    mapping.insert(Mapping::value_type('b', 'h'));
    mapping.insert(Mapping::value_type('k', 'i'));
    mapping.insert(Mapping::value_type('u', 'j'));
    mapping.insert(Mapping::value_type('o', 'k'));
    mapping.insert(Mapping::value_type('m', 'l'));
    mapping.insert(Mapping::value_type('x', 'm'));
    mapping.insert(Mapping::value_type('s', 'n'));
    mapping.insert(Mapping::value_type('e', 'o'));
    mapping.insert(Mapping::value_type('v', 'p'));
    mapping.insert(Mapping::value_type('z', 'q'));
    mapping.insert(Mapping::value_type('p', 'r'));
    mapping.insert(Mapping::value_type('d', 's'));
    mapping.insert(Mapping::value_type('r', 't'));
    mapping.insert(Mapping::value_type('j', 'u'));
    mapping.insert(Mapping::value_type('g', 'v'));
    mapping.insert(Mapping::value_type('t', 'w'));
    mapping.insert(Mapping::value_type('h', 'x'));
    mapping.insert(Mapping::value_type('a', 'y'));
    mapping.insert(Mapping::value_type('q', 'z'));

    // read input file
    ifstream ifile (argv[1]);
    ofstream ofile (argv[2]);

    if (!ifile || !ofile) { cout << "Error: files cant be opened"; exit (1); }

    int T, t = 1;
    char buff[1000];
    Mapping::iterator it;

    ifile >> T;
    ifile.ignore();

    while (t <= T) {
        ofile << "Case #" << t << ": ";
        ifile.getline( buff, 1000 );

        for (int i = 0; buff[i] != '\0'; i++) {
            if (buff[i] != ' ') {
                it = mapping.find(buff[i]);
                ofile << it->second;
            } else {
                ofile << ' ';
            }
        }
        ofile << endl;
        t++;
    }
}
