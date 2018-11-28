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

int badsum( int a, int b )
{
    int i, s = 0;
    int p = 0;
    while( a != 0 || b != 0 )
    {
        s += ((( a % 2 ) + ( b % 2 )) % 2 ) << p;
        // cout << a << " " << b << " " << s << endl;
        p++;
        a >>= 1;
        b >>= 1;
    }

    return s;
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
    getline( cin, line );

    getline( cin, line );
    DBG cout << "Lei line. '" << line << "'\n";

    int arr[1000];
    int n = line2arr( (char*)line.c_str(), arr, 1000 );
    DBG cout << "Array has " << n << " elements\n";

    std::sort( arr, arr + n );

    int bits[1000];
    REP(i,1000) bits[i] = 0;

    int bitpos = 0;
    int bitval = 0;

    REP(i,n)
    {
        int num = arr[i];
        bitpos = 0;
        while( num != 0 )
        {
            bitval = num % 2;
            num >>= 1;
            bits[bitpos] += bitval;
            bitpos++;
        }
    }

    int posible = 1;
    REP(i,bitpos) 
    {
        DBG cout << "bits[" << i << "] is " << bits[i] << endl;
        if( bits[i] % 2 != 0 )
        {
            DBG cout << "bits[" << i << "] is " << bits[i] << endl;
            posible = 0;
        }
    }

    // Answer for this case
    cout << "Case #" << caseno << ": ";
    if( posible == 0 )
    {
        cout << "NO";
    }
    else
    {
        // posible, find solution then
        int realsum = 0;
        int lastgood = 0;
        int fakesum = 0;
        int fakesum2 = 0;
        int found = 0;
        int j;
        LOOP( i, 0, n-1 )
        {
            realsum += arr[n-i-1];
            fakesum = badsum( arr[n-i-1], fakesum );
            // cout << "i: " << i << " val: " << arr[n-i-1] << " sum:" << realsum << endl;
            fakesum2 = 0;
            REP( j, n-i-1 )
            {
                fakesum2 = badsum( fakesum2, arr[j] );
                // cout << "j " << j << " " << arr[j] <<  " -> " << fakesum2 << endl;
            }

            // cout << "fake vs fakesum " << fakesum << " " << fakesum2 << endl;
            if( fakesum == fakesum2 )
            {
                // cout << realsum;
                lastgood = realsum;
                found = 1;
            }
        }

        if( found == 0 )
        {
            cout << "NO";
        }
        else
        {
            cout << lastgood;
        }
    }

    // cout << answer;
    cout << "\n";
}

int main( int argc, char* argv[] ) {
    // freopen("candy.in", "r",stdin);
    // freopen("A-smll-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
    // freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
    // freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

    if ( argc != 1 ) dbg = true;

    int ncases,i;
    string line;

    /*
    cout << "bad(5,4) " << badsum(5,4) << endl;
    cout << "bad(7,9) " << badsum(7,9) << endl;
    cout << "bad(50,10) " << badsum(50,10) << endl;
    */
    scanf("%d",&ncases);
    getline( cin, line );
    DBG cout << "ncases = " << ncases << "\n";
    REP(i,ncases) doAll(i+1);

    return 0;
}

