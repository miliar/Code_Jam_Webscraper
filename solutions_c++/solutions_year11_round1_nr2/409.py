#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

string dict[10000];


int main() {
	ifstream cin("B-small.in");
	ofstream cout("B-small.out");
	int T;
	cin >> T;
	int cc = 1;
	while (T--) {
		int N, M;
		cin >> N >> M;
		for (int i = 0; i < N; i++)
			cin >> dict[i];
		vector<string> ans;
		for (int i = 0; i < M; i++) {
			string list;
			cin >> list;
			int bst = -1;
			string bstw = "";
			for (int w = 0; w < N; w++) {
				//string mask;
				bool dead[100];
				memset(dead, false, sizeof(dead));
				/*for (int t = 0; t < dict[w].size(); t++) {
					mask += "-";
				}*/
				int co = 0;
				for (int l = 0; l < list.size(); l++) {
					bool willGuess = false;
					char c = list[l];
					for (int i = 0; i < N; i++) {
						if (!dead[i]) {
							if (dict[i].size() != dict[w].size())
								dead[i] = true;
							/*else {
								for (int t = 0; t < dict[i].size(); t++)
									if (mask[t] != '-' && mask[t] != dict[i][t])
										dead[i] = true;
							}*/
						}

						if (!dead[i] && dict[i].find(c) != -1)
							willGuess = true;
					}

					if (willGuess) {
						if (dict[w].find(c) == -1)
							co++;
						for (int i = 0; i < dict[w].size(); i++) {
							for (int t = 0; t < N; t++)
								if (!dead[t] && ((dict[t][i] != c && dict[w][i] == c) || (dict[t][i] == c && dict[w][i] != c)))
									dead[t] = true;
							
						}


					}
				}
				if (co > bst) {
						bst = co;
						bstw = dict[w];
					}
				

			}

			ans.push_back(bstw);
		}
		


		cout << "Case #" << cc++ <<": " << ans[0];
		for (int i = 1; i < ans.size(); i++)
			cout << " " << ans[i];
		cout << endl;
	}
	return 0;
}