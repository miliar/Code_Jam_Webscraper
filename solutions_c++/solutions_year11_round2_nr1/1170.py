#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);
	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int n;
		cin >> n;
		char input[100][100];
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				char ch;
				cin >> ch;
				input[i][j] = ch;
			}
		}

		double owp[100][100];
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				int played = 0;
				int win = 0;
				for (int k=0;k<n;k++) {
					if (k == i) continue;
					if (input[j][k] == '1') { played++; win++; }
					else if (input[j][k] == '0') { played++; }
				}

				owp[i][j] = (played == 0) ? 0 : ((double) win / played);
			}
		}

		cout << "Case #" << (q+1) << ": " << endl;

		for (int i=0;i<n;i++) {
			double rpi = 0;
			int played = 0;
			int won = 0;
			vector<int> opp;
			for (int j=0;j<n;j++) {
				if (input[i][j] == '0') {
					played++;
					opp.push_back(j);
				}
				else if (input[i][j] == '1') {
					played++;
					won++;
					opp.push_back(j);
				}
			}

			rpi += (((double) won) / played) / 4.0;
			double sum = 0;
			double sum2 = 0;
			for (int j=0;j<opp.size();j++) {
				sum += owp[i][opp[j]];

				int count = 0;
				double oop = 0;
				for (int k=0;k<n;k++) {
					if (input[k][opp[j]] == '0' || input[k][opp[j]] == '1') {
						oop += owp[opp[j]][k];
						count++;
					}
				}

				sum2 += oop / count;
			}

			rpi += sum / (opp.size() * 2) + sum2 / (opp.size() * 4);
			cout << rpi << endl;
		}
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
