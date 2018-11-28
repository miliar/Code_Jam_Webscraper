#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	string temp;
	int n;
	cin >> n;
	for (int c = 0; c < n; c++) {
		int s;
		cin >> s;
		getline(cin, temp);
		vector <string> searchengines;
		for (int i = 0; i < s; i++) {
			getline(cin, temp);
			searchengines.push_back(temp);
		}

		int q;
		cin >> q;
		getline(cin, temp);
		vector <string> queries;
		for (int i = 0; i < q; i++) {
			getline(cin, temp);
			//printf("%d: %s\n", i, temp.c_str());
			queries.push_back(temp);
		}

		int sw = 0;
		vector <int> checked(s, 0);
		for (int i = 0; i < q; i++) {
			int se = -1;
			for (int j = 0; j < s; j++) {
				if (queries[i] == searchengines[j]) {
					se = j;
				}
			}
			if (se >= 0) checked[se] = 1;
			int ac = 0;
			for (int j = 0; j < s; j++) {
				ac += checked[j];
			}
			if (ac == s) {
				sw ++;
				checked.resize(0);
				checked.resize(s, 0);
			}
			if (se >= 0) checked[se] = 1;
		}
		
		printf("Case #%d: %d\n", c + 1, sw);
	}

	return 0;
}
