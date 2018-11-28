#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

unsigned int total=0;

int calculate(string s, string w, int startw, int starts) {
    if(starts==w.length()) {
        return 1;
    }
    for(int m=startw; m<s.length(); m++) {
        if(s[m] == w[starts]) {
            total += calculate(s, w, m+1,  starts+1);
            if(total > 60000) {
                total -= 60000;
            }
        }
    }
    return 0;
}

int main(int argc, char *argv[])
{
    ifstream fin("file.in");
    if(!fin) {
        cout << "Error: FileNotFound 'file.in'";
        system("PAUSE");       
        return -1;
    }
    ofstream fout("file.out");
    string s;
    getline (fin, s);
    int t;
    stringstream(s) >> t;
    string WELC = "welcome to code jam";
    for(int i=0; i<t; i++) {
        getline (fin, s);
        if(s.length() < 18) {
            fout << "Case #" << i+1 << ": " << "0000" << endl;
            continue;
        }
        total=0;
        calculate(s, WELC, 0, 0);
        if(total > 9999) {
            total = total % 10000;
        }
        fout << "Case #" << i+1 << ": " << setw(4) << setfill('0') << total << endl;
    }
    fin.close();
    fout.close();
    return 0;
}


