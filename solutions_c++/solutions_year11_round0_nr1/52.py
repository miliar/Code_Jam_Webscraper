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
    ifstream ifs( "A-large.in" );
    string strbuf;
    getline(ifs, strbuf);
    int test = atoi(strbuf.c_str());
    for ( int i = 0; i < test; i++ ) {
        getline(ifs, strbuf);
        istringstream iss(strbuf);

        int N;
        iss >> N;
        vector<pair<string,int> > v;
        for ( int j = 0; j < N; j++ ) {
            string str; int sw;
            iss >> str >> sw;
            v.push_back(make_pair(str,sw));
        }

        int posO = 1, posB = 1, sum = 0, w = 0;
        bool prevO = false;
        for ( int j = 0; j < v.size(); j++ ) {
            if ( v[j].first == "O" ) {
                int move = abs(v[j].second-posO);
                if ( prevO ) {
                    int add = move + 1;
                    sum += add;
                    w += add;
                    posO = v[j].second;
                } else {
                    int add = max( 0, move-w ) + 1;
                    sum += add;
                    w = add;
                    posO = v[j].second;
                }
                prevO = true;
            } else {
                int move = abs(v[j].second-posB);
                if ( !prevO ) {
                    int add = move + 1;
                    sum += add;
                    w += add;
                    posB = v[j].second;
                } else {
                    int add = max( 0, move-w ) + 1;
                    sum += add;
                    w = add;
                    posB = v[j].second;
                }
                prevO = false;
            }
        }


        printf( "Case #%d: %d\n", i+1, sum );

    }
    return 0;   
}
