#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    ifstream ifs( "B-large.in" );
    string strbuf;
    getline(ifs, strbuf);
    int test = atoi(strbuf.c_str());
    for ( int i = 0; i < test; i++ ) {
        getline(ifs, strbuf);
        istringstream iss(strbuf);

        int C = 0, D = 0, N;
        iss >> C;
        vector<string> cstr, dstr;
        for ( int j = 0; j < C; j++ ) {
            string s;
            iss >> s;
            cstr.push_back(s);
        }

        iss >> D;
        for ( int j = 0; j < D; j++ ) {
            string s;
            iss >> s;
            dstr.push_back(s);
        }

        iss >> N;
        string str;
        iss >> str;

        vector<char> s;
        for ( int j = 0; j < str.size(); j++ ) {
            s.push_back(str[j]);
            if ( j == 0 ) continue;

            if ( s.size() > 1 ) {
                for ( int k = 0; k < cstr.size(); k++ ) {
                    if ( s.back() == cstr[k][0] && s[s.size()-2] == cstr[k][1] ||
                         s.back() == cstr[k][1] && s[s.size()-2] == cstr[k][0] ) {
                             s.pop_back();s.pop_back();
                             s.push_back(cstr[k][2]);
                    }
                }
            }

            if ( s.size() > 1 ) {
                for ( int k = 0; k < dstr.size(); k++ ) {
                    if ( find(s.begin(), s.end(), dstr[k][0]) != s.end() &&
                         find(s.begin(), s.end(), dstr[k][1]) != s.end() ) {
                             s.clear();
                             break;
                    }

                }
            }
        }

        printf( "Case #%d: [", i+1 );
        for ( int j = 0; j < s.size(); j++ ) {
            if ( j == s.size()-1 ) printf("%c", s[j]);
            else printf("%c, ", s[j]);
        }
        puts("]");


    }
    return 0;   
}
