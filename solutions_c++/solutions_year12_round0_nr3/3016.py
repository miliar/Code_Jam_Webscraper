#include <iostream>
#include <vector>
using namespace std;

vector<int> pairs[2000000+1];

void generate(int n = 2000000) {
    int n_nums = 1;
    int n_next = 10;
    int n_curr = 1;
    for (int i = 1; i <= n; ++i) {
        if (i >= n_next) {
            ++n_nums;
            n_curr = n_next;
            n_next *= 10;
        }
        int num = i;
        for (int j = 0; j < n_nums-1; ++j) {
            int dig = num % 10;
            num = num / 10 + n_curr*dig;
            if (dig > 0 && num > i)
                pairs[i].push_back(num);
        }
    }
}

void solve(int tc) {
    int a,b;
    cin >> a >> b;

    int sum = 0;
    for (int i = a; i <= b; ++i)
        for (int j = 0; j  < pairs[i].size(); ++j)
            sum += int(pairs[i][j] <= b);
    cout << "Case #" << tc << ": " << sum << "\n";
}

int main() {
    generate();
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
        solve(t+1);
    return 0;
}
