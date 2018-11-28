#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int tominutes(string s)
{
	int h, m;
	char c;
	istringstream ss(s);
	ss >> h >> c >> m;
	return h * 60 + m;
}

struct trip
{
	int start, finish, town;
	trip(int start_, int finish_, int town_) : start(start_), finish(finish_), town(town_) {}
	bool operator < (const trip& obj) { return start == obj.start ? finish < obj.finish : start < obj.start; }
};

pair<int, int> solve(int t, const vector<trip>& a)
{
	int res[2] = {0, 0}, have[210][2] = {0, 0};
	int trips = (int)a.size();
	vector<int> was(trips, 0);

	for (int i = 0; i < trips; ++i) {
		int from = a[i].town;
		if (!have[i][from]) {
			++res[from];
			for (int j = i + 1; j < trips; ++j) {
				if (a[j].town == !from && a[j].start >= a[i].finish + t) ++have[j][!from];
			}
		} else {
			for (int j = i + 1; j < trips; ++j) {
				if (a[j].town == from) --have[j][from];
				if (a[j].town == !from && a[j].start >= a[i].finish + t) ++have[j][!from];
			}
		}
	}

	return make_pair(res[0], res[1]);
}

int main()
{
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int t, na, nb;
		cin >> t >> na >> nb;
		vector<trip> a;
		string s1, s2;
		for (int i = 0; i < na; ++i) {
			cin >> s1 >> s2;
			a.push_back(trip(tominutes(s1), tominutes(s2), 0));
		}
		for (int i = 0; i < nb; ++i) {
			cin >> s1 >> s2;
			a.push_back(trip(tominutes(s1), tominutes(s2), 1));
		}
		sort(a.begin(), a.end());
		pair<int, int> result = solve(t, a);
		cout << "Case #" << (test + 1) << ": " << result.first << " " << result.second << endl;
	}
	return 0;
}
