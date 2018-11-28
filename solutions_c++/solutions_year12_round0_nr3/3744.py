#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>

using namespace std;

string intToStr(int x) {
    string ans = "";
    while (x) {
        ans = (char)('0' + x % 10) + ans;
        x /= 10;
    }
    return ans;        
}

int strToInt(string s) {
    int ans = 0;
    for (size_t index = 0; index < s.length(); ++index) 
        ans = 10 * ans + (s[index] - '0');
    return ans;
}

map<string, int> STI;
vector<string> ITS(2000000 + 1);
vector<int> cycles[2000000 + 1];

int calc(int A, int B) {
    int ans = 0;
    for (int m = A + 1; m <= B; ++m) {
        for (size_t jndex = 0; jndex < cycles[m].size(); ++jndex) {
            int t = cycles[m][jndex];
            if (t >= A && t <= B)
                ++ans;
        }
    }
    return ans;
}

int main() {
    for (int i = 1; i <= 2000000; ++i) {
        string s = intToStr(i);
        STI[s] = i;
        ITS[i] = s;
    }

    for (int m = 1; m <= 2000000; ++m) {
        set<int> numbers;
        string s = ITS[m];
        for (size_t jndex = 0; jndex < s.length(); ++jndex) {
            char c = s[0];
            s = s.substr(1);
            s += c;
            int t = STI[s];
            if (t < m)
                numbers.insert(t);
        }
        set<int>:: iterator it = numbers.begin();
        while (it != numbers.end()) {
            cycles[m].push_back(*it);
            ++it;
        }
    }

    int testsCount;
    cin >> testsCount;
    for (size_t test = 1; test <= testsCount; ++test) {
        int A, B;
        cin >> A >> B;
        cout << "Case #" << test << ": " << calc(A, B) << endl;
    }
    return 0;
}
