#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

string pat;
vector<string> words;

vector<string> part;
int L, D, N;

bool ok(string &w)
{
	for (int i=0; i<w.length(); ++i) {
		string::iterator it = lower_bound(part[i].begin(), part[i].end(), w[i]);
		if (it == part[i].end()) return false;
		if (*it != w[i]) return false;
	}
	return true;
}


int calc(void)
{
	int i;
	int j = 0;
	for (i=0; i<L; ++i) {
		if (pat[j] != '(') {
			part[i] = string(1, pat[j]);
			j++;
		} else {
			part[i] = "";
			j++;
			while (pat[j] != ')') {
				part[i] += pat[j];
				j++;
			}
			j++;
		}

		sort(part[i].begin(), part[i].end());
	}
	
	int ans = 0;
	for (i=0; i<words.size(); ++i) {
		if (ok(words[i])) ans++;
	}
	return ans;
}

int main(void)
{
	cin >> L >> D >> N;

	part.resize(L);

	int i;
	words.resize(D);
	for (i=0; i<D; ++i) {
		cin >> words[i];
	}

	for (int ca=1; ca<=N; ++ca) {
		cin >> pat;
		cout << "Case #" << ca << ": " << calc() << endl;
	}

	return 0;
}
