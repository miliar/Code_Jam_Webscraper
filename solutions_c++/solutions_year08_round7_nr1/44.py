#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
using namespace std;

typedef unsigned nat;

struct mix {
	vector<nat> stuff;
	bool done;
	nat val;
};

typedef map<string, nat> mymap;

nat get(vector<mix>& MIX, nat a) {
	if (MIX[a].done)
		return MIX[a].val;

	nat n = MIX[a].stuff.size();
	vector<nat> A(n);

	for (nat i = 0; i != n; ++i)
		A[i] = get(MIX, MIX[a].stuff[i]);

	sort(A.begin(), A.end(), greater<nat>());

	if (n == 0)
		MIX[a].val = 1;
	else if (n == 1)
		MIX[a].val = max(A[0], 2u);
	else {
		nat f = 0;
		nat v = 0;
		nat ok = false;
		for (nat i = 0; i != n; ++i) {
			nat k = A[i];
			if (k > 1)
				ok = true;
			if (k <= f)
				--f;
			else {
				nat d = k - f;
				v+= d;
				f = k-1;
			}
		}
		MIX[a].val = ok ? v : v+1;
	}

	MIX[a].done = true;

	return MIX[a].val;
}

int main() {

	nat tc;
	cin >> tc;
	for (nat cs = 0; cs != tc; ++cs) {
		nat n;
		cin >> n;
		
		mymap M;
		nat idx = 0;
		vector<mix> MIX(n);
		for (nat i = 0; i != n; ++i) {
			string name;
			cin >> name;

			nat p;
			if (M.find(name) == M.end())
				p = M[name] = idx++;
			else
				p = M[name];

			nat m;
			cin >> m;
			for (nat j = 0; j != m; ++j) {\
				string s;
				cin >> s;
				if ('A' <= s[0] && s[0] <= 'Z') {
					nat q;
					if (M.find(s) == M.end())
						q = M[s] = idx++;
					else
						q = M[s];

					MIX[p].stuff.push_back(q);
				}
			}

			MIX[p].done = false;
		}

		printf("Case #%u: %u\n", cs+1, get(MIX, 0));
	}
}


