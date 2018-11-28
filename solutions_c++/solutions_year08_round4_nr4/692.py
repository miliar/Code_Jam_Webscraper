#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <cmath>
#include <algorithm>
using namespace std;

#define SZ(X) (int)X.size()
#define pb(X,Y) X.push_back(Y)


/*class  {
public:

};*/


int main() {
    int N;
    cin >> N;
    int num;
    for( num = 0; num < N; num++ ) {
        int k;
        cin >> k;
        char S[50010];
        cin >> S;
        int len = strlen(S);
        int a[16];
        int i,j;
        for( i = 0; i < k; i++ ) a[i] = i;
        int res = 10000000;
        do {
            char B[50010];
            B[len] = '\0';
            for( i = 0; i < len; i += k ) {
                for( j = 0; j < k; j++ ) {
                    B[i+j] = S[i+a[j]];
                }
            }
            int tmp = 1;
            char pre = B[0];
            for( i = 1; i < len; i++ ) {
                if( pre != B[i] ) {
                    tmp++;
                    pre = B[i];
                }
            }
            if( tmp < res ) res = tmp;
        } while( next_permutation(a,a+k) );
        printf("Case #%d: %d\n",num+1,res);
    }
    system("pause");
    return 0;
}
