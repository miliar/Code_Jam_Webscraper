#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main(void)
{
    int no_cases = 0;
    cin >> no_cases;

    for (int c=1; c<= no_cases; ++c) {
        long long rides = 0;
        long long space = 0;
        int no_groups = 0;
        cin >> rides;
        cin >> space;
        cin >> no_groups;
        vector<long long> group_sizes(no_groups);

        long long group_size = 0;
        long long all = 0;
        for (int i=0; i<no_groups; ++i) {
            cin >> group_size;
            group_sizes[i] = group_size;
            all += group_size;
        }

        // special case: enough space for everybody to get in
        if (space >= all) {
            cout << "Case #" << c << ": " << all * rides << endl;
            continue;
        }

        vector<int> starts;
        vector<long long> euros;

        int start = 0;
        while (find(starts.begin(), starts.end(), start) == starts.end()) {
            starts.push_back(start);
            long long space_left = space;
            int current = start;
            while (space_left >= group_sizes[current]) {
                space_left -= group_sizes[current];
                ++current;
                if (current >= no_groups) current = 0;
            }
            euros.push_back(space - space_left);
            start = current;
        }

        /*
        cerr << "starts:" << endl;
        copy(starts.begin(), starts.end(), ostream_iterator<int>(cerr, " "));
        cerr << endl;

        cerr << "euros:" << endl;
        copy(euros.begin(), euros.end(), ostream_iterator<long long>(cerr, " "));
        cerr << endl;
        */

        // find what's the repetition point
        int rep_index = 0;
        while (starts[rep_index] != start) ++rep_index;

        int rep_phase = starts.size() - rep_index;

        long long rep_euros = 0;
        for (int i=rep_index; i<starts.size(); ++i) {
            rep_euros += euros[i];
        }
        
        /*
        cerr << "rep phase: " << rep_phase << 
            ", index: " << rep_index << 
            ", euros: " << rep_euros << endl;
        */

        // first until rep_index...
        long long euros_earned = 0;
        for (int i=0; i<rep_index; ++i) {
            euros_earned += euros[i];
            --rides;
            if (rides == 0) break;
        }
        
        //cerr << "head: " << euros_earned << " rides left: " << rides << endl;

        // Then repetition, full rounds:
        euros_earned += ((rides / rep_phase)*rep_euros);

        long long left = rides % rep_phase;
        //cerr << "+ full: " << euros_earned << " " << rides << " " << left << endl;
        
        int i = 0;
        while (left) {
            euros_earned += euros[rep_index + i];
            ++i;
            --left;
        }
        
        cout << "Case #" << c << ": " << euros_earned << endl;
    }
    return 0;
}
