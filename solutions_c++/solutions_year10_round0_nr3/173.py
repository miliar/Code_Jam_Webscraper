#include <iostream>
#include <vector>

using namespace std;



int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        long long runCount, rollerCap, groupCount;
        cin >> runCount >> rollerCap >> groupCount;

        vector<int> g(groupCount);
        for(int i=0; i<groupCount; i++) cin >> g[i];

        vector<int> next(g.size());
        vector<long long> nexttook(g.size());

        for(int i=0; i<g.size(); i++) {
            int pos=i;
            long long took = 0;
            while(true)
            {
                if (took + g[pos] > rollerCap) break;

                took += g[pos];
                pos = (pos + 1) % groupCount;
                if (pos == i) break;
            }

            next[i] = pos;
            nexttook[i] = took;
        }

        int pos=0;
        long long ans =0;
        for(int i=0; i<runCount; i++)
        { 
            ans += nexttook[pos];
            pos = next[pos];
        }
        cout << "Case #" <<(c+1) << ": " << ans << endl;
    }
}
