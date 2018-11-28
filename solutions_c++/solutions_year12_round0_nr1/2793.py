#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(){
    map<char, char> mTrans;
    string linha, lixo;
    string::iterator it;
    char auxC;
    int T;
    mTrans['a'] = 'y';
    mTrans['b'] = 'h';
    mTrans['c'] = 'e';
    mTrans['d'] = 's';
    mTrans['e'] = 'o';
    mTrans['f'] = 'c';
    mTrans['g'] = 'v';
    mTrans['h'] = 'x';
    mTrans['i'] = 'd';
    mTrans['j'] = 'u';
    mTrans['k'] = 'i';
    mTrans['l'] = 'g';
    mTrans['m'] = 'l';
    mTrans['n'] = 'b';
    mTrans['o'] = 'k';
    mTrans['p'] = 'r';
    mTrans['q'] = 'z';
    mTrans['r'] = 't';
    mTrans['s'] = 'n';
    mTrans['t'] = 'w';
    mTrans['u'] = 'j';
    mTrans['v'] = 'p';
    mTrans['w'] = 'f';
    mTrans['x'] = 'm';
    mTrans['y'] = 'a';
    mTrans['z'] = 'q';
    mTrans[' '] = ' ';
    cin >> T;
    getline(cin,lixo);
    for(int i = 1; i <= T; i++){
        getline(cin,lixo);
        linha = "";
        for(it = lixo.begin(); it != lixo.end(); it++){
            auxC = *it;
            linha += mTrans[auxC];
        }
        cout << "Case #" << i << ": " << linha << endl;
    }
    return 0;
}
