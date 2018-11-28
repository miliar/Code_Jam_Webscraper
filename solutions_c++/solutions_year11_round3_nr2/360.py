#include      <iostream>
#include      <algorithm>
#include      <string>
#include      <fstream>
#include      <list>
#include      <map>
#include      <iomanip>

using namespace std;

struct SPos{
	int nPos;
	double fValue;

	friend bool operator<(const SPos &lhs, const SPos &rhs){
		return lhs.fValue > rhs.fValue;
	}
};

long long anTimes[1000000];
double afRealTimes[1000000];
double afRealTimes2[1000000];
SPos aPos[1000000];

int main(int argc, char **argv) {
	int nTests;


	long long nTimes, nTakesToBuild, nStars, nBoosters;
	double fCurTime;
	long long nCanBuildFrom;

	std::ifstream in("in");
	in >> nTests;

	for (int nTest = 1; nTest <= nTests; ++nTest) {
		in >> nBoosters >> nTakesToBuild >> nStars >> nTimes;

		//cout << nBoosters << nTakesToBuild << endl;

		for (int i = 0; i < nTimes; ++i) {
			in >> anTimes[i];
		}

		nCanBuildFrom = -1;
		fCurTime = 0;

		for (int i = 0; i < nStars; ++i) {
			afRealTimes[i] = (anTimes[i % nTimes]) * 2;
			fCurTime += afRealTimes[i];
			afRealTimes2[i] = afRealTimes[i];

			if (fCurTime >= nTakesToBuild) {
				afRealTimes[i] /= 2;
				if (nCanBuildFrom == -1) {
					double tmp = static_cast<double>(nTakesToBuild - (fCurTime - afRealTimes[i] * 2)) / 2;
					afRealTimes[i] = (afRealTimes[i] + tmp);
					nCanBuildFrom = i;
				}
			}

			aPos[i].nPos = i;
			aPos[i].fValue = afRealTimes2[i] - afRealTimes[i];

		}

		sort(aPos, aPos + nStars);

		double fTime = 0;

		for (int i = 0; i < nBoosters; ++i) {
			fTime += afRealTimes[aPos[i].nPos];
			afRealTimes2[aPos[i].nPos] = 0;
		}
		for (int i = 0; i < nStars; ++i) {
			fTime += afRealTimes2[i];
		}

		cout << "Case #" << nTest << ": " << setprecision(0) << fixed << fTime << endl;
	}

	in.close();

	return 0;
}
