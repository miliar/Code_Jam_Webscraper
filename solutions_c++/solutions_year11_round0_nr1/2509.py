#include <iostream>

using namespace std;

#define pci pair <char, int>

const int MN = 100 + 10;

pci arr[MN];
int blue[MN], orange[MN];

void nxt(int &p, int &mass_p, int *mass) {
	if (p < mass[mass_p])
		p ++;
	else if (p > mass[mass_p])
		p --;
}

int solve(int n) {
	int curr = 0;
	int i = 1, bl = 1, or = 1, i_or = 1, i_bl = 1;
	while (i <= n) {
		if (arr[i].first == 'O') {
			if (or == arr[i].second) {
				i ++;
				i_or ++;
				nxt(bl, i_bl, blue);
			}
			else {
				nxt(or, i_or, orange);
				nxt(bl, i_bl, blue);
			}
		}
		else {
			if (bl == arr[i].second) {
				i ++;
				i_bl ++;
				nxt(or, i_or, orange);
			}
			else {
				nxt(or, i_or, orange);
				nxt(bl, i_bl, blue);
			}
		}
		curr ++;
	}
	return curr;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n;
	cin >> t;
	for(int i = 0; i < t; i ++) {
		cin >> n;
		blue[0] = orange[0] = 0;
		for(int j = 1; j <= n; j ++) {
			cin >> arr[j].first >> arr[j].second;
			if (arr[j].first == 'B')
				blue[++ blue[0]] = arr[j].second;
			else
				orange[++ orange[0]] = arr[j].second;
		}
		printf("Case #%d: %d\n", i + 1, solve(n));
	}
	return 0;
}