#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int casenum = 1; casenum <= n; casenum++) {
		string temp;
		int h, m;
		char c;

		vector <int> time[4];
		int t, s, e;
		cin >> t >> s >> e;

		for (int i = 0; i < s; i++) {
			cin >> h >> c >> m;
			time[0].push_back(h * 60 + m);
			cin >> h >> c >> m;
			time[1].push_back(h * 60 + m);
		}
		for (int i = 0; i < e; i++) {
			cin >> h >> c >> m;
			time[2].push_back(h * 60 + m);
			cin >> h >> c >> m;
			time[3].push_back(h * 60 + m);
		}

		for (int i = 0; i < 4; i++) {
			time[i].push_back(28 * 60);
			sort(time[i].begin(), time[i].end());
		}

		int a, b, num;
		int mina = 0;
		a = b = num = 0;
		while (a < s || b < e) {
			if (time[0][a] >= time[3][b] + t) {
				num ++;
				b ++;
			} else {
				num --;
				a ++;
			}
			mina = min(mina, num);
		}

		int minb = 0;
		a = b = num = 0;
		while (a < s || b < e) {
			if (time[2][b] >= time[1][a] + t) {
				num ++;
				a ++;
			} else {
				num --;
				b ++;
			}
			minb = min(minb, num);
		}

		printf("Case #%d: %d %d\n", casenum, -mina, -minb);
	}

	return 0;
}
