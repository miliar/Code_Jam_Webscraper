#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

struct seq {
    char hall;
    int loc;

    seq (char h, int l)
    {
        hall = h;
        loc = l;
    }
};

int main (int argc, char *argv [])
{
    int T = 0;
    int N = 0;

    int i = 0;
    int j = 0;

    cin >> T;

    while (T)
	{
        vector <struct seq> full_sequence;
		T --;

        cin >> N;

		for (j = 0; j < N; j ++) {
            char h;
            int l;
            cin >> h >> l;
            struct seq s (h, l);
            full_sequence.push_back (s);
        }

        int B_loc = 1;
        int O_loc = 1;
        int B_time = 0;
        int O_time = 0;
        int B_total_time = 0;
        int O_total_time = 0;
        int ans = 0;

        int free_time = 0;

        for (j = 0; j < N; j ++) {
            // cout << endl << j << " " << "Hall: " << full_sequence [j].hall << " Loc: " << full_sequence [j].loc << endl;
            if (full_sequence [j].hall == 'B') {
                free_time = abs (full_sequence [j].loc - B_loc) - O_time;
                B_time += (free_time < 0? 1: 1 + free_time);
                B_loc = full_sequence [j].loc;
                O_time = 0;
                B_total_time += (free_time < 0? 1: 1 + free_time);
            } else {
                free_time = abs (full_sequence [j].loc - O_loc) - B_time;
                O_time += (free_time < 0? 1: 1 + free_time);
                O_loc = full_sequence [j].loc;
                B_time = 0;
                O_total_time += (free_time < 0? 1: 1 + free_time);
            }
            // cout << "O_total_time: " << O_total_time << "\t" << "B_total_time: " << B_total_time << endl;
        }

        ans = O_total_time + B_total_time;

		printf ("Case #%d: %lld\n", i + 1, ans);
		i ++;
    }

    return 0;
}
