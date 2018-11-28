#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string welcome = "welcome to code jam";
    int len = welcome.size();
    int N;
    {
        string n_s;
        getline(cin, n_s);
        N = atoi(n_s.c_str());
    }
    for (int i = 0; i < N; ++i) {
        string line;
        getline(cin, line);
        vector< int > count(len);
        for (string::iterator it = line.begin(); it != line.end(); ++it) {
            for (int j = 0; j < len; ++j) {
                if (welcome[j] == *it) {
                    count[j] = (count[j] + (j == 0 ? 1 : count[j - 1])) % 10000;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " 
             << setfill('0') << setw(4) << count[len - 1] << "\n";
    }
}

