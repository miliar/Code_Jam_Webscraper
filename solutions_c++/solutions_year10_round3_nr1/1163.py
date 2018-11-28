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
#include <set>
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

struct point
{
    int a, b;
    void print() {
        cout << "a: " << a << " b: " << b << "\n";
    }

    bool intersect( point p2 )
    {
        return (a < p2.a && b > p2.b) ||
               (a > p2.a && b < p2.b);
    }
};

bool compare( point p1, point p2 )
{
    return p1.a <= p2.a;
}

void doAll( int caseno )
{
    int i, j, k;
    /*
    char line[MAX_LINE];
    fgets(line,MAX_LINE,stdin); chomp(line);
    */

    int N;
    scanf( "%d", &N );
    DBG cout << "N: " << N << endl;

    vector<point> v;
    bool ready[1000][1000];
    REP( i, 1000 ) REP( j, 1000 ) ready[i][j] = false;

    REP( i, N ) {
        int A, B;

        scanf( "%d%d", &A, &B );
        point p;
        p.a = A;
        p.b = B;
        v.push_back(p);
        DBG cout << "  A: " << A << " B: " << B << endl;
    }
    DBG cout << "sorted vector " << endl;
    sort( v.begin(), v.end(), compare );
    REP( i, v.size() ) {
        DBG v[i].print();
    }

    int s = 0;
    REP( i, N ) REP( j, i ) {
        DBG cout << "trying " << i << " " << j << endl;
        s += v[i].intersect( v[j] );
    }
    /*
    int arr[10];
    int n = line2arr( line, arr, 10 );
    DBG cout <<( "Array has " << n "elements\n";
    */

    // Answer for this case
    cout << "Case #" << caseno << ": ";
    cout << s;
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
    // getline( cin, line );
    DBG cout << "ncases = " << ncases << "\n";
    REP(i,ncases) doAll(i+1);

    return 0;
}

