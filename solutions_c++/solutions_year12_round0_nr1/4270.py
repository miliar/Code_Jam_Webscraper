#include<iostream>
#include<fstream>
using namespace std;

int main() {
    ifstream fin ("a.in");
    ofstream fout ("a.out");
    int n;
    fin >> n;
    string s;
    getline(fin,s);
    for(int i = 0; i < n; ++i) {
        getline(fin,s);
        fout << "Case #" << i+1 << ": ";
        for(int ii = 0; ii < s.size(); ++ii) {
            if(s[ii] == ' ') fout << " ";
            else if(s[ii] == 'y') fout << "a";
            else if(s[ii] == 'n') fout << "b";
            else if(s[ii] == 'f') fout << "c";
            else if(s[ii] == 'i') fout << "d";
            else if(s[ii] == 'c') fout << "e";
            else if(s[ii] == 'w') fout << "f";
            else if(s[ii] == 'l') fout << "g";
            else if(s[ii] == 'b') fout << "h";
            else if(s[ii] == 'k') fout << "i";
            else if(s[ii] == 'u') fout << "j";
            else if(s[ii] == 'o') fout << "k";
            else if(s[ii] == 'm') fout << "l";
            else if(s[ii] == 'x') fout << "m";
            else if(s[ii] == 's') fout << "n";
            else if(s[ii] == 'e') fout << "o";
            else if(s[ii] == 'v') fout << "p";
            else if(s[ii] == 'z') fout << "q";
            else if(s[ii] == 'p') fout << "r";
            else if(s[ii] == 'd') fout << "s";
            else if(s[ii] == 'r') fout << "t";
            else if(s[ii] == 'j') fout << "u";
            else if(s[ii] == 'g') fout << "v";
            else if(s[ii] == 't') fout << "w";
            else if(s[ii] == 'h') fout << "x";
            else if(s[ii] == 'a') fout << "y";
            else if(s[ii] == 'q') fout << "z";
        }
        fout << endl;
    }
}
