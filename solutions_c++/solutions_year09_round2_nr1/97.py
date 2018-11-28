#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


map <string, int> ff;


class Tr {
public:
	long double p;
	bool isleaf;
	int ff;
	Tr * ll, *rr;
	Tr() {p = 0; ll = rr = NULL; isleaf = true;ff = 0;}
};

Tr * root;

Tr * GetTree()
{
	Tr *res;
	res = new Tr;
	char c;
	string s;
	cin >> res->p;
	c = getchar();
	res->isleaf = true;
	while ((c < 'a' || c > 'z') && c != ')') {
		c = getchar();
	}
	if (c == ')') {
		return res;
	}	
	res->isleaf = false;
	s = "";
	while (c >= 'a' && c <= 'z') {
		s += c;
		c = getchar();
	}
	if (ff.find(s) == ff.end()) {
		res->ff = ff.size() + 1;
		ff[s] = res->ff;
	}
	res->ff = ff[s];
	c = getchar();
	while (c != '(') c = getchar();
	res->ll = GetTree();
	c = getchar();
	while (c != '(') c = getchar();
	res->rr = GetTree();
	c = getchar();
   	while (c != ')') c = getchar();
   	return res;
}

int n;
set<int> an[111];


long double GetAns(Tr *cur, int ii)
{
	if (cur->isleaf) {
		return cur->p;
	}
	long double res = cur->p;
	if (an[ii].find(cur->ff) != an[ii].end()) {
		return res * GetAns(cur->ll, ii);
	};
	return res * GetAns(cur->rr, ii);
}

void Load()
{
	int i, j, k, t;
	char c;
	string s;
	cin >> i;
	ff.clear();
	c = getchar();
	while (c != '(') c = getchar();
	root = GetTree();
	cin >> n;
	for (i = 1; i <= n; i++) {
		cin >> s;
		an[i].clear();
		cin >> j;
		for (k = 0; k < j; k++) {
			cin >> s;
			if (ff.find(s) == ff.end()) {
				t = ff.size() + 1;
				ff[s] = t;
			}
			an[i].insert(ff[s]);
		}
	}
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(11);
	for (i = 1; i <= n; i++)
		cout << GetAns(root, i) << "\n";
}



void Solve()
{
}



int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tt, nt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ":\n";
		Load();
		Solve();

	}
	return 0;
}