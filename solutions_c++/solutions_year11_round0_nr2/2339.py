#include <cstdio>
#include <iostream>
#include <vector>

#define px first
#define py second
#define mp make_pair

using namespace std;

void solve()
{
	int c, d, n;
	scanf("%d ", &c);
	vector<pair<pair<char, char>, char> > comb(c);
	for (int i = 0; i < c; ++i) {
		scanf("%c%c%c ", &comb[i].px.px, &comb[i].px.py, &comb[i].py);
	}
	scanf("%d ", &d);
	vector<pair<char, char> > destr(d);
	for (int i = 0; i < d; ++i) {
		scanf("%c%c ", &destr[i].px, &destr[i].py);
	}
	scanf("%d ", &n);
	vector<char> list;
	for (int i = 0; i < n; ++i) {
		char x;
		scanf("%c", &x);
		list.push_back(x);
		for (int j = 0; j < c; ++j) {
			if (list.size() < 2) {
				break;
			}
			char l1 = list[list.size() - 1], l2 = list[list.size() - 2];
			if (l1 == comb[j].px.px && l2 == comb[j].px.py || l1 == comb[j].px.py && l2 == comb[j].px.px) {
				list.pop_back();
				list.pop_back();
				list.push_back(comb[j].py);
				j = -1;
			}
		}
		if (list.empty()) {
			continue;
		}
		bool ok = false;
		for (int j = 0; j < d; ++j) {
			if (list.back() == destr[j].px) {
				for (size_t k = 0; k + 1 < list.size(); ++k) {
					if (list[k] == destr[j].py) {
						list.clear();
						ok = true;
						break;
					}
				}
				if (ok) {
					break;
				}
			}
			if (list.back() == destr[j].py) {
				for (size_t k = 0; k + 1 < list.size(); ++k) {
					if (list[k] == destr[j].px) {
						list.clear();
						ok = true;
						break;
					}
					if (ok) {
						break;
					}
				}
			}
		}
	}
	printf("[");
	for (size_t i = 0; i + 1 < list.size(); ++i) {
		printf("%c, ", list[i]);
	}
	if (list.size() > 0) {
		printf("%c", list.back());
	}
	printf("]\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
