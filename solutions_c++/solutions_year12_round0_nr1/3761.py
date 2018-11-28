#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

string translate(string input){

    char flip[122];
    flip['a'] = 'y';
    flip['b'] = 'h';
    flip['c'] = 'e';
    flip['d'] = 's';
    flip['e'] = 'o';
    flip['f'] = 'c';
    flip['g'] = 'v';
    flip['h'] = 'x';
    flip['i'] = 'd';
    flip['j'] = 'u';
    flip['k'] = 'i';
    flip['l'] = 'g';
    flip['m'] = 'l';
    flip['n'] = 'b';
    flip['o'] = 'k';
    flip['p'] = 'r';
    flip['q'] = 'z';
    flip['r'] = 't';
    flip['s'] = 'n';
    flip['t'] = 'w';
    flip['u'] = 'j';
    flip['v'] = 'p';
    flip['w'] = 'f';
    flip['x'] = 'm';
    flip['y'] = 'a';
    flip['z'] = 'q';
    flip[' '] = ' ';
    
    string output = "";

    for(int i = 0; i<input.length(); i++){
        output += flip[input[i]];
    }

    return output;
}

int main(){
    

    int N=0;
    string line;
    //scanf("%d",&N);
    cin >> N;
    getline(cin,line);
    for(int i = 0;i < N; i++){
        getline(cin,line);
        //printf("Case %d: %s\n",i,line);
        cout << "Case #" << i+1 << ": " << translate(line) << endl;
    }
}
