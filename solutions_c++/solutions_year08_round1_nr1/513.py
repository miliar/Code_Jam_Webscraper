// author: hken 
#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <memory.h>

using namespace std;

#define LL                  long long
#define pb                  push_back
#define mp                  make_pair
typedef vector <int>        vi;
typedef vector <string>     vs;
typedef pair   <int, int>   pii;

int n;
LL a[1000],b[1000];

void input()
{
    int i;

    cin >> n;
    for (i=0; i<n; i++) cin >> a[i];
    for (i=0; i<n; i++) cin >> b[i];
}

LL process()
{
    int i;
    LL res = 0;

    sort(a,a+n); 
    sort(b,b+n);
    
    for (i=0; i<n; i++) res += a[i]*b[n-i-1];
    return res;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int i,j,numTest;
    char buf[201];
    
    // get numTest
    cin >> numTest;
    for (i=0; i<numTest; i++)
    {
        // input
        input();

        // output
        cout << "Case #" << (i+1) << ": " << process() << endl;
    }
    return 0;
}
