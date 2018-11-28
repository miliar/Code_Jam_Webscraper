#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    
    cin >> N >> ws;
    for (int testcase = 1; testcase <= N; ++testcase) {
        string line;
        getline(cin, line);
        int S = atoi(line.c_str());
        map<string, int> server;
        for (int i = 0; i < S; ++i) {
            getline(cin, line);
            server[line] = i;
        }
        
        int ans = 0, count = 0;
        vector<char> flag(S, false);
        getline(cin, line);
        int Q = atoi(line.c_str());
        for (int i = 0; i < Q; ++i) {
            getline(cin, line);
            if (!flag[server[line]]) {
                flag[server[line]] = true;
                ++count;
                if (count == S) {
                    ++ans;
                    flag.assign(S, false);
                    flag[server[line]] = true;
                    count = 1;
                }
            }
        }
        
        cout << "Case #" << testcase << ": " << ans << endl;
    }
    
    return 0;
}
