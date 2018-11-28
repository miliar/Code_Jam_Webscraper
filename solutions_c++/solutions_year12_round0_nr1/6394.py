#include <iostream>
#include <map>
#include <fstream>
#include <cstring>

using namespace std;

map<char, char> googleres;

int main () {
    /*googleres.insert( pair<char,char> ('a','y') );
    googleres.insert( pair<char,char> ('b','h') );
    googleres.insert( pair<char,char> ('c','e') );
    googleres.insert( pair<char,char> ('d','s') );
    googleres.insert( pair<char,char> ('e','o') );
    googleres.insert( pair<char,char> ('f','c') );
    googleres.insert( pair<char,char> ('g','v') );
    googleres.insert( pair<char,char> ('h','x') );
    googleres.insert( pair<char,char> ('i','d') );
    googleres.insert( pair<char,char> ('j','u') );
    googleres.insert( pair<char,char> ('k','i') );
    googleres.insert( pair<char,char> ('l','g') );
    googleres.insert( pair<char,char> ('m','l') );
    googleres.insert( pair<char,char> ('n','b') );
    googleres.insert( pair<char,char> ('o','k') );
    googleres.insert( pair<char,char> ('p','r') );
    googleres.insert( pair<char,char> ('q','z') );
    googleres.insert( pair<char,char> ('r','t') );
    googleres.insert( pair<char,char> ('s','n') );
    googleres.insert( pair<char,char> ('t','w') );
    googleres.insert( pair<char,char> ('u','j') );
    googleres.insert( pair<char,char> ('v','p') );
    googleres.insert( pair<char,char> ('w','f') );
    googleres.insert( pair<char,char> ('x','m') );
    googleres.insert( pair<char,char> ('y','a') );
    googleres.insert( pair<char,char> ('z','q') );
    googleres.insert( pair<char,char> (' ',' ') );*/

    googleres['a'] = 'y';
    googleres['b'] = 'h';
    googleres['c'] = 'e';
    googleres['d'] = 's';
    googleres['e'] = 'o';
    googleres['f'] = 'c';
    googleres['g'] = 'v';
    googleres['h'] = 'x';
    googleres['i'] = 'd';
    googleres['j'] = 'u';
    googleres['k'] = 'i';
    googleres['l'] = 'g';
    googleres['m'] = 'l';
    googleres['n'] = 'b';
    googleres['o'] = 'k';
    googleres['p'] = 'r';
    googleres['q'] = 'z';
    googleres['r'] = 't';
    googleres['s'] = 'n';
    googleres['t'] = 'w';
    googleres['u'] = 'j';
    googleres['v'] = 'p';
    googleres['w'] = 'f';
    googleres['x'] = 'm';
    googleres['y'] = 'a';
    googleres['z'] = 'q';
    googleres[' '] = ' ';

    ifstream fin("in.txt");
    ofstream fout("out.txt");

    int T;
    fin>>T;
            char codeJam[200];
    fin.getline(codeJam,100);
    cout<<T;
    for(int i = 0; i < T; i ++) {

        fin.getline(codeJam,200);

        int len = strlen(codeJam);
        char output[200];
        int j;
        for(j = 0; j < len; j++)
            output[j] = googleres[codeJam[j]];
        output[j] = '\0';
        fout<<"Case #"<<i+1<<": "<<output<<"\n";
        cout<<"Case #"<<i+1<<": "<<output<<"\n";
    }
}
