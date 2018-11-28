#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cctype>

using namespace std;

typedef string::iterator iter;

vector<string> transpose(const vector<string>& v)
{
    vector<string> ret;
    for (int i = 0; i != 4; ++i) {
        string s;
        for (int j = 0; j != 4; ++j) {
            string temp = v[j];
            s += temp[i];
        }
        ret.push_back(s);
    }
    return ret;
}
char winner(const vector<string>& v)
{
    iter X, O, T, DOT;
    bool full = 1;
    vector<string> v_trans = transpose(v);
    string diag1, diag2;
    for (int i = 0; i != 4; ++i) {
        string line = v[i];
        diag1 += line[i];
        diag2 += line[3-i];
        X = find(line.begin(), line.end(), 'X');
        O = find(line.begin(), line.end(), 'O');
        DOT = find(line.begin(), line.end(), '.');
        T = find(line.begin(), line.end(), 'T');
        if (DOT == line.end() && O == line.end()) return 'X';
        if (DOT == line.end() && X == line.end()) return 'O';
    
        if (DOT != line.end()) full = 0;
        
        //transpose
        string line_trans = v_trans[i];
        X = find(line_trans.begin(), line_trans.end(), 'X');
        O = find(line_trans.begin(), line_trans.end(), 'O');
        DOT = find(line_trans.begin(), line_trans.end(), '.');
        T = find(line_trans.begin(), line_trans.end(), 'T');
        if (DOT == line_trans.end() && O == line_trans.end()) return 'X';
        if (DOT == line_trans.end() && X == line_trans.end()) return 'O';
    }
    
    //diag1:
    X = find(diag1.begin(), diag1.end(), 'X');
    O = find(diag1.begin(), diag1.end(), 'O');
    DOT = find(diag1.begin(), diag1.end(), '.');
    T = find(diag1.begin(), diag1.end(), 'T');
    if (DOT == diag1.end() && O == diag1.end()) return 'X';
    if (DOT == diag1.end() && X == diag1.end()) return 'O';
    
    //diag2:
    X = find(diag2.begin(), diag2.end(), 'X');
    O = find(diag2.begin(), diag2.end(), 'O');
    DOT = find(diag2.begin(), diag2.end(), '.');
    T = find(diag2.begin(), diag2.end(), 'T');
    if (DOT == diag2.end() && O == diag2.end()) return 'X';
    if (DOT == diag2.end() && X == diag2.end()) return 'O';
    
    if (full) return 'D';
    return 'N';
       
}
int main()
{
    ifstream infile("A-large.in");
    ofstream outfile("out.txt");
    int i;
    string line, trash;
    getline(infile, line);
    istringstream str(line);
    str >> i;
    cout << i << endl;
    for (int j = 1; j<= i; ++j) {
        vector<string> v(4);
        for (int k = 0; k != 4; ++k) {
            getline(infile, v[k]);
        }
        char state = winner(v);
        if (i != j) {
        if (state == 'X' || state == 'O') outfile << "Case #" << j << ": " << state << " won" << endl;
        if (state == 'D') outfile << "Case #" << j << ": " << "Draw" << endl;
        if (state == 'N') outfile << "Case #" << j << ": " << "Game has not completed" << endl;
        }
        else {
        if (state == 'X' || state == 'O') outfile << "Case #" << j << ": " << state << " won";
        if (state == 'D') outfile << "Case #" << j << ": " << "Draw";
        if (state == 'N') outfile << "Case #" << j << ": " << "Game has not completed";
        }
        getline(infile, trash);
    }
    return 0;
}