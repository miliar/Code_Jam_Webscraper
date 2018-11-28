#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define VI vector<int>
#define VS vector<string>
#define VVI vector< VI >
#define PB push_back
#define ALL(a) (a).begin(), (a).end()
#define SORT(a) sort( ALL(a) )
#define IPAIR pair<int,int>
#define VIPAIR vector< IPAIR >
#define FOR(i,b,n) for ( int i = (b); i < (n); i++ )
#define REP(i,n) FOR(i,0,n)
#define ll long long

const int SIZE = 60 * 24;
int tblA[ SIZE ];
int tblB[ SIZE ];
int turn;

int toi( char* str )
{
    char buf[10];
    buf[0] = str[0];
    buf[1] = str[1];
    buf[2] = 0;
    int h = atoi( buf );
    buf[0] = str[3];
    buf[1] = str[4];
    buf[2] = 0;
    int m = atoi( buf );
    return h * 60 + m;
}



int add( int* tbl, int m, int d ) {
    int start = m;
    if ( d == 1 ) {
        start += turn;
    }
    for ( int i = start; i < SIZE; i++ ) {
        tbl[i] += d;
    }
    return 0;
}

int main()
{
    int n;
    scanf( "%d", &n );
    
    for ( int i = 0; i < n; i++ ) {
    
        memset( tblA, 0, sizeof(tblA) );
        memset( tblB, 0, sizeof(tblB) );
        
        scanf( "%d", &turn );
        int na, nb;
        scanf( "%d%d", &na, &nb );
        
        for ( int j = 0; j < na; j++ ) {
            char buf1[256], buf2[256];
            scanf( "%s%s", &buf1, &buf2 );
            int m = toi( buf1 );
            add( tblA, m, -1 );
            m = toi( buf2 );
            add( tblB, m, +1 );
        }
        
        for ( int j = 0; j < nb; j++ ) {
            char buf1[256], buf2[256];
            scanf( "%s%s", &buf1, &buf2 );
            int m = toi( buf1 );
            add( tblB, m, -1 );
            m = toi( buf2 );
            add( tblA, m, +1 );
        }
        
        int minA = 0, minB = 0;
        
        minA = *min_element( tblA, tblA + SIZE );
        minB = *min_element( tblB, tblB + SIZE );
        
        printf( "Case #%d: %d %d\n", i+1, -minA, -minB );
    }
    
    return 0;
}
