/* 2009 Google Code Jam Qualification Round
 * Problem C: Welcome to Code Jam
 *
 * Coded by Lapro
 * Sep. 3, 2009
 */

#include <iostream>
#include <string>
#include <sstream>
using namespace std;
const string pattern("welcome to code jam");
int f[1000][20];

void calc(string& str){
    int n = str.size();
    int m = 19;
    memset(f, 0, sizeof(f));
    for(int i = 0; i <= n; ++ i)
        f[i][0] = 1;
    for(int i = 1; i <= n; ++ i)
        for(int j = 1; j <= m; ++ j){
            if (str[i - 1] == pattern[j - 1])
                f[i][j] = (f[i][j] + f[i - 1][j - 1]) % 10000;
            f[i][j] = (f[i][j] + f[i - 1][j]) % 10000;
        }
    cout.fill('0');
    cout.width(4);
    cout << f[n][m] << endl;
}

int main(){
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w+", stdout);
    string input_str;
    int N;
    cin >> N;
    getline(cin, input_str);
    for(int i = 0; i < N; ++ i){
        getline(cin, input_str);
        printf("Case #%d: ", i + 1);
        calc(input_str);
    }
    return 0;
}
