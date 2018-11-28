#include <iostream>
#include <fstream>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

string sin="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvzq";
string sout="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upqz";

char conv[27];
bool mark[27];
int main() {
    for( int i=0; i<sin.size(); i++ ) {
            if( sin[i] != ' ' ) {
                conv[sin[i]-'a'] = sout[i];
                //mark[ sout[i]-'a' ] = true;
            }
    }

    /*
    for( int i=0; i<26; i++ ) {
            if( conv[i] == 0 ) cout << char(i+'a') << endl;
            if( !mark[i] ) cout << char(i+'a') << endl;
    }
    */
    int T;
    string clear;
    in >> T;
    getline( in, clear );
    for (int tcase = 1; tcase <= T; tcase++ ) {
        string line, ans="";
        getline(in,line);
        for( int i=0; i<line.size(); i++ ) {
            if( line[i] != ' ' ) ans += conv[ line[i]-'a' ];
            else ans += ' ';
        }
        out << "Case #" << tcase << ": " << ans << endl;
    }
    return 0;
}


