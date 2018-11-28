#include <iostream>
#include <string>
using namespace std;

int N;
string s = "welcome to code jam";
int dp[25][505];
int X;

void printans(int ans);

int main() {
    string line;

    cin >> N;
    getline(cin,line);
    for (X = 1; X <= N; X++) {
        getline(cin,line);
        for (int i = 0; i <= line.length(); i++)
            dp[0][i] = 1;
        for (int i = 1; i <= s.length(); i++)
            dp[i][0] = 0;

        for (int i = 1; i <= s.length(); i++)
            for (int j = 1; j <= line.length(); j++) {
                dp[i][j] = dp[i][j-1];
                if (line[j-1] == s[i-1])
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % 10000;
            }

        cout << "Case #" << X << ": ";
        printans(dp[s.length()][line.length()]);
        cout << endl;
    }

    return 0;
}

void printans(int ans) {
    string sout;
    for (int i = 0; i < 4; i++) {
        sout = (char)((ans%10)+'0') + sout;
        ans /= 10;
    }
    cout << sout;
}
