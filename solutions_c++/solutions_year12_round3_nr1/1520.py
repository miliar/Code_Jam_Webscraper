#include "stdlib.h"
#include "iostream"
#include "vector"
#include "algorithm"
#include <map>

using namespace std;

int main()
{
	int t;
	cin >> t;
	
	for (int i = 0; i < t; i++) {
		int N;
		cin >> N;
		std::vector<std::vector<int>> graf(N);
		for (int j = 0; j < N; j++) {
			int m;
			cin >> m;
			for (int k = 0; k < m; k++) {
				int clas;
				cin >> clas;
				graf[j].push_back(clas - 1);
			}
		}
		bool answer_finded = false;
		for (int j = 0; j < N; j++) {
			std::vector<int> answer(N, 0);
			std::vector<int> way(graf[j]);
			
			while (way.size() != 0) {
				int clas = way.back();
				way.pop_back();
				if (answer[clas] == 0) {
					answer[clas]++;
				} else {
					answer_finded = true;
					break;
				}
				for (int k = 0; k < graf[clas].size(); k++) {
					way.push_back(graf[clas][k]);
				}
			}

			if (answer_finded == true) {
				break;
			}
		}

		cout << "Case #" << (i + 1) << ": " ;
		if (answer_finded == true) {
			cout << "Yes\n";
		} else {
			cout << "No\n";
		}
	}
		
	return 0;
}
