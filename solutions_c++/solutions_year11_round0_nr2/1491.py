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
#define loop(var,n)   LOOP(var,0,n)
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

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

char comb[256][256];
char destroy[256][256];

void doAll( int caseno )
{
    int i, j, k;

    REP(i,256) REP(j,256) { comb[i][j] = 0; destroy[i][j] = 0; }
    /*
    char line[MAX_LINE];
    fgets(line,MAX_LINE,stdin); chomp(line);
    */

    string line;
    int nelements;
    char texto[3];
    char frase[128];
    char result[128];

    scanf("%d",&nelements);

    getline( cin, line );

    DBG cout << "Lei line. '" << line << "'\n";

    istringstream s(line);

    REP( i, nelements )
    {
        s >> texto;
        // cout << "Encontre creation: '" << texto << "'" <<endl;
        comb[texto[0]][texto[1]] = texto[2];
        comb[texto[1]][texto[0]] = texto[2];
    }

    s >> nelements;

    REP( i, nelements )
    {
        s >> texto;
        // cout << "Encontre destroy: '" << texto << "'" <<endl;
        destroy[texto[0]][texto[1]] = destroy[texto[1]][texto[0]] = 1;
    }

    s >> nelements;
    s >> frase;

    DBG cout << "Frase a revisar: '" << frase << "'" <<endl;

    int largofinal = 0;
    REP( i, nelements )
    {
        char c = frase[i];
        DBG cout << "Chequeando char " << c << endl;
        if( largofinal == 0 )
        {
            result[largofinal++] = c;
        }
        else
        {
            char gen = comb[result[largofinal-1]][c];
            if( gen != 0 )
            {
                result[largofinal-1] = gen;
            }
            else
            {
                // buscar si el nuevo caracter es capaz de destruir todo
                int destruye = 0;
                REP( j, largofinal )
                {
                    if( destroy[c][result[j]] )
                    {
                        largofinal = 0;
                        destruye = 1;
                        break;
                    }
                }

                if( !destruye )
                {
                    result[largofinal++] = c;
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
    cout << "[";
    REP( i, largofinal )
    {
        cout << result[i];
        if( i != largofinal-1 )
            cout << ", ";
    }
    cout << "]";
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

