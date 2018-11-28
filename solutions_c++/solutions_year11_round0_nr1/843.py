#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <deque>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

#define all(v) (v).begin(), (v).end()

const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = 1000 * 1000;

typedef long long ll;
typedef pair<int, int> pii;

struct button {
    int owner_id, number;
    button(int some_ownew_id, int some_number) 
        : owner_id(some_ownew_id)
        , number(some_number)
    {}
};


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        int n;
        cin >> n;
        vector<button> seq;
        for (int i = 0; i < n; ++i) {
            char owner;
            int number;
            cin >> owner >> number;
            if (owner == 'O') {
                seq.push_back(button(0, number));
            }
            else {
                seq.push_back(button(1, number));
            }
        }
        vector<int> last_press_time(2, 0);
        vector<int> last_button(2, 1);
        for (int i = 0; i < n; ++i) {
            int owner = seq[i].owner_id;
            int number = seq[i].number;
            int min_reach_time = 1 + abs(last_button[owner] - number) + last_press_time[owner];
            min_reach_time = max(min_reach_time, last_press_time[1 - owner] + 1);
            last_press_time[owner] = min_reach_time;
            last_button[owner] = number;
        }
        int result = max(last_press_time[0], last_press_time[1]);
        printf("Case #%d: %d\n", test, result);
    }
	return 0;
}
