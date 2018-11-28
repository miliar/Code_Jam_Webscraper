
#include <utility>
#include <vector>
#include <iostream>
using namespace std;

int H, W;

int north(int c) { return c < W? -1: c - W; }

int south(int c) { return (c + W) >= H*W? -1: c + W; }

int west(int c) { return c % W == 0? -1: --c; }

int east(int c) { return c % W == (W - 1)? -1: ++c; }

int
drainsto(int c, const vector<int>& alts)
{
	int d = c, a = alts[c];
	int n = north(c); if (n != -1 && alts[n] < a) a = alts[d = n];
	int w = west(c); if (w != -1 && alts[w] < a) a = alts[d = w];
	int e = east(c); if (e != -1 && alts[e] < a) a = alts[d = e];
	int s = south(c); if (s != -1 && alts[s] < a) a = alts[d = s];
	return d;
}

vector<int>
markareas(const vector<int>& alts)
{
	vector<int> labels(alts.size(), 0);
	vector<int> marked;

	int label = 1;
	for (unsigned i = 0; i < alts.size(); i++) {
		if (drainsto(i, alts) == i) {
			labels[i] = label++;
			marked.push_back(i);
		}
	}
	while (!marked.empty()) {
		int c = marked.back(); marked.pop_back();
		char label = labels[c];
		int n = north(c); if (n != -1 && labels[n] == 0 && drainsto(n, alts) == c) { labels[n] = label; marked.push_back(n);}
		int w = west(c); if (w != -1 && labels[w] == 0 && drainsto(w, alts) == c) { labels[w] = label; marked.push_back(w);}
		int e = east(c); if (e != -1 && labels[e] == 0 && drainsto(e, alts) == c) { labels[e] = label; marked.push_back(e);}
		int s = south(c); if (s != -1 && labels[s] == 0 && drainsto(s, alts) == c) { labels[s] = label; marked.push_back(s);}
	}
	return labels;
}

void
displayMap(vector<int> labels)
{
	vector<char> names(27, 0);
	char label = 'a';

	int k = 0;
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			if (names[labels[k]] == 0) {
				names[labels[k]] = label++;
			}
			cout << names[labels[k++]] << ' ';
		}
		cout << endl;
	}
}


int
main()
{
	int nmaps;
	vector<int> alts;

	cin >> nmaps;
	for (int i = 1; i <= nmaps; i++) {
		cin >> H >> W;
		alts.resize(H * W);
		for (unsigned k = 0; k < alts.size(); k++) {
			cin >> alts[k];
		}
		cout << "Case #" << i << ":" << endl;
		displayMap(markareas(alts));
	}
}
