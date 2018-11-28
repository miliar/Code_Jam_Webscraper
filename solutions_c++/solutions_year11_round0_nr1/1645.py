#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <map>

#define PII pair<int, int>
#define MP make_pair
#define PB push_back
#define X first
#define Y second

using namespace std;

int mmax(int a, int b) { return (a>b)?a:b; }

int main(void)
{
    int T, n, k, i, j;
    
    cin >> T;
    
    PII a[110];
    int tim[110];
    
    for(int caso=1; caso<=T; caso++) {
        cin >> n;
        
        
        for(i=0; i<n; i++) {
            string rob;
            int b;
            cin >> rob >> b;
            if(rob == "O") a[i] = MP(0,b);
            else a[i] = MP(1,b);
        }
        
        int ol=-1, bl=-1;
        
        for(i=0; i<n; i++) {
            int t;
            if(a[i].X == 0) {
                // Orange
                if(ol < 0) t = a[i].Y;
                else t = tim[ol] + abs(a[ol].Y-a[i].Y) + 1;
                
                if(bl >= 0) {
                    t = mmax(t, tim[bl]+1);
                }
                
                ol = i;
            } else {
                // Blue
                if(bl < 0) t = a[i].Y;
                else t = tim[bl] + abs(a[bl].Y-a[i].Y) + 1;
                
                if(ol >= 0) {
                    t = mmax(t, tim[ol]+1);
                }
                
                bl = i;
            }
            tim[i] = t;
        }
        
        cout << "Case #" << caso << ": " << tim[n-1] << endl;
    }
    
    return 0;
}
