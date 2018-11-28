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
#define CLEARL(a,len)  std::fill(&arr[0], &arr[len], 0 )

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

void doAll( int caseno )
{
    int i, j, k;
    /*
    char line[MAX_LINE];
    fgets(line,MAX_LINE,stdin); chomp(line);
    */

    string line;
    int nelements;
    int n,l,h;
    int a[100];

    REP( i, 100 ) a[i] = 0;

    scanf( "%d%d%d", &n, &l, &h );
    REP( i, n )
    {
        scanf( "%d", &a[i] );
    }

    // Answer for this case
    cout << "Case #" << caseno << ": ";

    int note = 0;
    int puede = 0;
    FOR( i, l, h+1 )
    {
        puede = 1;
        REP( j, n )
        {
            if( (a[j] % i != 0) && (i % a[j] != 0) )
            {
                puede = 0;
                break;
            }
        }
        if( puede )
        {
            note = i;
            break;
        }
    }
    if( puede )
        cout << note;
    else
        cout << "NO";

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

