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

FILE *fi = freopen("small.in", "r", stdin);
FILE *fo = freopen("small.out", "w", stdout);

int main()
{
    int t = GI;
    
    for( int cas=1; cas<=t; cas++ )
    {
        int n=GI, lo=GI, hi=GI;
        vector<int> v(n);

        for( int i=0; i<n; i++ )
            cin >> v[i];

        bool flag = 0;
        int ans = 0;
        for( int i=lo; i<=hi; i++ )
        {
            int cnt = 0;
            for( int j=0; j<n; j++ )
            {
                if( (i<=v[j] && v[j]%i==0) || (i>v[j] && i%v[j]==0) )
                    cnt++;
            }

            if( cnt == n )
            {
                flag = 1;
                ans = i;
                break;
            }
        }

        cout << "Case #" << cas << ": ";
        if( flag )
            cout << ans << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}
