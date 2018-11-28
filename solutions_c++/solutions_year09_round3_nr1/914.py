// writen by the moving hken
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <memory.h>
#include <limits.h>

using namespace std;

#define c2d(x) ( (x)<='9' ? (x)-'0' : (x)-'a'+10 )

int numtest, len;
string a;
int c[36], b[36];
long long res;

void process()
{
     //
     int cnt = 0;
     memset(b, false, sizeof(b));
     for (int i=0; i<len; i++) b[c2d(a[i])] = true;
     for (int i=0; i<36; i++) if (b[i]) cnt++;
     if (cnt == 1) cnt = 2;
     
     //
     memset(c, -1, sizeof(c));
     c[c2d(a[0])] = 1;
     for (int i=1; i<len; i++) if (a[i] != a[0]) { c[c2d(a[i])] = 0; break; }
     for (int k=2, i=0; i<len; i++) if (c[c2d(a[i])] == -1) { c[c2d(a[i])] = k++; } 
     
     //
     res = 0;
     for (int i=0; i<len; i++) res = res*cnt + c[c2d(a[i])];
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> numtest;    
    for (int i=0; i<numtest; i++)
    {
        cin >> a; len = a.length();
        process();
        printf("Case #%d: %I64d\n", i+1, res); 
    }
    
    return 0;
}
