#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int test_count = 0;
    cin >> test_count;

    for (int test_index = 1; test_index <= test_count; test_index++) {
        int n = 0;
        cin >> n;

        long positions_o[111];
		long positions_b[111];
		long positions[111];

		long positions_o_count = 0;
		long positions_b_count = 0;

        for (int i = 0; i < n; i++) {
            string pos;
            string who;
            cin >> who >> pos;
            int new_pos = atoi(pos.c_str());
			if (who.compare("O") == 0) {
				positions_o[positions_o_count++] = new_pos;
				positions[i] = 0;
            } else {
				positions_b[positions_b_count++] = new_pos;
				positions[i] = 1;
            }

        }

		long index_o = 0;
		long index_b = 0;
		long pos_o = 1;
        long pos_b = 1;
        long ans = 0;

		for (int i = 0; i < n; i++) {
			long dist_o = fabs((float)(pos_o - positions_o[index_o]));
			long dist_b = fabs((float)(pos_b - positions_b[index_b]));
			long dist = min(dist_o, dist_b) + 1;
			
			if (positions[i] == 0) {
				ans += dist_o + 1;				
				pos_o = positions_o[index_o];
				index_o++;

				if (pos_b > positions_b[index_b]) {
					pos_b -= min(dist, pos_b - positions_b[index_b]);
				} else {
					pos_b += min(dist, positions_b[index_b] - pos_b);
				}
			} else {
				ans += dist_b + 1;
				pos_b = positions_b[index_b];
				index_b++;
				
				if (pos_o > positions_o[index_o]) {
					pos_o -= min(dist, pos_o - positions_o[index_o]);
				} else {
					pos_o += min(dist, positions_o[index_o] - pos_o);
				}
			}
		}
        cout << "Case #" << test_index << ": " << ans << endl;
    }

	return 0;
}
