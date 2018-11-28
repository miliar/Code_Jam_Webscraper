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
    int r,c;
    unsigned char a[50][50];

    REP( i, 50 ) REP( j, 50 ) a[i][j] = 0;

    scanf("%d%d",&r,&c);
    getline( cin, line );

    int count = 0;
    REP( i, r )
    {
        getline( cin, line );
        // DBG cout << "linea = " << line << endl;
        REP( j, c )
        {
            a[i][j] == 0;
            if ( line[j] == '#' )
            {
                a[i][j] = 1;
                // DBG cout << "tile malo en " << i << "," << j << endl;
                count++;
            }
        }
    }

    // recorrer intentando reemplazar los 1 por 0s
    // solo intentar solucionar si count es multiplo de 4
    if ( count % 4 == 0 )
    {
        REP( i, r-1 )
        {
            REP( j, c-1 )
            {
                if ( a[i][j] == 1 )
                {
                    if ( a[i][j+1] == 1 && a[i+1][j] == 1 && a[i+1][j+1] == 1 )
                    {
                        DBG cout << "Encuentro y reemplazo aqui " << i << "," << j << endl;
                        count -= 4;
                        a[i][j] = '/';
                        a[i+1][j] = a[i][j+1] = '\\';
                        a[i+1][j+1] = '/';
                    }
                }
            }
        }
    }

    /*
    int arr[ARRSIZE];
    int n = line2arr( (char*)line.c_str(), arr, ARRSIZE );
    DBG cout << "Array has " << n << " elements\n";
    */

    // Answer for this case
    cout << "Case #" << caseno << ": ";
    // cout << answer;
    if ( count > 0 )
        cout << "\nImpossible";
    else
    {
        REP( i, r )
        {
            cout << endl;
            REP( j, c )
            {
                if ( a[i][j] == 0 )
                    cout << ".";
                else
                    cout << a[i][j];
            }
        }
    }
    cout << endl;
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

