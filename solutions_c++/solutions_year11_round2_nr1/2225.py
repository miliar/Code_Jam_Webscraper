/* Jai swaminarayan!!!
 * File:   TaskA.cpp
 * Author: CIA(Indraraj)
 *
 *
 */

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define Repie(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Repde(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define Repi(i, n) for(int i=0; i<(int)(n); i++)
#define Repd(i, n) for(int i=(n)-1; i>=0; i--)
#define Fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define print case_number++, printf("Case #%d: ",case_number), printf
#define iout case_number++, printf("Case #%d: ",case_number), cout

template <class _T> inline _T sqr(const _T& x) {
    return x * x;
}

template <class _T> inline string tostr(const _T& a) {
    ostringstream os("");
    os << a;
    return os.str();
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

// Types
typedef long double ld;
typedef signed long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;
const ld INF = ( 1<<10) ;
const ld PHI = ( sqrt( 5.0 ) + 1 ) / 2.0;

int main() {
    //    ifstream in( "input.txt" );
    //    ofstream out( "output.txt" );
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    cout << setiosflags(ios::fixed) << setprecision(10);

    int case_number = 0,T = 1;
    int ans = 0;
    scanf( "%d", &T );
    while( T-- )
    {
        int n;
        cin >> n;
        char a[100][100];

        for (int i = 0; i < n; i++) {
            cin >> a[i];

        }
        ld wp[100];

        for (int i = 0; i < n; i++) {
            ld won=0,total=0;
            for (int j = 0; j < n; j++) {
                if( a[i][j] != '.' )
                    total++;
                if( a[i][j] == '1' )
                {
                    won++;
                }

            }
            if( total != 0 )
            wp[i] = ( won/total );
//            cout << wp[i] << endl;
        }

        ld owp[100];
        for (int i = 0; i < n; i++) {
            ld ttotal=0,count=0;
            for (int j = 0; j < n; j++) {
                if( a[i][j] != '.' )
                {
                    count++;
                    ld won=0,total=0;
                    for (int k = 0; k < n; k++) {
                        if( i == k )
                            continue;
                        if( a[j][k] == '1' )
                            won++;
                        if( a[j][k] != '.' )
                            total++;

                    }
                    if( total != 0 )
                    ttotal += (won/total);
                }
                
            }
            if( count != 0 )
            owp[i] = ttotal/count;
        }

        ld oowp[100];
        for (int i = 0; i < n; i++) {
            ld total=0,count=0;
            for (int j = 0; j < n; j++) {
                if( a[i][j] != '.' )
                {
                    total+=owp[j];
                    count++;
                }

            }
            if( count != 0 )
            oowp[i] = (total/count);

        }


        iout << endl;
        for (int i = 0; i < n; i++) {
            cout << ( 0.25 * wp[i] ) + ( 0.5 * owp[i] ) + ( 0.25 * oowp[i] ) << endl;


        }


//        iout << T << endl;
    }

    return 0;
}

