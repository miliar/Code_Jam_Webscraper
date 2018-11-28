/* File:   a.cpp
 * Author: Venkatesh
 * Created on 21 May, 2011, 9:51 PM
 * Powered by NetBeans 6.9
 */
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>
#include <cassert>
#include <utility>
#include <functional>
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

FILE *fi = freopen("large", "r", stdin);
FILE *fo = freopen("large.out", "w", stdout);

int main()
{
    int t = GI;
    
    for( int cas=1; cas<=t; cas++ )
    {
        int r=GI, c=GI;
        vector<string> in;
        string str;

        for( int i=0; i<r; i++ )
        {
            cin >> str;
            in.pb(str);
        }

        bool err = 0;
        for( int i=0; i<r; i++ )
        {
            for( int j=0; j<c; j++ )
            {
                if( in[i][j] == '#' )
                {
                    if( (j+1<c && in[i][j+1]=='#') && (i+1<r && in[i+1][j]=='#') && (in[i+1][j+1]=='#') )
                    {
                        in[i][j] = '/';
                        in[i][j+1] = '\\';
                        in[i+1][j] = '\\';
                        in[i+1][j+1] = '/';
                    }
                    else
                    {
                        err =1;
                        break;
                    }
                }
            }
            if( err )
                break;
        }

        cout << "Case #" << cas << ":" << endl;
        if( err )
            cout << "Impossible" << endl;
        else
        {
            for( int i=0; i<r; i++ )
            cout << in[i] << endl;
        }
    }

    return 0;
}
