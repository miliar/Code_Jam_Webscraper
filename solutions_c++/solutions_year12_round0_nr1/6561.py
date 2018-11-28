// ejp mysljylc kd kxveddknmc re jsicpdrysi
// rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
// de kr kd eoya kw aej tysr re ujdr lkgc jv
// Case #1: our language is impossible to understand
// Case #2: there are twenty six factorial possibilities
// Case #3: so it is okay if you want to just give up

#include <iostream>
#include <map>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
    ifstream input(argv[1]);
    ofstream output("codejam_1_out.txt");

    if(!input) {
        cout << "Wrong Input!\n";

        return -1;
    }

    map<char,char> g_map;
    
    g_map['a'] = 'y';
    g_map['b'] = 'h';
    g_map['c'] = 'e';
    g_map['d'] = 's';
    g_map['e'] = 'o';
    g_map['f'] = 'c';
    g_map['g'] = 'v';
    g_map['h'] = 'x';
    g_map['i'] = 'd';
    g_map['j'] = 'u';
    g_map['k'] = 'i';
    g_map['l'] = 'g';
    g_map['m'] = 'l';
    g_map['n'] = 'b';
    g_map['o'] = 'k';
    g_map['p'] = 'r';
    g_map['q'] = 'z';
    g_map['r'] = 't';
    g_map['s'] = 'n';
    g_map['t'] = 'w';
    g_map['u'] = 'j';
    g_map['v'] = 'p';
    g_map['w'] = 'f';
    g_map['x'] = 'm';
    g_map['y'] = 'a';
    g_map['z'] = 'q';

    int num;
    input >> num;
    cout << num << endl;

    char line[256];
    input.getline(line, 256);

    for(int i=1;i<=num;i++) {
        if(input.fail()) {
            cout << "Reached the End\n";
            break;
        }
        input.getline(line, 256);
        output << "Case #" << i << ": ";
        int linecnt = 0;
        for(int j=0;j<100;j++) {
            if(line[j] != ' ' && ((line[j] >= 65 && line[j]<=90) || 
                (line[j] >=97 && line[j]<=122))) {
                output << g_map[line[j]];
                linecnt = 0;
            } else if(line[j] == ' ' && linecnt == 0) {
                output << ' ';
                linecnt++;
            } else {
                break;
            }
        }
        output << "\n";
    }

    input.close();
    output.close();
    return 0;
    
}

