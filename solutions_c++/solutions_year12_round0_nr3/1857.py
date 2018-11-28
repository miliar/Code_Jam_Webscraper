#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

int main()
{
    const int pow10[] = {1,10,100,1000,10000,100000,1000000,10000000,100000000};
    int n, A, B;
    cin >> n;
    for ( int i = 0; i < n; i++ ) {
        cin >> A >> B;
        int ans = 0;
        for ( int j = A; j <= B; j++ ) {
            int d;
            for ( d = 1; pow10[d] <= j; d++ );
            set<int> s;
            for ( int k = 1; k < d; k++ ) {
                int x = j%pow10[k]*pow10[d-k] + j/pow10[k];
                if ( x >= A && x <= B && x > j ) ans+=s.insert(x).second;
            }
        }
        printf("Case #%d: %d\n", i+1, ans);
    }

    return 0;
}