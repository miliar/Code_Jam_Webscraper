#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <list>
#include <stack>
#include <deque>
#include <numeric>
#include <fstream>
#include <iterator>

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define INF (1<<29)

using namespace std;

int run(int ncase){
    int i, j, k;
    int N, K, B, T;
    

    cin >> N >> K >> B >> T;
    
    vector<int> x(N);
    vector<int> v(N);
    
    FOR(i, N) cin >> x[i];
    FOR(i, N) cin >> v[i];
    
    reverse(x.begin(), x.end());
    reverse(v.begin(), v.end());
    
    int out = 0;
    int swap = 0;
    int remain = K;
    FOR(i, N){
        if((x[i] + v[i] * T) >= B){
            swap += out;
            remain--;
        }else{
            out++;
        }
        if( remain == 0 ) break;
        
    }
    // cout << out << ":" <<  swap << ":" << remain << endl;
    cout << "Case #" << ncase << ": ";
    if( remain == 0) cout << swap << endl;
    else cout << "IMPOSSIBLE" << endl;
    return 0;
}

int main() {
    int i, test_set;
    cin >> test_set;
    FOR(i, test_set) run(i+1);
    return 0;
}
