/**********************************************************************
Author: cominde
Created Time: Saturday, July 26, 2008 AM09:03:15 CST
File Name: files/code/a.cpp
**********************************************************************/
#include <iostream>

using namespace std;

int n;
const int range = 1010;
int a[range], b[range];

int cmp (const int &a, const int &b) {
    return a > b;
}

int main () {
    freopen ("a.out", "w", stdout);
    int t;
    int c = 1;
    scanf ("%d", &t);
    while (t--) {
        scanf ("%d", &n);
        for (int i = 0; i < n; i++)
            scanf ("%d", &a[i]);
        for (int i = 0; i < n; i++)
            scanf ("%d", &b[i]);
        sort (a, a + n);
        sort (b, b + n, cmp);
        long long sum = 0;
        for (int i = 0; i < n; i++)
            sum += (long long)a[i] * (long long)b[i];
        printf ("Case #%d: %lld\n", c++, sum);
    }
    return 0;
}
    
        
    



