#include<iostream>
#include<map>
#include<string>
#include<fstream>
using namespace std;

int main() {
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    string in = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    map<char,char> G;
    
    for(int i = 0; i < in.length(); i++) {
        G[in[i]] = out[i];
    }
    G['q'] = 'z';
    G['z'] = 'q';
    G[' '] = ' ';
    
    int T;
    int X = 1;
    string S;
    char I[200];

    fin >> T;
    fin.getline(I, 200);
    while(X <= T){
        fin.getline(I, 200);
        for(int i = 0; i < strlen(I); i++){
            S += G[I[i]];
        }
        fout << "Case #" << X << ": " << S << endl;
        S = "";
        X++;
    }
    return 0;
}