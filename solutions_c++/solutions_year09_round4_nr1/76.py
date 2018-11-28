#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;


int main(void) { 
    cin.sync_with_stdio(0);

    int CASES; cin >> CASES;
    for ( int tt=1; tt<=CASES; ++tt ) { // caret here
        int N; cin >> N;
        vector<int> a(N);
        for ( int i=0; i<N; ++i ) {
            string red; cin >> red;
            int j;
            for ( j=N-1; j>0; --j ) {
                if ( red[j] == '1' ) break;
            }
            a[i] = j;
        }

        int ans = 0;
        for ( int i=0; i<N; ++i ) {
            if ( a[i] <= i ) continue;
            
            int j;
            for ( j=i+1; j<N; ++j ) {
                if ( a[j] <= i )
                    break;
            }
            ans += j-i;
            rotate(a.begin()+i, a.begin()+j, a.begin()+j+1);
        }

        cout << "Case #" << tt << ": " << ans << "\n";
    }

    return 0;
} 
