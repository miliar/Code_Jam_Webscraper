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

int main(void)
{
    int T, N, i, j, k;
    int mn, sum, xr;
    
    cin >> T;
    for(int caso=1; caso<=T; caso++) {
        cin >> N;
        mn=999999999, sum=0, xr=0;
        for(i=0; i<N; i++) {
            cin >> k;
            if(k<mn) mn=k;
            sum += k;
            xr ^= k;
        }
        
        cout << "Case #" << caso << ": ";
        
        if(xr) cout << "NO\n";
        else cout << sum-mn << endl;
    }
}
