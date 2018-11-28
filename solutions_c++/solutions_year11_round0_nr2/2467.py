#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <set>
#include <utility>

using namespace std;


vector < char > elementi;
set < pair <char, char> > suprotni;
map < pair <char, char>, char> kombinacije;

char postojiKomb(char a, char b) {
    map <pair <char, char>, char>::iterator it = kombinacije.find(make_pair(a, b));
    if(it != kombinacije.end())
        return (*it).second;
    it = kombinacije.find(make_pair(b, a));
    if(it != kombinacije.end())
        return (*it).second;
    return '#';
}

string ispisi() {
    if(elementi.empty()) return string("[]");
    string s;
    s = "[";
    for(int i=0; i<elementi.size()-1; ++i) {
        char elem[2] = {elementi[i]};
        s += string(elem) + ", ";
    }
    char elem[2] = {elementi[elementi.size()-1]};
    s += string(elem) + "]";
    return s;
}

int main() {

    ofstream out;
    out.open ("B-large.out");
    ifstream in;
    in.open("B-large.in");


    int t;
    in >> t;
    for(int i=0; i<t; ++i) {

        elementi.clear();
        suprotni.clear();
        kombinacije.clear();

        int c;
        in >> c;
        for(int j=0; j<c; ++j) {
            string s;
            in >> s;
            kombinacije.insert(make_pair(make_pair(s[0], s[1]), s[2]));
        }

        int d;
        in >> d;
        for(int j=0; j<d; ++j) {
            string s;
            in >> s;
            suprotni.insert(make_pair(s[0], s[1]));
            suprotni.insert(make_pair(s[1], s[0]));
        }

        int n;
        in >> n;
        string s;
        in >> s;
        for(int j=0; j<n; ++j) {
            char ch = s[j];
            elementi.push_back(ch);

            if(elementi.size() >= 2) {
                int n = elementi.size();
                char rez = postojiKomb(elementi[n-1], elementi[n-2]);
                if(rez != '#') {
                    elementi.erase(elementi.end()-1);
                    elementi[n-2] = rez;
                }

                else {
                    for(int i=0; i<n-1; ++i) {
                       if(suprotni.find(make_pair(elementi[n-1], elementi[i])) != suprotni.end()) {
                        elementi.clear();
                       }
                    }
                }
            }
        }

        out << "Case #" << (i+1) << ": " << ispisi() << endl;


    }

    return 0;
}
