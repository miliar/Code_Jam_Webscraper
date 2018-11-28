#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <cmath>
#include <functional>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <numeric>
#include <utility>
#include <cfloat>

using namespace std;

typedef long long int64_t;

template <typename T, int N>
inline size_t length_of(T(&)[N]) throw() { return N; }


struct Trip {
    Trip(int departure, int arrival): departure(departure), arrival(arrival) {}

    int departure;
    int arrival;
};

bool operator<(const Trip& a, const Trip& b)
{ 
    if (a.departure == b.departure)
        return a.arrival < b.arrival;
    else
        return a.departure < b.departure;
}


int main(int argc, char* argv[])
{
    int N;
    cin >> N;

    for (int n = 0; n < N; ++n) {
        vector< pair<Trip, int> > trips;
        string s;
        int T, NA, NB;
        int h0, m0, h1, m1;

        cin >> T >> NA >> NB;
        getline(cin, s);

        for (int i = 0; i < NA; ++i) {
            getline(cin, s);
            sscanf(s.c_str(), "%d:%d %d:%d", &h0, &m0, &h1, &m1);
            trips.push_back(make_pair(Trip(h0*60 + m0, h1*60 + m1), 0));
        }

        for (int i = 0; i < NB; ++i) {
            getline(cin, s);
            sscanf(s.c_str(), "%d:%d %d:%d", &h0, &m0, &h1, &m1);
            trips.push_back(make_pair(Trip(h0*60 + m0, h1*60 + m1), 1));
        }

        sort(trips.begin(), trips.end());

        vector<int> ready(trips.size(), false);
        int result[] = {0, 0};

        for (int i = 0; i < trips.size(); ++i) {
            if (ready[i]) continue;

            ready[i] = true;
            ++result[trips[i].second];

            int time = trips[i].first.arrival + T;
            int dir = trips[i].second ^ 1;

            for (int j = i+1; j < trips.size(); ++j) {
                if (!ready[j] && dir == trips[j].second && trips[j].first.departure >= time) {
                    ready[j] = true;
                    time = trips[j].first.arrival + T;
                    dir ^= 1;
                }
            }
        }

        printf("Case #%d: %d %d\n", n+1, result[0], result[1]);
    }

    return 0;
}

