// Candy Splitting

#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <assert.h>
using namespace std;

int readint() {
    int x;
    cin >> x;
    return x;
}

int abs(int x) {
    return (x > 0) ? x : -x;
}
int max(int x, int y) {
    return (x > y) ? x : y;
}

int main() {
    int T = readint();
    for(int t=0;t<T; t++) {
        int N = readint();

        vector<int> n;

        for(int i =0;i<N;i++)
            n.push_back( readint() );

        int tot = 1 << N;
        int bestMy = -1;
        for(int i = 0; i< tot; i++) {
            int my = i;
            int his = tot - 1 - i;

            if ((my == 0) || ( his == 0) )
                continue;

            int hisSum = 0, mySum = 0;
            int hisXor = 0, myXor = 0;

            for(int j = 0; j<N;j++) {
                int flag = 1 << j;
                if (my & flag) {
                    //MY
                    mySum += n[j];
                    myXor ^= n[j];
                }else {
                    // HIS
                    hisSum += n[j];
                    hisXor ^= n[j];
                }
            }
            if (hisXor == myXor) {
                // cout << my << " Xor: " << myXor << " : mysum " << mySum << " hisSum " << hisSum << endl;
                bestMy = max( bestMy, mySum );
            }
        }
        int result = bestMy;
        cout << "Case #" << t+1 << ": " ;
        if (result < 0)
            cout << "NO";
        else
            cout << result;
        cout << endl;
    }
    return 0;
}
