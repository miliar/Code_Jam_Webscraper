#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int p(string s, const vector <string>& dict)
{
    int n = 0;
    for (int i = 0; i < dict.size(); ++i)
    {
        bool flag = true;
        for (int j = 0, k = 0, m = 0, f = 0; j < dict[i].size(); ++k)
        {
            if (j >= dict[i].size() || k >= s.size())
            {
                flag = false;
                break;
            }
            if (s[k] == '(')
            {
                m = true;
                continue;
            }
            if (s[k] == ')')
            {
                m = false;
                if (!f)
                {
                    flag = false;
                    break;
                }
                f = false;
                continue;
            }
            if (f)
                continue;
            if (m && s[k] == dict[i][j])
            {
                ++j;
                f = true;
                continue;
            }
            if (!m && s[k] == dict[i][j])
            {
                ++j;
                continue;
            }
        }
        n += flag;
    }
    return n;
}

int main(int argc, char** argv)
{
    int L, D, N;
    ifstream in(argv[1]);
    in >> L >> D >> N;
  
    vector <string> words;
    for (int i = 0; i < D; ++i)
    {
        string t;
        in >> t;
        words.push_back(t);
    }

    vector <string> tests;
    for (int i = 0; i < N; ++i)
    {
        string t;
        in >> t;
        tests.push_back(t);
    }

    ofstream out(argv[2]);

    for (int i = 0; i < tests.size(); ++i)
        out << "Case #" << (i + 1) << ": " << p(tests[i], words) << endl;

    return 0;
}
