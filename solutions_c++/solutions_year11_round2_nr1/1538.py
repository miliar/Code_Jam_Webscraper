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
#include <set> // s.insert(elem) -- s.find(elem) != s.end()
using namespace std;

#define MAX_LINE 10000
#define ARRSIZE 1000

bool dbg = false;

#define DBG if( dbg )
#define LOOP(var,f,t) for( var=f; var<t; var++ )
#define FOR(var,f,t) for( var=f; var<t; var++ )
#define loop(var,n)   LOOP(var,0,n)
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define CLEAR(a)  memset( a, 0, sizeof(a) )

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

void chomp( char *line ) {
    if ( line != 0 )
        while ( strlen(line) > 0 && line[strlen(line)-1] == '\n' )
            line[strlen(line)-1] = 0;
}

#define N 100

int cache[N][N];

void clear_cache()
{
    int i, j;
    REP( i, N ) REP( j, N ) cache[i][j] = -1;
}

double wp( int a[N][N], int i, int op, int n )
{
    int j;
    int total = 0;
    int won = 0;
    double res = 0;

    if ( op >= 0 && cache[i][op] >= 0 )
        res =  cache[i][op];
    else
    {
        REP( j, n )
        {
            if ( i == j ) continue;
            if ( op == j ) continue;
            if ( a[i][j] >= 0 )
            {
                total++;
                if ( a[i][j] == 1 )
                    won++;
            }
        }
        res = (double) won / (double) total;
    }

    DBG cout << "   wp i " << i << " op " << op << " = " << res << endl;
    return res;
}

double owp( int a[N][N], int i, int n )
{
    int j;

    double sum = 0.0;
    int num = 0;

    REP( j, n )
    {
        if ( i == j ) continue;
        if ( a[i][j] >= 0 )
        {
            sum += wp( a, j, i, n );
            num++;
        }
    }

    DBG cout << "        owp i " << i << " = " << (double) sum / (double) num << endl;
    return sum / num;
}

double oowp( int a[N][N], int i, int n )
{
    int j;

    double sum = 0.0;
    int num = 0;

    REP( j, n )
    {
        if ( i == j ) continue;
        if ( a[i][j] >= 0 )
        {
            sum += owp( a, j, n );
            num++;
        }
    }

    DBG cout << "             oowp i " << i << " = " << (double) sum / (double) num << endl;
    return sum / num;
}

double rpi( int a[N][N], int i, int n )
{
    return 0.25 * wp( a, i, -1, n ) + 0.5 * owp( a, i, n ) + 0.25* oowp(a, i, n );
}

void doAll( int caseno )
{
    int i, j, k;
    /*
    char line[MAX_LINE];
    fgets(line,MAX_LINE,stdin); chomp(line);
    */

    string line;
    int nelements;

    int a[N][N];
    scanf("%d",&nelements);
    getline( cin, line );

    clear_cache();
    REP( i, nelements )
    {
        getline( cin, line );
        DBG cout << "Lei line. '" << line << "'\n";

        REP( j, line.size())
        {
            if ( line[j] == '.' )
                a[i][j] = -1;
            else
                a[i][j] = line[j] - '0';
        }
    }

    cout << "Case #" << caseno << ":";
    REP( i, nelements )
    {
        printf( "\n%.12lf", rpi( a, i, nelements ) );
    }

    /*
    int arr[ARRSIZE];
    int n = line2arr( (char*)line.c_str(), arr, ARRSIZE );
    DBG cout << "Array has " << n << " elements\n";
    */

    // Answer for this case
    // cout << answer;
    cout << "\n";
}

int main( int argc, char* argv[] ) {
    // freopen("sample.txt","r",stdin);
    // freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
    // freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
    // freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

    if ( argc != 1 ) dbg = true;

    int ncases,i;
    string line;

    scanf("%d",&ncases);
    getline( cin, line );
    DBG cout << "ncases = " << ncases << "\n";
    REP(i,ncases) doAll(i+1);

    return 0;
}

