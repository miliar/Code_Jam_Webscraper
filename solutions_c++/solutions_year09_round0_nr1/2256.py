/* File:   language.cpp
 * Author: Venkatesh
 * Created on September 3, 2009, 4:02 PM
 * Powered by NetBeans 6.5
 */
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>
#include <bitset>
#include <cctype>
#include <numeric>
#include <cstdlib>
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
#define pb push_back
#define sz size()
#define all(x) (x).begin(), (x).end()
#define GI ( { int t; scanf("%d",&t); t; } )
#define dbg(x) cout << #x << "= " << x << endl;
#define dbgg(x) cout << #x << endl;
#define eps 1e-8
#define eps1 1e-5
#define pi 2*acos(0.0)
#define mp make_pair
#define ff first
#define ss second

FILE *fi = freopen( "aLarge.in", "r", stdin );
FILE *fo = freopen( "aLarge.out", "w", stdout );

int main()
{
    int L = GI;
    int D = GI;
    int N = GI;
    getchar();

    string str;
    vector<string> dict(D);

    for( int i=0; i<D; i++ )
    {
        getline( cin, str );
        dict[i] = str;
    }

    string pattern;

    for( int caseno=1; caseno<=N; caseno++ )        // for each pattern
    {
        getline( cin, pattern );
        int index = -1;
        bool open = 0;

        vector< vector<bool> > mat( L, vector<bool>(26,0) );

        for( int i=0; i<pattern.sz; i++ )           // construct mat
        {
            if( pattern[i] == '(' )
                open = 1;
            else if( pattern[i] == ')' )
                open = 0;
            else
            {
                if( open )
                {
                    if( pattern[i-1] == '(' )
                        index++;
                }
                else
                    index++;

                mat[index][ pattern[i]-'a' ] = 1;
            }
        }

        int cnt = 0;

        for( int i=0; i<dict.sz; i++ )
        {
            bool ok = 1;

            for( int j=0; j<dict[i].sz; j++ )
            {
                if( !mat[j][ dict[i][j]-'a' ] )
                {
                    ok = 0;
                    break;
                }
            }

            if( ok )
                cnt++;
        }

        printf( "Case #%d: %d\n", caseno, cnt );
    }

    return 0;
}
