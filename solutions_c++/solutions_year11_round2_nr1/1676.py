#include      <iostream>
#include      <fstream>
#include      <string>
#include      <iomanip>

int main(int argc, char **argv) {
	int nTests;
	int nTeams;

	double afRPS[101];
	double afWPS[101][101];
	double afOWPS[101];
	double afOOWPS[101];
	char achTeamSch[1001][1001];
	int nOnes;
	int i, j;

	std::ifstream in("in");
	in >> nTests;

	for (int nTest = 1; nTest <= nTests; ++nTest) {
		in >> nTeams;

		for (i = 0; i < nTeams; ++i) {
			nOnes = 0;
			afWPS[i][1] = 0;

			for (j = 0; j < nTeams; ++j) {
				in >> achTeamSch[i][j];

				if (achTeamSch[i][j] == '1') {
					++nOnes;
					++afWPS[i][1];
				} else if (achTeamSch[i][j] == '0') {
					++afWPS[i][1];
				}
			}

			afWPS[i][0] = static_cast<double>(nOnes) / afWPS[i][1];
		}

		for (i = 0; i < nTeams; ++i) {
			afOWPS[i] = 0;
			double newWP;

			for (j = 0; j < nTeams; ++j) {
				if (achTeamSch[i][j] == '1' || achTeamSch[i][j] == '0') {
					newWP = afWPS[j][0];

					if (achTeamSch[i][j] == '1') {
						newWP = newWP * (afWPS[j][1] / (afWPS[j][1] - 1));
					} else {
						newWP = (newWP - 1 / afWPS[j][1]) * (afWPS[j][1] / (afWPS[j][1] - 1));
					}

					afOWPS[i] += newWP;
				}
			}

			afOWPS[i] /= afWPS[i][1];
		}

		for (i = 0; i < nTeams; ++i) {
			afOOWPS[i] = 0;

			for (j = 0; j < nTeams; ++j) {
				if (achTeamSch[i][j] == '1' || achTeamSch[i][j] == '0') {
					afOOWPS[i] += afOWPS[j];
				}
			}

			afOOWPS[i] /= afWPS[i][1];
		}

		std::cout << "Case #" << nTest << ":" << std::endl;

		for (i = 0; i < nTeams; ++i) {
			//std::cout << afWPS[i][0] << ' ' << afOWPS[i] << ' ' << afOOWPS[i] << std::endl;
			std::cout << std::setprecision(8);
			std::cout << std::fixed << 0.25 * afWPS[i][0] + 0.50 * afOWPS[i] + 0.25 * afOOWPS[i] << std::endl;
		}
	}

	in.close();

	return 0;
}
