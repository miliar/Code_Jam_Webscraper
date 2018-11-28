#include <climits>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <bitset>
#include <map>

using namespace std;

int parse_time(const string &s)
{
	const char *ss = s.c_str();
	int hh = atoi(ss);
	int mm = atoi(ss + 3);
	return hh * 60 + mm;
}

typedef vector<pair<int, int> > VP;

#define ARRIVING	0
#define LEAVING		1
#define WAITING		2

int
minimalize(VP &table, int trains)
{
	sort(table.begin(), table.end());

	for (int i = 0; i < table.size(); i++) {
		if (table[i].second == LEAVING) {
			for (int j = 0; j < i; j++) {
				if (table[j].second == ARRIVING) {
					table[i].second = WAITING;
					table[j].second = WAITING;
					trains--;
					break;
				}
			}
		}
	}
	return trains;
}

int
main(int argc, char **argv)
{
	int N, n;
	cin >> N;
	for (n = 0; n < N; n++) {
		int T, NA, NB;
		VP timetable_a;
		VP timetable_b;

		cin >> T >> NA >> NB;

		for (int i = 0; i < NA; i++) {
			string t1, t2;
			cin >> t1 >> t2;
			int time1 = parse_time(t1);
			int time2 = parse_time(t2);
			timetable_a.push_back(make_pair(time1, LEAVING));
			timetable_b.push_back(make_pair(time2 + T, ARRIVING));
		}

		for (int i = 0; i < NB; i++) {
			string t1, t2;
			cin >> t1 >> t2;
			int time1 = parse_time(t1);
			int time2 = parse_time(t2);
			timetable_b.push_back(make_pair(time1, LEAVING));
			timetable_a.push_back(make_pair(time2 + T, ARRIVING));
		}

		int a = minimalize(timetable_a, NA);
		int b = minimalize(timetable_b, NB);
		cout << "Case #" << n + 1 << ": " << a << " " << b << endl;
	}
	return 0;
}
