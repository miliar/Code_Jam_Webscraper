#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct table
{
	int dep, arr, town;

	table(int dep, int arr, int town) {
		this->dep = dep;
		this->arr = arr;
		this->town = town;
	}
};

vector<table> t;
int av[3700][2];

int parse (){
	string s;
	cin >> s;
	return ((int)(s[0]-'0')*10 + (int)(s[1]-'0'))*60 +
		    (int)(s[3]-'0')*10 + (int)(s[4]-'0');
}

bool cmp (table a, table b)
{
	if (a.dep == b.dep)
		return a.arr < b.arr;
	return a.dep < b.dep;
}

int main ()
{
	int test, tests;
	cin >> tests;
	for (test = 1; test <= tests; ++test) {
		int ansa = 0, 
			ansb = 0;

		int i, j;
		int T, na, nb;
		cin >> T;
		cin >> na >> nb;

		t.clear();

		for (i = 0; i < na; ++i)
		{
			int a, b;
			a = parse();
			b = parse();
			t.push_back(table(a, b, 0));
		}

		for (i = 0; i < nb; ++i) 
		{
			int a, b;
			a = parse();
			b = parse();
			t.push_back(table(a, b, 1));
		}

		memset(av, 0, sizeof(av));
		sort(t.begin(), t.end(), &cmp);

		int from = 0,
			ava = 0,
			avb = 0;

		for (i = 0; i < t.size(); ++i) {
			for (j = from; j <= t[i].dep; ++j) {
				ava += av[j][0];
				avb += av[j][1];
				av[j][0] = av[j][1] = 0;
			}
			from = t[i].dep;

//			cout << t[i].town << " " << (int)(t[i].dep/60) << ":" << t[i].dep%60 << " --> " << (int)(t[i].arr/60) << ":" << t[i].arr%60 << " | " << ava << "-" << avb << endl;

			if (t[i].town == 0 && ava > 0) {
				ava--;
				av[t[i].arr + T][1] ++;
			}
			else if (t[i].town == 0 && ava == 0) {
				ansa++;
				av[t[i].arr + T][1] ++;
			}
			else if (t[i].town == 1 && avb > 0) {
				avb--;
				av[t[i].arr + T][0] ++;
			}
			else if (t[i].town == 1 && avb == 0) {
				ansb++;
				av[t[i].arr + T][0] ++;
			}
		}


		cout << "Case #" << test << ": " << ansa << " " << ansb << endl;
	}
	return 0;
};