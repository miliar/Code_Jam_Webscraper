#include <iostream>
#include <vector>
#include <map>


using namespace std;


//
// Main Function
//

int main()
{
	// Obtain the number of test cases
	int T;
	cin >> T;
	
	// Handle each test case
	for (int i = 0; i < T; i++) {
		
		// Obtain the values for the inputs
		int L, N, C;
		unsigned long long t;
		cin >> L;
		cin >> t;
		cin >> N;
		cin >> C;
		vector<int> a;
		a.resize(C);
		for (int j = 0; j < C; j++) {
			int val;
			cin >> val;
			a[j] = val;
		}
		
		// Determine the estimated travel times between stars
		vector<int> time;
		time.resize(N);
		for (int j = 0; j < N; j++)
			time[j] = a[j % C] * 2;  // 0.5 pacsec/hour speed assumed
		
		// Determine the ship's position at the earliest possible completion
		// of the speed boosters
		int pos = 0;
		unsigned long long elapsed = 0;
		for (int j = 0; j < N; j++) {
			if (elapsed + time[j] <= t) {
				pos++;
				elapsed += time[j];
				time[j] = 0;
			}
			else {
				time[j] -= (t - elapsed);
				elapsed = t;
				break;
			}
		}
//		cout << "pos: " << pos << ", elapsed: " << elapsed << endl;
//		for (int j = 0; j < N; j++)
//			cout << " " << time[j];
//		cout << endl;
		
		// Place the nonzero estimated travel time values in a map for more
		// efficient access. Key will be estimated travel time and value will
		// be number of travel segments having that estimated travel time.
		map<int, int> timeMap;
		for (int j = pos; j < N; j++) {
			int value = time[j];
			if (timeMap.find(value) != timeMap.end())
				(timeMap[value])++;
			else
				timeMap[value] = 1;
		}
//		map<int, int>::reverse_iterator i1 = timeMap.rbegin();
//		map<int, int>::reverse_iterator s1 = timeMap.rend();
//		while (i1 != s1) {
//			cout << " (" << (*i1).first << "," << (*i1).second << ")";
//			i1++;
//		}
//		cout << endl;
		
		// Decide the placement of the speed boosters. Prioritize on stars where
		// the estimated travel times are highest and then work our way down.
		// This approach naturally skips travel segments that have already been
		// completed because we already set the estimated travel times on those
		// to zero. Using the map we formed above, speed booster placements and
		// time computations may be sped up if many travel segments share the
		// same estimated travel time.
		while ((L > 0) && (timeMap.size() > 0)) {
			map<int, int>::reverse_iterator it = timeMap.rbegin();
			int value = (*it).first;
			int count = (*it).second;
//			cout << "value: " << value << ", count: " << count << endl;
			if (L >= count) {
				elapsed += ((unsigned long long) value / 2) *
						   (unsigned long long) count;
				L -= count;
				timeMap.erase(value);
			}
			else {
				elapsed += ((unsigned long long) value / 2) *
						   (unsigned long long) L;
				timeMap[value] -= L;
				L = 0;
			}
//			cout << "elapsed = " << elapsed << endl;
		}
		
		// Add in the travel time for segments that won't have speed boosters.
		map<int, int>::iterator it   = timeMap.begin();
		map<int, int>::iterator stop = timeMap.end();
		while (it != stop) {
			int value = (*it).first;
			int count = (*it).second;
			elapsed += (unsigned long long) value * (unsigned long long) count;
			it++;
//			cout << "elapsed = " << elapsed << endl;
		}
		
		// Provide the result
		cout << "Case #" << i + 1 << ": " << elapsed << endl;
	}
	
	return 0;
}
