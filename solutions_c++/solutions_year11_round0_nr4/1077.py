#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

#define DEBUG 0

using namespace std;

struct elt {
	int val;
	int index;
};

bool cmpElt (struct elt e1, struct elt e2) {
	return (e1.val < e2.val);
}

int main () {
	int nCases, iCase = 0;
	cin >> nCases;

	while (iCase < nCases) {
		int nElt;
		cin >> nElt;
		vector<struct elt> list;

		for (int i = 0; i < nElt; i++) {
			struct elt temp;
			cin >> temp.val;
			temp.index = i;
			list.push_back (temp);
		}

		sort (list.begin(), list.end(), cmpElt);
		vector<struct elt>::iterator it;
		
		int i = 0;
		int c = 0;
		for (it = list.begin(); it < list.end(); it++) {
			struct elt temp = *it;
			if (temp.index != i) {
				c++;
			}
			i++;

			if (DEBUG) printf ("Test val %d, index %d\n", temp.val, temp.index);
		}
		printf ("Case #%d: %.6f\n", ++iCase, (float) c);
	}

	return 0;
}
