#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

int W, H;
string st;

char outst[1000];
char map[300];

void init(){
     map['a'] = 'y';
     map['y'] = 'a';
     map['e'] = 'o';
     map['j'] = 'u';
     map['p'] = 'r';
     map['m'] = 'l';
     map['s'] = 'n';
     map['l'] = 'g';   
     map['c'] = 'e';
     map['k'] = 'i';
     
     map['d'] = 's';
     map['x'] = 'm';
     map['v'] = 'p';
     map['n'] = 'b';
     map['r'] = 't';
     map['i'] = 'd';
     map['b'] = 'h';
     map['t'] = 'w';
     map['w'] = 'f';
     map['f'] = 'c';
     
     map['g'] = 'v';
     map['h'] = 'x';
     map['o'] = 'k';
     map['q'] = 'z';
     map['u'] = 'j';
     map['z'] = 'q';
}

void doit(){
       int i = 0;
       while (st[i] != 0){
             if (st[i] == ' ') outst[i] = ' ';
             else outst[i] = map[st[i]];
             i++;
       }
       outst[i] = 0;
}

int main(int argc, char *argv[])
{
    
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");
    init();
    int T;
    fin >> T;
    int i;
    getline(fin, st);
    for (i = 0; i < T; i++){
        getline(fin, st);
        doit();
        fout << "Case #" << i + 1 << ": " << outst << endl;
    }
    fout.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
