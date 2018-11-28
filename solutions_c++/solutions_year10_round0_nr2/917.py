#include <iostream>
#include <vector>
using namespace std;

int gcd(int n1, int n2)
{
    if (n2 == 0) return n1;
    else return gcd(n2, n1 % n2);
}

int main()
{
    int C;
    scanf("%d", &C);

    for (int i = 0; i < C; i++) {
        int N;
        scanf("%d", &N);
        vector<int> v;
        for (int j = 0; j < N; j++) {
            int t;
            scanf("%d", &t);
            v.push_back(t);
        }
        sort(v.begin(), v.end());
        
        vector<int> vd;
        for (int j = 0; j < N - 1; j++) {
            vd.push_back(v[j+1] - v[j]);
        }
        int n = 1;
        if (N == 2) {
            n = vd[0];
        } else {
            n = gcd(vd[0], vd[1]);
        }
        if (v[0] % n == 0) {
            printf("Case #%d: 0\n", i + 1);
        } else {
            printf("Case #%d: %d\n", i + 1, n - (v[0] % n));
        }
    }
}
