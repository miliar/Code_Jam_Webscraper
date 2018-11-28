#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int T;
int NA, NB;
vector<pair<int,int> > a;
vector<pair<int,int> > b;

void trainb(int i);
void traina(int i)
{
	pair<int,int> cur = a[i];
	a.erase(a.begin()+i);

	for (int j=0; j<b.size(); ++j) {
		if (b[j].first >= cur.second) {
			return trainb(j);
		}
	}
}

void trainb(int i)
{
	pair<int,int> cur = b[i];
	b.erase(b.begin()+i);

	for (int j=0; j<a.size(); ++j) {
		if (a[j].first >= cur.second) {
			return traina(j);
		}
	}
}

int conv(string s)
{
	int a = (s[0]-'0')*10+s[1]-'0';
	int b = (s[3]-'0')*10+s[4]-'0';

	return a*60+b;
}

int main(void)
{
	int i, j, k;
	int N;
	cin >> N;
	for (i=1; i<=N; ++i) {
		cin >> T;
		cin >> NA >> NB;

		a.clear();
		b.clear();

		string s1, s2;
		for (j=0; j<NA; ++j) {
			cin >> s1 >> s2;
			a.push_back(pair<int,int>(conv(s1), conv(s2)+T));
			//cout << a[a.size()-1].first << ' ' << a[a.size()-1].second << endl;
		}
		sort(a.begin(), a.end());
		for (j=0; j<NB; ++j) {
			cin >> s1 >> s2;
			b.push_back(pair<int,int>(conv(s1), conv(s2)+T));
			//cout << b[b.size()-1].first << ' ' << b[b.size()-1].second << endl;
		}
		sort(b.begin(), b.end());

		int anum = 0;
		int bnum = 0;

		while (a.size() && b.size()) {
			if (a[0].first <= b[0].first) {
				anum++;
				traina(0);
			} else {
				bnum++;
				trainb(0);
			}
		}

		anum += a.size();
		bnum += b.size();

		cout << "Case #" << i << ": " << anum << ' ' << bnum << endl;
	}

	return 0;
}

