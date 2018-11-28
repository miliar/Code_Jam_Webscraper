#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;

string calc()
{
	stringstream S;
	int i, j;

	int N;
	cin >> N;

	vector<pair<int,int> > buttons;

	for (i=0; i<N; ++i) {
		char c;
		int a;
		cin >> c >> a;
		buttons.push_back(make_pair(c=='O'?0:1,a));
	}

	int ans = 0;
	int pos[2] = {1, 1};

	for (i=0; i<N; ++i) {
		int cur = buttons[i].first;
		int k = -1;
		for (j=i+1; j<N; ++j) {
			if (buttons[j].first != cur) {
				k = j;
				break;
			}
		}
		
		int needTime = 1 + abs(buttons[i].second-pos[cur]);
		pos[cur] = buttons[i].second;

		if (k != -1) {
			if (needTime >= abs(buttons[k].second-pos[1-cur])) {
				pos[1-cur] = buttons[k].second;
			} else {
				pos[1-cur] = buttons[k].second+ abs(buttons[k].second-pos[1-cur]) - needTime;
			}
		}

		ans += needTime;
	}

	S << ans;

	return S.str();
}

int main(void)
{
	int caseNum;
	cin >> caseNum;
	//string line;
	//getline(cin, line);
	for (int c=1; c<=caseNum; ++c) {
		cout << "Case #" << c << ": " << calc() << endl;
	}

	return 0;
}

