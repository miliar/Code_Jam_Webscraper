#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> dict;

struct Pattern
{
    vector<string> posi;

    bool isOK(string & str)
    {
        for (int i = 0; i < str.length(); ++i) {
            bool find = false;
            for (int j = 0; j < posi[i].length(); ++j)
                if (posi[i][j] == str[i])
                    find = true;
            if (!find) return false;
        }
        return true;
    }

    Pattern(string & str)
    {
        string now = "";
        int state = 0;
        for (int i = 0; i < str.length(); ++i) {
            if (str[i] == '(') {
                state = 1;
                continue;
            }
            if (str[i] == ')') {
                if (now.length() > 0) 
                    posi.push_back(now);
                now = "";
                state = 0;
                continue;
            }

            if (state == 0) {
                posi.push_back(string(1, str[i]));
            }
            if (state == 1) {
                now += string(1, str[i]);
            }
        }
    }
};

int main()
{
    int L, D, tests;
    string line;
    cin >> L >> D >> tests;
    getline(cin, line);

    for (int i = 0; i < D; ++i) {
        getline(cin, line);
        dict.push_back(line);
    }

    for (int i = 0; i < tests; ++i) {
        getline(cin, line);
        Pattern pattern(line);
        int answer = 0;
        for (int j = 0; j < dict.size(); ++j)
            if (pattern.isOK(dict[j]))
                answer++;
        printf("Case #%d: %d\n", i + 1, answer);
    }
}


