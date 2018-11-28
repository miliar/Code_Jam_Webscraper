#include <iostream>
#include <set>
#include <queue>
#include <algorithm>
#include <stack>
using namespace std;

int main () {
    int test;
    cin >> test;
    int N, PD, PG;
    for(int cases = 1; cases <= test; ++cases) {
        cin >> N >> PD >> PG;
        
        cout << "Case #" << cases << ": ";
        // tim T1
        int t = 0;
        for(int i = 1; i <= N; ++i) {
            if((PD*i)%100 == 0) {
                //int d1 = PD*i/100;
                //int minT2 = d1*100/b;
                // tim T2
                //for(int j = max(i, minT2); 
                t = 1; 
                break;
            }
        }
        if(PD != 100 && PG == 100) {
            t = 0;
        }
        else if(PD == 0 && PG != 100) {
            t = 1;
        }
        else if(PD != 0 && PG == 0) {
            t = 0;
        }
        
        if(t == 1) {
            cout << "Possible" << endl;
        }
        else {
            cout << "Broken" << endl;
        }
    }
}
