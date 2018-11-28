#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX 1000

vector<int> wins[MAX];
vector<int> losses[MAX];

double wp[MAX];
double owp[MAX];
double oowp[MAX];


int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int c = 1; c <= numCases; c++) {
		int numTeams;
		scanf("%d", &numTeams);

		char buffer[MAX];
		for (int i = 0; i < numTeams; i++) {
			wins[i].clear();
			losses[i].clear();

			scanf("%s", buffer);

			for (int j = 0; j < numTeams; j++) {
				if (buffer[j] == '1') {
					wins[i].push_back(j);
				} else if (buffer[j] == '0') {
					losses[i].push_back(j);
				}
			}

			wp[i] = (double) wins[i].size() / (double) (wins[i].size() + losses[i].size());
//			printf("wp[%d] = %3.3lf\n", i, wp[i]);
		}
		for (int i = 0; i < numTeams; i++) {
			double tmpOP = 0.0;
			for (int j = 0; j < (signed) wins[i].size(); j++) {
				int other = wins[i][j];
				double tmp = wp[other] * (double) (wins[other].size() + losses[other].size());
				tmp /= (double) (wins[other].size() + losses[other].size() - 1);
				tmpOP += tmp;
			}
			for (int j = 0; j < (signed) losses[i].size(); j++) {
				int other = losses[i][j];
				double tmp = wp[other] * (double) (wins[other].size() + losses[other].size());
				tmp -= 1.0;
				tmp /= (double) (wins[other].size() + losses[other].size() - 1);
				tmpOP += tmp;
			}
			owp[i] = tmpOP / (double) (wins[i].size() + losses[i].size());
//			printf("owp[%d] = %3.3lf\n", i, owp[i]);
		}
		for (int i = 0; i < numTeams; i++) {
			double tmpOP = 0.0;
			for (int j = 0; j < (signed) wins[i].size(); j++) {
				int other = wins[i][j];
				tmpOP += owp[other];
			}
			for (int j = 0; j < (signed) losses[i].size(); j++) {
				int other = losses[i][j];
				tmpOP += owp[other];
			}
			oowp[i] = tmpOP / (double) (wins[i].size() + losses[i].size());
//			printf("oowp[%d] = %3.3lf\n", i, oowp[i]);
		}
		printf("Case #%d:\n", c);
		for (int i = 0; i < numTeams; i++) {
			printf("%12.12lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}


	}

	return 0;
}
