#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

typedef long long lint;

int find_want(vector <pair <char, int> >& ops, char c, int i)
{
	for (int j = i; j < ops.size(); j++)
		if (ops[j].first == c)
			return ops[j].second;
	return 1;
}

int main()
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int n;
		vector <pair <char, int> > ops;

		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			char color;
			int pos;
			scanf(" %c %d", &color, &pos);
			ops.push_back(make_pair(color, pos));
		}

		int pos1 = 1, pos2 = 1, delay = 0;
		int i = 0;
		int want1 = find_want(ops, 'O', i);
		int want2 = find_want(ops, 'B', i);

		while (i < ops.size()) {
			int pushed = 0;

			if (pos1 < want1)
				pos1 ++;
			else if (pos1 > want1)
				pos1 --;
			else if (pos1 == want1 && ops[i].first == 'O') {
				i++;
				want1 = find_want(ops, 'O', i);
				pushed = 1;
			}			

			if (pos2 < want2)
				pos2 ++;
			else if (pos2 > want2)
				pos2 --;
			else if (pos2 == want2 && ops[i].first == 'B' && !pushed) {
				i++;
				want2 = find_want(ops, 'B', i);
			}

			delay ++;
		}

		printf("Case #%d: %d\n", t+1, delay);
	}

	return 0;
}
