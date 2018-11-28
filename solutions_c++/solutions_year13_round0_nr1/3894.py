/*
ID: zachary11
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>

using namespace std;

template <typename Type>
string toString(Type t){
	stringstream ss;
        string s;
	ss << t;
        ss >> s;
        return s;
}

string tomekBoard(string a, string b, string c, string d){
    if(count(a.begin(), a.end(), 'X') + count(a.begin(), a.end(), 'T') == 4) return "X won";
    if(count(b.begin(), b.end(), 'X') + count(b.begin(), b.end(), 'T') == 4) return "X won";
    if(count(c.begin(), c.end(), 'X') + count(c.begin(), c.end(), 'T') == 4) return "X won";
    if(count(d.begin(), d.end(), 'X') + count(d.begin(), d.end(), 'T') == 4) return "X won";
    if(count(a.begin(), a.end(), 'O') + count(a.begin(), a.end(), 'T') == 4) return "O won";
    if(count(b.begin(), b.end(), 'O') + count(b.begin(), b.end(), 'T') == 4) return "O won";
    if(count(c.begin(), c.end(), 'O') + count(c.begin(), c.end(), 'T') == 4) return "O won";
    if(count(d.begin(), d.end(), 'O') + count(d.begin(), d.end(), 'T') == 4) return "O won";
    string vert = toString(a[0]) + toString(b[0]) + toString(c[0]) + toString(d[0]);
    if(count(vert.begin(), vert.end(), 'X') + count(vert.begin(), vert.end(), 'T') == 4) return "X won";
    if(count(vert.begin(), vert.end(), 'O') + count(vert.begin(), vert.end(), 'T') == 4) return "O won";
    vert = toString(a[1]) + toString(b[1]) + toString(c[1]) + toString(d[1]);
    if(count(vert.begin(), vert.end(), 'X') + count(vert.begin(), vert.end(), 'T') == 4) return "X won";
    if(count(vert.begin(), vert.end(), 'O') + count(vert.begin(), vert.end(), 'T') == 4) return "O won";
    vert = toString(a[2]) + toString(b[2]) + toString(c[2]) + toString(d[2]);
    if(count(vert.begin(), vert.end(), 'X') + count(vert.begin(), vert.end(), 'T') == 4) return "X won";
    if(count(vert.begin(), vert.end(), 'O') + count(vert.begin(), vert.end(), 'T') == 4) return "O won";
    vert = toString(a[3]) + toString(b[3]) + toString(c[3]) + toString(d[3]);
    if(count(vert.begin(), vert.end(), 'X') + count(vert.begin(), vert.end(), 'T') == 4) return "X won";
    if(count(vert.begin(), vert.end(), 'O') + count(vert.begin(), vert.end(), 'T') == 4) return "O won";
    string diag = toString(a[0]) + toString(b[1]) + toString(c[2]) + toString(d[3]);
    if(count(diag.begin(), diag.end(), 'X') + count(diag.begin(), diag.end(), 'T') == 4) return "X won";
    if(count(diag.begin(), diag.end(), 'O') + count(diag.begin(), diag.end(), 'T') == 4) return "O won";
    diag = toString(a[3]) + toString(b[2]) + toString(c[1]) + toString(d[0]);
    if(count(diag.begin(), diag.end(), 'X') + count(diag.begin(), diag.end(), 'T') == 4) return "X won";
    if(count(diag.begin(), diag.end(), 'O') + count(diag.begin(), diag.end(), 'T') == 4) return "O won";
    string comb = a+b+c+d;
    //cout << comb << " " << count(comb.begin(), comb.end(), '.') << endl;
    if(count(comb.begin(), comb.end(), '.') > 0) return "Game has not completed";
    return "Draw";
}

int main() {
    ofstream fout("codeJam.out");
    ifstream fin("codeJam.in");
    int caseNumber=0;
    string discard;
    fin >> caseNumber;
    for(int i=1; i<=caseNumber; i++){
        string a,b,c,d;
        fin >> a >> b >> c >> d;
        string solution = tomekBoard(a,b,c,d);
        fout << "Case #" << i << ": " << solution << endl;
        cout << "Case #" << i << ": " << solution << endl;
    }
    
    return 0;
}
