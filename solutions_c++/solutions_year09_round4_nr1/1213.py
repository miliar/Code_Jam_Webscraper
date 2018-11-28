#include <fstream>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cctype>
#include <stdio.h>
#include <cstdlib>

using namespace std;

ifstream in("1.in");
ofstream out("1.out");

struct mas
{
	int kol;
	vector<int> a;
};

vector<int> a;
queue<mas> Q;
mas q;
string s[100];
int n, t, ans;
string st;

bool prov()
{
	for (int i = 0; i < n; i++)
		if (q.a[i] > i) return false;
	return true;
}

int main()
{
	in >> t;

	for (int tt = 0; tt < t; tt++) {
		in >> n;
		getline(in, st);
		ans = 0;
		for (int i = 0; i < n; i++) getline(in, s[i]);
		a.clear();
		for (int i = 0; i < n; i++) {
			bool f = false;
			for (int j = n - 1; j >= 0; j--) 
				if (s[i][j] == '1') {
					a.push_back(j);
					f = true;
					break;
				}
			if (!f) a.push_back(0);
		}
		q.a = a;
		q.kol = 0;
		if (prov()) ans = 0;
		else {
			set<vector<int> > S;			
			S.insert(a);
			ans = 0;
			Q.push(q);
			while (!Q.empty()) {
				q = Q.front();
				Q.pop();
				if (ans != 0) continue;
				for (int i = 0; i < n - 1; i++) {
					swap(q.a[i], q.a[i + 1]);
					if (S.find(q.a) == S.end()) {
						S.insert(q.a);
						q.kol++;
						if (prov()) {
							ans = q.kol;
							break;
						}
						Q.push(q);
						q.kol--;
					}
					swap(q.a[i], q.a[i + 1]);
				}
			}
		}

		out << "Case #" << tt + 1 << ": " << ans << endl;
	}

	return 0;
}
