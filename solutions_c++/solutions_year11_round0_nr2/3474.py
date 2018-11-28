#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

const int MAXN = 300;
char comb[MAXN][MAXN];
bool opp[MAXN][MAXN];

int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        for( int i=0; i<MAXN; i++ )
            for( int j=0; j<MAXN; j++ ) {
                comb[i][j] = '!';
                opp[i][j] = false;
            }

        int C, D, N;
        in >> C;
        for( int i=0; i<C; i++ ) {
            string temp;
            char a, b, c;
            in >> temp;
            a = temp[0], b=temp[1], c=temp[2];
            comb[a][b] = comb[b][a] = c;
        }

        in >> D;
        for( int i=0; i<D; i++ ) {
            string temp;
            char a, b;
            in >> temp;
            a = temp[0], b=temp[1];
            opp[a][b] = opp[b][a] = true;
        }

        vector<char> str;
        in >> N;
        //cout << "N:" << N << endl;
        for( int i=0; i<N; i++ ) {
            char a;
            in >> a;
            //cout << a << endl;
            //try to combine
            if( str.size() > 0 && comb[a][str.back()] != '!' ) {
                char temp = comb[a][str.back()];
                str.pop_back();
                str.push_back( temp );
            }
            else {
                str.push_back(a);
                //see if opposed
                for( int j=0; j<str.size()-1; j++ ) {
                    if( opp[str[j]][str.back()] ) {
                        str.clear();
                        break;
                    }
                }
            }
        }

        out << "Case #" << test << ": [";
        for( int i=0; i<str.size(); i++ ) {
            if( i+1<str.size() ) out << str[i] << ", ";
            else out << str[i];
        }
        out << "]" << endl;

    }

    return 0;
}



