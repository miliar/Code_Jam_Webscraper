#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

int main()
{
	int N, case_nr, S, Q, answer, i;
	vector <string> engines, queries;
	set <string> unused, all;
	string tmp;

	ios_base::sync_with_stdio(false);

	getline(cin, tmp);
	N = atoi(tmp.c_str());

	for (case_nr=1; case_nr<=N; case_nr++) {
		getline(cin, tmp);
		S = atoi(tmp.c_str());

		engines.resize(S);

		all.clear();
		for (i=0; i<S; i++) {
			getline(cin, engines[i]);
			all.insert(engines[i]);
		}

		getline(cin, tmp);
		Q = atoi(tmp.c_str());

		queries.resize(Q);

		for (i=0; i<Q; i++)
			getline(cin, queries[i]);

		answer = 0;
	
			unused = all;
			for (i=0; i<Q; i++) {
				unused.erase(queries[i]);
				if (unused.empty()) {
					answer++;
					unused = all;
				}
				unused.erase(queries[i]);
			}

		cout << "Case #" << case_nr << ": " << answer << "\n";
	}
}
