#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>
#include <cstring>

using namespace std;

#define ll          long long
#define VI          vector<int>
#define ALL(a)      (a).begin(), (a).end()
#define SORT(a)     sort( ALL(a) )
#define PB          push_back
#define FOR(i,a,b)  for( int i = (a); i < (int)(b); i++ )
#define dump_(x)     cerr << #x << " = " << (x) << " ";
#define dump(x)     cerr << #x << " = " << (x) << endl
#define dump_vec(x) FOR(zZz,0,x.size()) cout << x[zZz] << " "; cout << endl


template< typename type > type readOne()
{
    type res;
    char inp[5000];
    char* dum = fgets( inp, sizeof( inp ), stdin );
    stringstream ss( dum );
    ss >> res;
    return res;
}

template< typename type > vector<type> readMulti()
{
    vector<type> res;
    char inp[5000];
    char* dum = fgets( inp, sizeof( inp ), stdin );
    stringstream ss( dum );
    for ( type t; ss >> t; )
        res.push_back( t );
    return res;
}

//
//
// LET'S START
//
//

char check(string s) {
    int c[256] = {0};
    char x = s[0];
    FOR(i, 0, 4) {
        if (s[i] == '.') return ' ';
        c[s[i]]++;
    }
    if (c['X'] + c['T'] == 4) return 'X';
    if (c['O'] + c['T'] == 4) return 'O';
    return ' ';
}

string doCase()
{
    string res = "Draw";
    vector<string> cands;
    
    //
    // READ INPUT
    //
    string board[4];
    FOR(i, 0, 4) {
        string s;
        cin >> s;
        board[i] = s;
        cands.push_back(s);
    }

    FOR(i, 0, 4) FOR(j, 0, 4) if (board[i][j] == '.')
        res = "Game has not completed";
    
    FOR(i, 0, 4) {
        string s;
        FOR(j, 0, 4) s += board[j][i];
        cands.push_back(s);
    }

    string s, t;
    FOR(i, 0, 4) {
        s += board[i][i];
        t += board[i][3-i];
    }

    cands.push_back(s);
    cands.push_back(t);

    FOR(i, 0, cands.size()) {
        char ans = check(cands[i]);
        if (ans == 'X') return "X won";
        if (ans == 'O') return "O won";
    }

    return res;
}

int main()
{
    int cases = readOne<int>();
    for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;
    return 0;
}
