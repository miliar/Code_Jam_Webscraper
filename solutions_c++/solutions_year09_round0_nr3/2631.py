#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

static const char * input = "welcome to code jam";

int solve(string str)
{
    vector<vector<int> > cache(str.size());

    for (int i = 0; i < str.size(); i++) {
        cache[i].resize(strlen(input));
    }

    for (int i = str.size() - 1; i >= 0; i--) {
        for (int j = strlen(input) - 1; j >= 0; j--) {
            if (str[i] == input[j]) {
                if (j == strlen(input) - 1) {
                    if (i == str.size() -1) {
                        cache[i][j] = 1;
                    } else {
                        cache[i][j] = 1 + cache[i+1][j];
                    }
                } else if (i != str.size() - 1) {
                    cache[i][j] = (cache[i+1][j+1] + cache[i+1][j]) % 10000;
                } else {
                    cache[i][j] = 0;
                }
            } else if (i != str.size() - 1) {
                cache[i][j] = cache[i+1][j];
            } else {
                cache[i][j] = 0;
            }
        }
    }

    return cache[0][0];
}

int main()
{
    int n;
    cin >> n;
    string str2;
    getline(cin, str2);

    for (int i = 1; i <= n; i++) {
        string str;
        getline(cin, str);

        int num = solve(str);
        
        cout << "Case #" << i << ": " << setw(4) << setfill('0') << num << endl;
    }

    return 0;
}
