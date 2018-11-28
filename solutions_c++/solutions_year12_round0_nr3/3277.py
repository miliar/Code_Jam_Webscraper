#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

set < pair < int, int > > st;
vector < int > v[1 << 21];

int A, B;


int toint ( string x ){
    int res = 0;

    for ( int i = 0; i < x.size(); ++i )
        res =res * 10 + x[i];

    return res;
}

vector < int > all ( int x ){
    vector < int > res;
    string t;
    int tx = x;

    while ( x  ){
        t += ( x % 10 );
        x /= 10;
    }
    reverse ( t.begin(), t.end() );

    for ( int i = 1; i < t.size(); ++i ){
        string s = t.substr ( i ) + t.substr ( 0, i );
        if ( s[0] != 0 ){
            int cur = toint ( s );
            if ( cur != tx )
                res.push_back ( cur );
        }
    }

    vector < int > :: iterator it = unique ( res.begin(), res.end() );
    res.resize( it - res.begin() );

    return res;
}
void init(){
    for ( int i = 1; i <= 2000000; ++i )
        v[i] = all ( i );
}

void scan(){
    cin >> A >> B;
}

void solve ( int cs ){
    int res = 0;

  //  cout << v[13].size() << endl;
    for ( int i = A; i <= B; ++i ){
        for ( int j = 0; j < v[i].size(); ++j )
            if ( A <= v[i][j] && B >= v[i][j] ){
    //                cout << i << " " << v[i][j] << endl;
                    ++res;
            }

    }

    cout << "Case #" << cs << ": " << res / 2<< endl;
}
int main(){
    init();
    int tests;

    cin >> tests;

    for ( int i = 1; i <= tests; ++i ){
        scan();
        solve(i);
    }
}
