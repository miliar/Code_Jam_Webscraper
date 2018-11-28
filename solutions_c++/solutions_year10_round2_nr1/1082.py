#include<cstdio>
#include<cstdlib>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>

using namespace std;

set<string> postojeci;


int brojMkdira(const string &dir) {

    if(postojeci.find(dir) != postojeci.end()) return 0;

    string s = dir;
    postojeci.insert(dir);
    int br=1;

    while(true) {

        int pos = s.rfind("/");
        s = s.substr(0, pos);
        if(s.empty()) break;
        if(postojeci.find(s) != postojeci.end()) {
            return br;
        }
        postojeci.insert(s);
        ++br;
    }

    return br;

}
int main() {

    ifstream in;
    ofstream out;
    out.open("A-large.out");
    in.open("A-large.in");

    int t;
    in >> t;

    for(int i=0; i<t; ++i) {

        postojeci.clear();
        int n, m;
        in >> n >> m;

        for(int j=0; j<n; ++j) {
            string dir;
            in >> dir;
            postojeci.insert(dir);
        }

        int ukupno = 0;
        for(int j=0; j<m; ++j) {
            string dir;
            in >> dir;
            ukupno += brojMkdira(dir);
        }

        out << "Case #" << (i+1) << ": " << ukupno << endl;
    }

    return 0;
}
