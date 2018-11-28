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

int n,m;
map<string,int> a;
string q[1000];

int process()
{
    int i,j,k,res = 0;
    int c[100];

    if (m==0) return 0;

    i = 0;
    while (i<m)
    {
        res++;

        for (j=0; j<n; j++) c[j] = INT_MAX;
        for (j=i; j<m; j++) { k = a[q[j]]; c[k] = min(c[k],j); }

        i = -1;
        for (j=0; j<n; j++) if (i < c[j]) i = c[j];
    }

    return res-1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int i,j,numTest;
    char buf[201];
    
    // get numTest
    cin.getline(buf, 200); sscanf(buf, "%d", &numTest);
    
    for (i=0; i<numTest; i++)
    {
        // input
        cin.getline(buf, 200); sscanf(buf, "%d", &n);
        for (j=0; j<n; j++) { cin.getline(buf, 200); a[string(buf)] = j; }
        cin.getline(buf, 200); sscanf(buf, "%d", &m);
        for (j=0; j<m; j++) { cin.getline(buf, 200); q[j] = string(buf); }

        // output
        cout << "Case #" << (i+1) << ": " << process() << endl;
    }
    return 0;
}
