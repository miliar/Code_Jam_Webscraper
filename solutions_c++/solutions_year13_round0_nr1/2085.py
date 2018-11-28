#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <ctype.h>  // isdigit(), isalnum(), isalpha()
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <numeric>
#include <set> // s.insert(elem) -- s.find(elem) != s.end()
using namespace std;

// read functions
// readint
#define READF(thetype,format,thename)  thetype thename()  { thetype x; scanf(format,&x); return x;}

READF(int,"%d",ri)
READF(double,"%lf",rd)
READF(float,"%f",rf)

#define MAX_LINE 10000
#define ARRSIZE 1000

bool dbg = true;

#define DBG if( dbg )

#define FOR(var,f,t) for(var=(f); var!=(t); ++var)
#define REP(i,n) FOR(i,0,n)

#define fi(limit) REP(i,limit)
#define fj(limit) REP(j,limit)
#define fk(limit) REP(k,limit)

#define FORSTL(it,n)  for(typeof(x.begin()) it = x.begin(); it != x.end(); it++ )
#define all(v)   v.begin(), v.end()

#define pb push_back

#define CLEAR(arr,value)  memset(arr,value,sizeof(arr))
#define ARR(T,a,n)   T a[n]; CLEAR(a,0);

// "3 4 5" ->  { 3, 4, 5 }
// returns the array size
// size should be big enough
template <class T>
int line2arr( char* line, T* arr, int max_size )
{
    int n = 0;
    if ( line != NULL ) {
        istringstream s(line);
        T v;
        while ( s >> v ) {
            arr[n++] = v;
        }
    }
    return n;
}

    // string line;

    //getline( cin, line );
    //DBG cout << "Lei line. '" << line << "'\n";

    /*
    int arr[ARRSIZE];
    int n = line2arr( (char*)line.c_str(), arr, ARRSIZE );
    DBG cout << "Array has " << n << " elements\n";
    */


template <typename T> string a2s( T start, T stop, bool quote=false ) {
    ostringstream os;
    os << "{";
    string comma = "";
    for (T iter = start; iter != stop; ++iter) {
        os << comma << ' ' ;
        if(quote) { os << '\"' << *iter << "\""; }
        else      { os << *iter; }
        // os << ',';
        comma = ",";
    }
    os << " }";
    return os.str();
}

void reopen_io( bool redir = true )
{
    // freopen("sample.txt","r",stdin);
    // freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
    // freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
    // freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

    if( redir ) {
        freopen( "input.txt", "r", stdin );
        // freopen( "output.txt", "w", stdout );
    }
}

bool winsX(int sum) {
    return sum == 130 || sum == 40;
}

bool winsO(int sum) {
    return sum == 103 || sum == 4;
}

void doAll()
{
    int i, j, k, n;
    
    int a[4][4];
    int colsum[4];
    CLEAR(colsum,0);

    string line;

    getline( cin, line );

    int count0 = 0;
    bool winX = false;
    bool winO = false;

    int diag1 = 0;
    int diag2 = 0;

    fi(4) { 
        getline(cin,line); 
        // cout << " line " << line << endl;
        fj(4) {
            char c = line[j];
            switch(c) {
                case 'T': a[i][j] = 100; break;
                case 'X': a[i][j] = 10; break;
                case '.': a[i][j] = 0; ++count0; break;
                case 'O': a[i][j] = 1; break;
            }
            colsum[j] += a[i][j];
            // cout << "colsum = " << a2s(colsum,colsum+4) << endl;
            if( i == j ) diag1 += a[i][i];
            if( i+j == 3) diag2 += a[i][j];
        }
        // cout << a2s(a[i],a[i]+4) << endl;
        int rowsum = accumulate( a[i], a[i]+4, 0);
        // cout << "rowsum = " << rowsum << endl;
        if( winsX(rowsum) ) { winX = true; }
        else
        if( winsO(rowsum) ) { winO = true; }
    }

    if( !winX && !winO && count0 > 0 ) {
        // CHECK COLS 
        fi(4) {
            // cout << "colsum[" << i << "] = " << colsum[i]<< endl;
            if( winsX(colsum[i]) ) { winX = true; }
            else
            if( winsO(colsum[i]) ) { winO = true; }
        }

        if( winsX(diag1) || winsX(diag2)) { winX = true; }
        else
        if( winsO(diag1) || winsO(diag2)) { winO = true; }

    }

    if( winX ) cout << "X won";
    else if( winO ) cout << "O won";
    else if( count0 == 0 ) cout << "Draw";
    else cout << "Game has not completed";

    // getline( cin, line );
    // cout << a2s(arrd,arrd+n);
    // cout << endl;

    // cout << answer;
    cout << endl;
}



int main( int argc, char* argv[] ) {

    reopen_io();

    if ( argc != 1 ) dbg = true;

    int i;
    string line;

    int ncases = ri();

    // DBG cout << "ncases = " << ncases << "\n";
    REP(i,ncases) {
        cout << "Case #" << (i+1) << ": ";
        doAll();
    }

    return 0;
}

