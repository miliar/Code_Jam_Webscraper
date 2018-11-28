#include<iostream>
#include<cstring>
#include<vector>

using namespace std;

int cache[1005][1005];

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
	int R, k, N;
	cin >> R >> k >> N;
	long long int groups[N];
	for (int i = 0; i < N; ++i) {
	    cin >> groups[i];
	}
	memset(cache, -1, sizeof(cache));
	vector<long long int> gain;
	int r = 0, pos = 0;
	long long int euros = 0;
	bool find_loop = false;
	int loop_pos, loop_start, loop_end;
	while (r < R) {
	    if (!find_loop) {
		long long int riders = 0;
		int prev_pos = pos;
		while (true) {
		    if (riders + groups[pos] <= k) {
			riders += groups[pos];
			if (++pos >= N) pos = 0;
			if (pos == prev_pos) break;
		    } else break;
		}
		if (cache[prev_pos][pos] != -1) {
		    find_loop = true;
		    loop_pos = cache[prev_pos][pos];
		    loop_start = cache[prev_pos][pos];
		    loop_end = gain.size()-1;
		} else {
		    cache[prev_pos][pos] = gain.size();
		    gain.push_back(riders);
		    euros += riders;
		    ++r;
		}
	    }
	    if (find_loop) {
		euros += gain[loop_pos];
		if (++loop_pos > loop_end) loop_pos = loop_start;
		++r;
	    }
	}
	cout << "Case #" << t << ": " << euros << endl;
    }
}
