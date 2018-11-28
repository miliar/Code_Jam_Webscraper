#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int main() {
    int N, S, Q, P;
    string s;
    cin >> N;
    getline(cin, s);

    for ( int c = 0; c < N; c++ ) {
        vector<string> v;
        P = 0;
        getline(cin, s);
        istringstream is1(s);
        is1 >> S;

        for ( int i = 0; i < S; i++ )
            getline(cin, s);

        getline(cin, s);
        istringstream is2(s);
        is2 >> Q;
        for ( int i = 0; i < Q; i++ ) {

            getline(cin, s);
            vector<string>::iterator result;
            result = find( v.begin(), v.end(), s );

            if( result == v.end() ) {
                v.push_back(s);
            }

            if ( v.size() == S ) {
                P++;
                v.clear();
                v.push_back(s);
            }
        }
        cout << "Case #" << c+1 << ": " << P << endl;
    }
    return 0;
}
