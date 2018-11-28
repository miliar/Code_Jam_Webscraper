#include <fstream>
#include <string>
using namespace std;

ifstream in("A-small.in");
ofstream out("A-small.out");

int N;
string A[50];

int solve() {
    int cnt = 0;
    int L[50];
    
    for (int i = 0; i < N; ++i) {
        L[i] = -1;
        for (int j = 0; j < N; ++j)
            if (A[i][j] == '1')
                L[i] = j;
    }
    
    for (int i = 0; i < N; ++i) {
        for (int j = i; j < N; ++j)
            if (L[j] <= i) {
                int tmp = L[j];
                for (int k = j; k > i; --k)
                    L[k] = L[k - 1];
                L[i] = tmp;
                cnt += (j - i);
                break;
            }
    }
    
    return cnt;
}

int main() {
    int T;
    in >> T;
    for (int t = 1; t <= T; ++t) {
        in >> N;
        for (int i = 0; i < N; ++i)
            in >> A[i];
        out << "Case #" << t << ": " << solve() << "\n";
    }
    return 0;
}
