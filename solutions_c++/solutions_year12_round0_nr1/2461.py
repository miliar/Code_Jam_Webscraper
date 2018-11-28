#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int map[26];
string input;
int nTests;

ifstream fin ("A-small-attempt1.in");
ofstream fout ("tongues.out");
int main() {
    string in[4];
    string out[4];
    for (int i = 0; i < 26; i++) {
        map[i] = -1;
    }
    in[1] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    in[2] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    in[3] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    out[1] = "our language is impossible to understand";
    out[2] = "there are twenty six factorial possibilities";
    out[3] = "so it is okay if you want to just give up";
    for (int i = 1; i <=3; i++) {
        for (int s = 0; s < in[i].length(); s++) {
            map[int(in[i][s]) - 97] = int(out[i][s])-97;
        }
    }
    map[16] = 25;
    //map[24] = 16;
    map[25] = 16;   
    fin >> nTests;
    fin.ignore(1);
    for (int i = 0; i < nTests; i++) {
        fout << "Case #" << i+1 << ": ";
        string input;
        getline(fin,input);
        for (int s = 0; s < input.length(); s++) 
            if (input[s] != ' '){
                fout << char(map[int(input[s])-97] + 97);
            } else {
                fout << " ";
            }
        fout << endl;
    }
}
