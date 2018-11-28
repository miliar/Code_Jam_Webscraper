#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=1; tt<=ts; ++tt) {

		int cnt;
		cin >> cnt;
		
		int n = 101,  m = 101;
		vector < vector<char> > a (n, vector<char> (m));
		queue < pair<int,int> > q;
		for (int i=0; i<cnt; ++i) {
			int x1, y1, x2, y2;
			scanf ("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int x=x1; x<=x2; ++x)
				for (int y=y1; y<=y2; ++y) {
					a[x][y] = true;
					q.push (make_pair (x, y));
				}
		}

		vector < pair<int,int> > die, alive, born;
		int ans = 0;
		while (q.size()) {
			/*
			for (int y=1; y<=6; ++y) {
				for (int x=1; x<=6; ++x)
					printf ("%c", a[x][y] ? '1' : '0');
				puts("");
			}
			puts("");
			*/
			alive.clear();
			die.clear();
			born.clear();

			++ans;
			while (q.size()) {
				int x = q.front().first,
					y = q.front().second;
				q.pop();

				if ((x-1<0 || !a[x-1][y]) && (y-1<0 || !a[x][y-1]))
					die.push_back (make_pair (x, y));
				else
					alive.push_back (make_pair (x, y));
				if (x+1 < n && !a[x+1][y] && (y-1>=0 && a[x+1][y-1]))
					born.push_back (make_pair (x+1, y));
			}

			for (size_t i=0; i<alive.size(); ++i)
				q.push (alive[i]);
			for (size_t i=0; i<die.size(); ++i)
				a[die[i].first][die[i].second] = false;
			for (size_t i=0; i<born.size(); ++i) {
				q.push (born[i]);
				a[born[i].first][born[i].second] = true;
			}

		}

		printf ("Case #%d: %d\n", tt, ans);
	}


}

