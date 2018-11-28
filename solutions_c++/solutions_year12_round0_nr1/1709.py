#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

#define SZ(a) (int)(a).size()
#define REP(i,n) for(int i=0;i<(int)(n);++i)

int rm[26];

void init() {
    string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
               "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
               "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string d = "our language is impossible to understand"
               "there are twenty six factorial possibilities"
               "so it is okay if you want to just give up";
    for (int i = 0; i < SZ(s); i++)
        if (s[i] != ' ')
            rm[s[i]-'a'] = d[i]-'a';
    rm['q'-'a'] = 'z'-'a';
    rm['z'-'a'] = 'q'-'a';
}

int main(int argc, char const *argv[]) {
    init();
    ifstream in ("A-small-attempt0.in");
    ofstream out ("A-small-attempt0.out");

    int n;
    string s;

    in >> n;
    getline(in,s);
    REP(i, n) {
        getline(in,s);
        out << "Case #" << i+1 << ": ";
        REP(j,SZ(s))
            if (s[j] == ' ') out << ' ';
            else out << (char)(rm[s[j]-'a']+'a');
        out << endl;
    }
    return 0;
}
