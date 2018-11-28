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

int di[] = {1, -1, 0, 0, 1, -1, 1, -1};
int dj[] = {0, 0, 1, -1, 1, -1, -1, 1};
int diK[] = {-2, -2, -1, 1, 2, 2, 1, -1};
int djK[] = {-1, 1, 2, 2, 1, -1, -2, -2};

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
typedef pair < char, int > PCI;
typedef vector < PCI > VP;
// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;
const ld INF = (1 << 9);
const ld PHI = (sqrt(5.0) + 1) / 2.0;

int main() {
    //    ifstream in( "input.txt" );
    //    ofstream out( "output.txt" );
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    cout << setiosflags(ios::fixed) << setprecision(10);

    int case_number = 0, T = 1;
    int ans = 0;
    scanf("%d", &T);
    while (T--) {

          int q;
        cin >> q;
        int o[100], b[100], no = 0, nb = 0;
        char c;
        VP vec;
        PCI p;
        for (int i = 0; i < q; i++) {
            //            cin >> c;
            //            if( c == 'O' )
            //            {
            //                cin >>o[no++];
            //            }
            //            else
            //            {
            //                cin >> b[no++];
            //            }
            cin >> p.first;
            cin >> p.second;
            if( p.first == 'O' )
                o[no++] = p.first;
            else
                b[nb++] = p.second;
            
            vec.push_back(p);
        }

        int time = 0,otime=0,ptime=0;
        int po = 1, pbb = 1;
        int turn = -1;
        int oo=0,bb=0;

        VP::iterator itr;
        for (itr = vec.begin(); itr != vec.end(); itr++) {
            p = *itr;
            if (p.first == 'O')
                turn = 1;
            else {
                turn = 2;
            }
            if( turn == 1 )
            {
                if( abs( p.second - po ) > ( time - otime ) )
                {
                    time += abs( p.second - po ) - ( time - otime ) + 1;
                }
                else
                {
                    time++;
                }
                po = p.second;
                otime = time;
            }
            else
            {
                if( abs( p.second - pbb ) > ( time - ptime ) )
                {
                    time += abs( p.second - pbb ) - ( time - ptime ) + 1;
                }
                else
                {
                    time++;
                }
                pbb = p.second;
                ptime = time;
            }

        }

        iout << time << endl;

    }

    return 0;
}

