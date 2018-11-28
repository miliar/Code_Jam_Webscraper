
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

string solve(string s) {
    vector <int> ind;
    for(int i = 0; i < s.size(); i++)
        if(s[i] == '?')
            ind.push_back(i);

    int n = ind.size();
    for(int i = 0; i < (1 << n); i++) {
        for(int j = 0; j < n; j++) {
            if(i & (1 << j))
                s[ind[j]] = '1';
            else
                s[ind[j]] = '0';
        }
        long long num = 0;
        for(int j = 0; j < s.size(); j++)
            num = (num << 1) + (s[j] - '0');

        long long m = sqrt(1.0 * num + 0.5);
        if(m * m == num)
            return s;
    }
    return "";
}

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        string s;
        cin >> s;
        cout << "Case #" << i+1 << ": " << solve(s) << endl;
    }
}
