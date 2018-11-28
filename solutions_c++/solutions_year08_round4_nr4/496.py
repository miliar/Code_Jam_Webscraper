#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

const int INF=0x1fffffff;

int main() {
	ios_base::sync_with_stdio(false);
	int case_nr, N;

	cin >> N;

	for (case_nr=1; case_nr<=N; case_nr++) {
		int ret=INF, k;
		vector <int> perm;
		string S;

		cin >> k >> S;

		for (int i=0; i<k; i++)
			perm.push_back(i);

		do {
			string X=S;
			for (int i=0; i<X.size(); i+=k) {
				for (int j=0; j<k; j++)
					X[i+j]=S[i+perm[j]];
			}

			// compress

			int sz=X.size();
			for (int i=1; i<X.size(); i++)
				if (X[i]==X[i-1])
					sz--;

			ret=min(ret, sz);
		} while (next_permutation(perm.begin(), perm.end()));

		cout << "Case #" << case_nr << ": " << ret << endl;
	}
}
