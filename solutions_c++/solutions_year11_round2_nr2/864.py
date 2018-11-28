#include <vector>
#include <set>
#include <map>
#include <deque>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <iostream>

using namespace std;

const double EPS = 1e-9;

bool test_dist (double max_dist, double want_d, vector<double> &people) {
    if (people.size () == 0)
        return true;

    double prev_pos = people[0] - max_dist, cur_dist;
    int sz = people.size ();

    for (int i = 1; i < sz; ++i) {
        // cout << "prev pos " << prev_pos << endl;
        // cout << "i " << i << " people " << people[i] << endl;
        cur_dist = fabs (people[i] - prev_pos);

        if (people[i] > prev_pos ||
            fabs (people[i] - prev_pos) < EPS) {
            if (cur_dist < want_d) {
                if (cur_dist + max_dist > want_d ||
                    fabs (cur_dist + max_dist - want_d) < EPS) {
                
                    prev_pos = people[i] + (want_d - cur_dist);
                } else {
                    return false;
                } 
            } else if (fabs (cur_dist - want_d) < EPS) {
                prev_pos = people[i];
            } else {
                prev_pos = people[i] - min (max_dist, fabs (cur_dist - want_d));
            }
        } else {
            if (cur_dist > max_dist ||
                fabs (cur_dist - max_dist) < EPS) {

                return false;
            } else {
                if (want_d > (max_dist - cur_dist))
                    return false;
                else
                    prev_pos = prev_pos + min (want_d, max_dist - cur_dist);
            }
        }
    }

    // cout << "prev pos last " << prev_pos << endl;

    return true;
}

int main ()
{
    double want_d, cur_max_d, total_places;
    long long cur_people, cur_place;
    vector<double> people;
    int num_tests;
    double left, right, mid;

    cin >> num_tests;
    for (int test = 0; test < num_tests; ++test) {
        printf ("Case #%d: ", test + 1);

        cin >> total_places >> want_d;
        // cout << "total_places " << total_places << endl;
        // cout << "want_d " << want_d << endl;
        people.clear (); 

        for (int i = 0; i < total_places; ++i) {
            cin >> cur_place >> cur_people;
            // cout << "cur_place " << cur_place << endl;
            // cout << "cur_people " << cur_people << endl;

            while (cur_people--) {
                people.push_back (cur_place);
            }
        }

        left = 0;
        right = 1e15;

        while (fabs (right - left) > EPS) {
            mid = left + (right - left) / 2;
            // cout << "left " << left << endl;
            // cout << "mid " << mid << endl;
            // cout << "right " << right << endl;

            if (test_dist (mid, want_d, people)) {
                // cout << "ok " << endl;
                right = mid;
            } else {
                // cout << "not ok " << endl;
                left = mid;
            }
        }

        printf ("%.9lf\n", mid);
    }
    return 0;
}
