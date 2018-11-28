#include <iostream>
#include <vector>
using namespace std;
int calc(int P, int Q) {
    vector<int> a;
    for(int i = 0; i < Q; ++ i) {
        int nn;
        cin >> nn;
        a.push_back(nn);
    }
    sort(a.begin(), a.end());
    vector<int> b;
    int prev = 0;
    for(int i = 0; i < a.size(); ++ i) {
        b.push_back(a[i] - 1 - prev);
        prev = a[i];
    }
    b.push_back(P - prev);
    int f[110][110];
    memset(f, 0, sizeof(f));
    int n = b.size();
    vector<int> sb;
    sb.push_back(0);
    for(int i = 0; i < n; ++ i)
        sb.push_back(b[i] + sb[i]);
    /*
    for(int i = 0; i < n; ++ i)
        printf("b[%d] = %d, ", i, b[i]);
    cout << endl;
    */
    // b[i..j] = sb[j + 1] - sb[i];
    for(int j = 2; j <= n; ++ j) 
        for(int i = 0; i < n - j + 1; ++ i){
            int & ff = f[i][j];
            ff = -1;
            for(int k = 1; k < j; ++ k) {
                int temp = f[i][k] + f[i + k][j - k] + sb[i + j] - sb[i] + j - 2;
                if (ff == -1 || temp < ff) ff = temp;
            }
        }
    /*
    for(int i = 0; i < n; ++ i)
        for(int j = 0; j < n - i; ++ j)
            printf("f[%d][%d] = %d\n", i, j, f[i][j]);
            */
    return f[0][n];
}
int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w+", stdout);
    int N, P, Q;
    cin >> N;
    for(int i = 1; i <= N; ++ i){
        cin >> P >> Q;
        printf("Case #%d: %d\n", i, calc(P, Q));
    }
    return 0;
}
