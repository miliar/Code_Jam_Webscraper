#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

int c, d, n;
map<pair<char, char>, char> combine, oposite;
vector<char> list;
char str[1000];


void add(char c) {
	char A, B;
	map<pair<char, char>, char>::iterator e;
	list.push_back(c);
	while (list.size() > 1) {
		A = list[list.size() - 1];
		B = list[list.size() - 2];
		e = combine.find(make_pair(A, B));
		if (e == combine.end())
			e = combine.find(make_pair(B, A));

		if (e == combine.end())
			break;

		list.pop_back();
		list.pop_back();
		list.push_back(e->second);
	}

	c = list[list.size() - 1];
	for (int i=0, n = list.size() - 1; i < n; ++ i) {
		if (oposite.find(make_pair(list[i], c)) != oposite.end() || oposite.find(make_pair(c, list[i])) != oposite.end()) {
			list.clear();
			return;
		}
	}

}

void print_list() {
	cout << "[";
	for (int i=0, n = list.size(); i < n; ++ i) {
		cout << list[i];
		if (i + 1 < n)
			cout << ", ";
	}
	cout << "]";
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, TT;
	cin >> T;
	for (int TT=1;TT<=T;++TT) {
		combine.clear();
		oposite.clear();
		list.clear();

		cin >> c;
		while (c--) {
			cin >> str;
			combine[make_pair(str[0], str[1])] = str[2];
		}

		cin >> d;
		while (d--) {
			cin >> str;
			oposite[make_pair(str[0], str[1])] = 1;
		}

		cin >> n >> str;

		for (int i=0;i<n;++i) {
			add(str[i]);
		}


		cout << "Case #" << TT << ": ";
		print_list();
		cout << "\n";
	}

	return 0;
}
