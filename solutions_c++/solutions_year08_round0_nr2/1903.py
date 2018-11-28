#include <iostream>
#include <vector>
#include <set>

using namespace std;

const int MAXTIME = 1500;

class Trip {
public:
    int start, end;
    int flag;

    Trip() {}
    Trip(int flag, string from, string to) {
        this->flag = flag;
        start = ((from[0]-'0')*10 + (from[1]-'0')) * 60 + (from[3]-'0')*10 + (from[4]-'0');
        end = ((to[0]-'0')*10 + (to[1]-'0')) * 60 + (to[3]-'0')*10 + (to[4]-'0');
    }

    friend bool operator<(const Trip& t1, const Trip& t2) {
        return (t1.start < t2.start || (t1.start == t2.start && t1.end < t2.end));
    }
};

int CASE = 0;

int n, t;
int na, nb;
vector<Trip> trips;

set<int> Q[2];

int main() {
    freopen("B.in", "r", stdin);
    cin >> n;
    while(n--) {
        int ans[2] = {0, 0};
        trips.clear();
        Q[0].clear(), Q[1].clear();

        cin >> t;
        cin >> na >> nb;
        for(int i = 0; i < na; i++) {
            string from, to;
            cin >> from >> to;
            trips.push_back(Trip(0, from, to));
        }
        for(int i = 0; i < nb; i++) {
            string from, to;
            cin >> from >> to;
            trips.push_back(Trip(1, from, to));
        }
        sort(trips.begin(), trips.end());

        for(int i = 0; i < trips.size(); i++) {
            if(Q[trips[i].flag].size() > 0 && *(Q[trips[i].flag].begin()) <= trips[i].start)
                Q[trips[i].flag].erase(Q[trips[i].flag].begin());
            else
                ans[trips[i].flag]++;
            Q[1 - trips[i].flag].insert(trips[i].end + t);
        }

        cout << "Case #" << ++CASE << ": " << ans[0] << " " << ans[1] << endl;
    }
    return 0;
}
