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

int rabs( int n )
{
     if( n <= 0 )
         n = -n;

     return n;
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

    scanf("%d",&nelements);
    // cout << "nelems: " << nelements << endl;

    getline( cin, line );

    DBG cout << "Lei line. '" << line << "'\n";

    istringstream s(line);

    int pos[2] = { 1, 1 };
    int currpos = -1;
    int curridx = -1;
    int previdx = -1;
    int t = 0;
    int total = 0;
    int need = 0;

    REP( i, nelements ) {
        char texto[3];
        int n;
           s >> texto;
           s >> n;

           // cout << "texto: '" << texto << "' " ;
           // cout << "n: " << n << endl;

           switch( texto[0] ) 
           {
               case 'O':
                   curridx = 0;
                   break;
               case 'B':
                   curridx = 1;
                   break;
           }

           currpos = pos[curridx];
           // sigue moviendose el mismo robot
           if( previdx == curridx || curridx == -1 )
           {
               int mueve = rabs( n - currpos );
               total += mueve + 1;  // 1 seg en presionar boton
               t += mueve + 1;
           }
           // le toca moverse al otro
           else
           {
               need = abs( n - currpos );
               // hubo tiempo suficiente para moverse al objetivo
               if( need <= t )
               {
                   t = 1;
               }
               else
               {
                   t = need - t + 1;
               }
               total += t;
           }
           pos[curridx] = n;

           previdx = curridx;

   }
    /*
    int arr[ARRSIZE];
    int n = line2arr( (char*)line.c_str(), arr, ARRSIZE );
    DBG cout << "Array has " << n << " elements\n";
    */

    // Answer for this case
    cout << "Case #" << caseno << ": ";
    cout << total;
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

