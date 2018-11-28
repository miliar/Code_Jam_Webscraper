#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <cstdio>
#include <fstream>
using std::vector;
using std::map;
using std::pair;
using std::make_pair;
using std::cout;
using std::cin;
using std::endl;
using std::set;
using std::string;
using std::ifstream;
using std::ofstream;


int main() {
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");

    int T;
    fin >> T;

    for(int t = 0; t < T; t++) {
        long long R, k, N;
        fin >> R >> k >> N;

        vector<int> groups;

        for(int g = 0; g < N; g++) {
            int tmp;
            fin >> tmp;
            groups.push_back(tmp);
        }


        int index = 0;

        vector<int> nextIndex(N);
        vector<int> profit(N);

        // generate number of groups and profit for each possible queue
        for(int n = 0; n < N; n++) {
            int spaceLeft = k;
            index = n;

            // fill up coaster
            for(int i = 0; i < N; i++) {
                if(groups[index] > spaceLeft) break;
                spaceLeft -= groups[index];
                index++;
                index %= N;
            }

            profit[n] = k-spaceLeft;
            nextIndex[n] = index;
        }


        long long ans = 0;
        index = 0;
        for(int r = 0; r < R; r++) {
            ans += profit[index];

            index = nextIndex[index];
        }

        fout << "Case #" << t+1 << ": " << ans << endl;
        cout << t << endl;

    }
    fin.close();
    fout.close();

    return 0;
}
