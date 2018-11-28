#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1010;

struct segm
{
	int y1, y2;
};

int n;

segm s[MAX];

bool intersection(segm a, segm b)
{
	return ((a.y1 > b.y1 && a.y2 < b.y2)||(a.y1 < b.y1 && a.y2 > b.y2));
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int tt = 0; tt < t; ++tt) {
		int ans = 0;
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> s[i].y1 >> s[i].y2;
		for (int i = 0; i < n; ++i)
			for (int j = i+1; j < n; ++j)
				if (intersection(s[i], s[j]) || intersection(s[j], s[i]))
					++ans;
		cout << "Case #" << tt+1 << ": " << ans << endl;
	}

 	return 0;
}