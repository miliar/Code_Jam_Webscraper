#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{
	ifstream in(argv[1]);
	int tests;
	in >> tests;
	for(unsigned test = 1; test <= tests; ++test)
	{
		int r, k, n;
		in >> r >> k >> n;
		
		vector<unsigned> g;
		g.resize(n);
		for(int i = 0; i < n; ++i)
			in >> g[i];

		int next_state[1024];
		long long value[1024];
		int rides[1024];

		for(int i = 0; i < n; ++i) {
			next_state[i] = -1;
			value[i] = -1;
			rides[i] = -1;
		}

		int cur_state = 0;
		int cur_rides = 0;
		long long cur_value = 0;
		
		value[cur_state] = cur_value;
		rides[cur_state] = cur_rides;
		
		bool found_loop = false;

		while(cur_rides < r)
		{
			int left = k;
			unsigned i;
			for(i = cur_state; i < n; ++i) {
				if(g[i] > left)
					goto done;
				left -= g[i];
			}

			for(i = 0; i < cur_state; ++i) {
				if(g[i] > left)
					goto done;
				left -= g[i];
			}
done:;
			cur_value += k - left;
			++cur_rides;

			if(!found_loop && value[i] >= 0) {
				int loop_rides = cur_rides - rides[i];
				long long loop_value = cur_value - value[i];

				if((cur_rides + loop_rides) <= r) {
					int loop_times = (r - cur_rides) / loop_rides;

					cur_rides += loop_times * loop_rides;
					cur_value += loop_times * loop_value;
				}
				found_loop = true;
			}

			next_state[cur_state] = i;
			cur_state = i;
			value[cur_state] = cur_value;
			rides[cur_state] = cur_rides;
			
			//cerr << cur_rides << ": state " << cur_state << " $ " << cur_value << endl;
		}

		cout << "Case #" << test << ": " << cur_value << endl;
	}
	return 0;
}

