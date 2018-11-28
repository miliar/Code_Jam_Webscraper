#include <iostream>
using namespace std;

int a[1001], b[1001];

int main()
{
    int t;
    cin >> t;
    for(int ca = 1; ca <= t; ca++) {
        int n, ret = 0;
        cin >> n;
        for(int i = 0; i < n; i++) {
            cin >> a[i] >> b[i];
            for(int k = 0; k < i; k++) {
                if ((a[k] < a[i] && b[k] > b[i]) || (a[k] > a[i] && b[k] < b[i])) {
                    ret++;
                }
            }
        }
        printf("Case #%d: %d\n", ca, ret);
    }
}
