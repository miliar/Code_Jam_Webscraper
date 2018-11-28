#include <iostream>
#include <cstring>

#include <algorithm>
#include <vector>

using namespace std;

struct point_pair{
    int x;
    int y;
};

bool myfunction (point_pair i,point_pair j) { return (i.x<j.x); }

vector<point_pair> pairs;
vector<point_pair>::iterator it, it2;

int main() {
    int T, N, i, j, k, x, y;
    cin >> T;
    point_pair p;
    for(i= 1; i <= T; i++) {
        cin >> N;
        pairs.erase(pairs.begin(), pairs.end());
        for(j= 1; j <= N; j++) {
            cin >> p.x >> p.y;
            pairs.push_back(p);
        }
        sort(pairs.begin(), pairs.end(), myfunction);
        int sum= 0;
        for(it= pairs.begin(); it != pairs.end(); it++) {
            for(it2= pairs.begin(); it2 != it; it2++) {
                if (it2->y > it->y ) sum++;
            }
        }

        cout << "Case #" << i << ": " << sum << endl;
    }
    return 0;
}
