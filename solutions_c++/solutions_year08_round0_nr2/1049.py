#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int N, case_nr, T, NA, NB, i;
	vector <int> A1, A2, D1, D2; // Arrivals and Departs from A and B;

	ios_base::sync_with_stdio(false);

	cin >> N;

	for (case_nr=1; case_nr<=N; case_nr++) {
		cin >> T >> NA >> NB;
		A1.clear(); A2.clear(); D1.clear(); D2.clear();

		for (i=0; i<NA; i++) {
			int g, m;
			cin >> g;
			cin.get();
			cin >> m;
			D1.push_back(g*60+m);

			cin >> g;
			cin.get();
			cin >> m;
			A2.push_back(g*60+m+T);
		}

		for (i=0; i<NB; i++) {
			int g, m;
			cin >> g;
			cin.get();
			cin >> m;
			D2.push_back(g*60+m);

			cin >> g;
			cin.get();
			cin >> m;
			A1.push_back(g*60+m+T);
		}

		sort(A1.begin(), A1.end());
		sort(A2.begin(), A2.end());
		sort(D1.begin(), D1.end());
		sort(D2.begin(), D2.end());

		int j=A1.size()-1, answerA=0, answerB=0;
		for (i=D1.size()-1; i>=0; i--) {
			bool inc = true;
			while (j>=0) {
				if (A1[j] <= D1[i]) {
					j--;
					inc=false;
					break;
				}
				j--;
			}

			if (inc)
				answerA++;
		}

		j=A2.size()-1;
		for (i=D2.size()-1; i>=0; i--) {
			bool inc = true;
			while (j>=0) {
				if (A2[j] <= D2[i]) {
					j--;
					inc=false;
					break;
				}
				j--;
			}

			if (inc)
				answerB++;
		}

		cout << "Case #" << case_nr << ": " << answerA << " " << answerB << "\n";
	}
}
