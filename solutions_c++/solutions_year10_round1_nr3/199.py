#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <queue>

#define FOR(i,a,b) for(int i = a; i <= b; i++) 
#define DOWN(i,a,b) for(int i = a; i >= b; i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define FR(i,a) for(int i = 0; i < a; i++)
#define REP(i,a) for(int i = 0; i < a; i++)
#define Rep(i,a) for(int i = 0; i < a; i++)
#define For(i,a,b) for(int i = a; i <= b; i++)

#define sqr(x) (x)*(x)
#define dout debug && cout 
#define ll long long
#define sz size()
#define ull unsigned long long
#define pb push_back
#define oo 1000000002
/* DEBUGGING */
bool debug = false;
/* MAIN PROGRAM */

using namespace std;int check(int i,int j)
{
    
    if (i == j) return 0;
    if (!i) return 1;
    if (!j) return 1;
    if (i % j == 0) return 1;
    if (j % i == 0) return 1;
    if (i > j)
    {
        int delta = i / j;
        if (delta >= 2) return 1;
        return 1-check(i-j,j);
    }
    int delta = j / i;
    if (delta >= 2) return 1;
    return 1-check(j-i,i);
}
int main()
{ 
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest,A1,B1,A2,B2;
    cin >> ntest;
    FOR(test,1,ntest)
    {
        cout << "Case #" << test << ": ";
        cin >> A1 >> A2 >> B1 >> B2;
        int res = 0;
        FOR(i,A1,A2)
        FOR(j,B1,B2) if (check(i,j)) res++;
        cout << res << endl;
    }
    /*
    F[1] = 1;
    F[0] = 1;
    FOR(i,2,35) F[i] = F[i-1] + F[i-2];
    cout << F[35];
    cout << 1 << " " << 1 << endl;
    FOR(i,2,40)
    {
    }
    
    memset(g,-1,sizeof(g));
    FOR(i,2,1000)
    {
        int first = oo,last = -oo;
        FOR(j,1,1000)
        {
            if (!visit(i,j)) first = min(first,j),last =max(last,j);
        }
        cout << i << " " << first << endl;
    }
    */
    /*
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest)
    {
        cout << "Case #" << test << ": ";
        cin >
    }
    
    */
    return 0;
}
