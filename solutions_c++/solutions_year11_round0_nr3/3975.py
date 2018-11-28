#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int case_nr, T;

	cin >> T;

	for (case_nr=1; case_nr<=T; case_nr++) {
		cout << "Case #" << case_nr << ": ";

		int N, C, best = -1;
		cin >> N;
		vector<tuple<int, int, int, int>> v, v2;

		v.push_back(make_tuple(0,0,0,0));
		for (int i=0; i<N; i++) {
			cin >> C;

			for (vector<int>::size_type j=0; j<v.size(); j++) {
				v2.push_back(make_tuple(get<0>(v[j])^C, get<1>(v[j]), get<2>(v[j])+C, get<3>(v[j])));
				v2.push_back(make_tuple(get<0>(v[j]), get<1>(v[j])^C, get<2>(v[j]), get<3>(v[j])+C));
			}

			v = v2;
			v2.clear();
		}

		for (vector<int>::size_type j=0; j<v.size(); j++)
			if (get<0>(v[j]) == get<1>(v[j]) && get<3>(v[j])!=0)
				best = max(best, get<2>(v[j]));

		if (best == -1)
			cout << "NO\n";
		else
			cout << best << "\n";
	}
}
