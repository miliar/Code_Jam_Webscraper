#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const char iname[] = "A-large.in";
const char oname[] = "A-large.out";

int getAnswer(string dict, string pattern)
{
    int matches = 0, idx = 0;
    for (int i = 0; i < pattern.size(); ++ i, ++ idx) {
        if (pattern[i] == '(') {
            int match = false;
            while (pattern[++ i] != ')') {
                if (dict[idx] == pattern[i])
                    match = true;
            }
            if (!match)   return 0;
        }
        else {
            if (dict[idx] != pattern[i])
                return 0;
        }
    }
    return 1;
}

int main(void)
{
    ifstream in(iname);
    ofstream out(oname);
    int L, D, N;

    in >> L >> D >> N;
    vector <string> dict(D);
    for (int i = 0; i < D; ++ i)
        in >> dict[i];
    for (int i = 0; i < N; ++ i) {
        string pattern;
        in >> pattern;

        int answer = 0;
        for (int j = 0; j < dict.size(); ++ j)
            answer += getAnswer(dict[j], pattern);

        out << "Case #" << (i + 1) << ": " << answer << "\n";
    }
    in.close();
    out.close();
    return 0;
}
