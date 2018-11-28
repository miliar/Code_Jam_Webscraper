#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <limits>
#include <map>

using namespace std; 

int main(int argc, char const *argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int m;
    cin >> m;

    for(int i = 0; i < m; ++i) {        
        int n, s, p;
        cin >> n >> s >> p;
        
        vector<int> scores(n);
        for(int j = 0; j < n; ++j)
            cin >> scores[j];

        int ans = n;
        for(int j = 0; j < n; ++j) {
            if(scores[j] > 3*(p-1))
                continue;
            // surprise
            if(s > 0) {
                if(scores[j] != 3*p-3 && scores[j] != 3*p-4 || p < 2)
                    ans -= 1;
                else
                    s -= 1;
            } else
                ans -= 1;
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }

    return 0;
}
