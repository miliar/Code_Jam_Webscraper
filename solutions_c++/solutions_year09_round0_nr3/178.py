#include <iostream>
#include <string>
#include <vector>
using namespace std;

const char WELCOME[] = "welcome to code jam";
const size_t LEN = sizeof(WELCOME) / sizeof(WELCOME[0]) - 1;

string normalize(size_t number) {
    string result("    ");
    for (size_t i = 0; i < 4; ++i) {
        result[3 - i] = ((number % 10) + '0');
        number /= 10;
    }
    return result;
}

int main() {
    size_t N;
    cin >> N;
    cin.ignore();
    for (size_t cases = 1; cases <= N; ++cases) {
        string data;
        getline(cin, data);
        vector< vector<size_t> > has_data(data.size(), vector<size_t>(LEN, false));
        vector< vector<size_t> > dp(data.size(), vector<size_t>(LEN, 0));
        for (size_t i = 0; i < data.size(); ++i) {
            for (size_t j = 0; j < LEN; ++j) {
                if (data[i] == WELCOME[j]) {
                    if (j == 0) {
                        has_data[i][j] = true;
                        dp[i][j] = 1;
                    } else {
                        for (size_t k = i; k != -1; --k) {
                            if (has_data[k][j - 1]) {
                                dp[i][j] += dp[k][j - 1];
                                dp[i][j] %= 10000;
                                has_data[i][j] = true;
                            }
                        }
                    }
                }
            }
        }
        size_t answer = 0;
        for (size_t k = data.size() - 1; k != -1; --k) {
            if (has_data[k][LEN - 1]) {
                answer += dp[k][LEN - 1];
                answer %= 10000;
            }
        }
        cout << "Case #" << cases << ": " << normalize(answer) << endl;
    }
    return 0;
}
