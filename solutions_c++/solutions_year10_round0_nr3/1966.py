#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <complex>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
typedef complex<double> tComp;

struct Group {
    LL npersons;
    int index_prev;
    // index + 1 is the rides from starting from this position
    // the content at index is how many persons are transported
    // in index + 1 rides
    vector<LL> npersonsrode;

    Group() : npersons(0), index_prev(-1), npersonsrode() {
    }

};

ostream &operator<<(ostream &os, const Group &g) {
    os << "npersons: " << g.npersons
       << " index_prev: " << g.index_prev
       << " npersonsrode: ";
    copy(g.npersonsrode.begin(), g.npersonsrode.end(),
         ostream_iterator<LL>(os, " "));
    cout << endl;

    return os;
}

Group groups[1000];

int main(int argc, char **argv) {
//      freopen("C.in","r",stdin);

//        freopen("C-small-attempt0.in","r",stdin);
//        freopen("C-small-attempt0.out","w",stdout);

//      freopen("C-small-attempt1.in","r",stdin);
//      freopen("C-small-attempt1.out","w",stdout);

//     freopen("C-small-attempt2.in","r",stdin);
//     freopen("C-small-attempt2.out","w",stdout);

     freopen("C-large.in","r",stdin);
     freopen("C-large.out","w",stdout);

//      freopen("C-large-test1.in","r",stdin);
//      freopen("C-large-test1.out","w",stdout);

    int ntestcases = 0;
    scanf("%d\n", &ntestcases);

    int testcase = 0;
    while (testcase < ntestcases) {

        int R = 0;
        int k = 0;
        int N = 0;
        scanf("%d %d %d\n", &R, &k, &N);

        string line;
        getline(cin, line);

        istringstream is(line);


        for (int i = 0; i < N; ++i) {
            groups[i] = Group();
            is >> groups[i].npersons;
        }

        LL money = 0;
        bool circle = false;
        int curr_group_index = 0;
        int prev_group_index = -1;
        int ride = 0;
        for (ride = 0; ride < R && !circle; ++ride) {
            int n_on_ride = 0;
            int curr_group = groups[curr_group_index].npersons;
            int start_group_index = curr_group_index;
            int cap = k - curr_group;
            int personsrode = 0;
            // fill rollercoaster car
            while (cap >= 0 && n_on_ride < N) {
                personsrode += curr_group;
                money += curr_group;
                curr_group_index = (curr_group_index + 1) % N;
                ++n_on_ride;
                curr_group = groups[curr_group_index].npersons;
                cap -= curr_group;
            }
            // remember this ride
            groups[start_group_index].index_prev = prev_group_index;
            groups[start_group_index].npersonsrode.push_back(personsrode);

            // recursively add this ride to all previous remembered rides too
            int i = prev_group_index;
            while (i != -1) {
                if (!groups[i].npersonsrode.empty()) {
                    groups[i].
                        npersonsrode.push_back(*(groups[i].npersonsrode.end() - 1) + personsrode);
                }
                i = groups[i].index_prev;
            }

//             cout << groups[start_group_index];

            prev_group_index = start_group_index;

            if (!groups[curr_group_index].npersonsrode.empty()) {
                circle = true;
            }
        }

//          for (int i = 0; i < N; ++i) {
//              cout << groups[i];
//          }

        if (circle && ride < R) {
            LL persons_per_circle = *(groups[curr_group_index].npersonsrode.end() - 1);
            LL rides_per_circle = groups[curr_group_index].npersonsrode.size();
            LL rides_left = R - ride;
//             cout << rides_left;
//             cout << money;
            LL n_full_circles = rides_left / rides_per_circle;
            LL rest_rides = rides_left % rides_per_circle;
            money += n_full_circles * persons_per_circle;
            if (rest_rides > 0) {
                money += groups[curr_group_index].npersonsrode[rest_rides - 1];
            }
        }

        cout << "Case #" << (testcase + 1) << ": " << money << endl;

        ++testcase;
    }

    return 0;
}
