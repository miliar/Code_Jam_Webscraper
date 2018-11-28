#include      <iostream>
#include      <fstream>
#include      <algorithm>
#include      <iomanip>

struct SWalkway {
	double fStart, fEnd;
	double fSpeed;
	bool operator<(const SWalkway &rhs) const{
		return fStart < rhs.fStart;
	}
};

class CSortRev{
	public:
		bool operator()(const SWalkway &lhs, const SWalkway &rhs) const{
			return lhs.fSpeed < rhs.fSpeed;
		}
};

int main(int argc, char **argv) {
	int nTests;
	double fCoridor, fWalkSpeed, fRunSpeed, fMaxRunTime;
	int nWalkways;
	SWalkway walkways[1001];
	double fCur;
	double fSum;

	std::ifstream in("in");
	in >> nTests;

	for (int nTest = 1; nTest <= nTests; ++nTest) {
		in >> fCoridor >> fWalkSpeed >> fRunSpeed >> fMaxRunTime >> nWalkways;


		for (int nWalkway = 0; nWalkway < nWalkways; ++nWalkway) {
			in >> walkways[nWalkway].fStart >> walkways[nWalkway].fEnd >> walkways[nWalkway].fSpeed;
		}

		std::sort(walkways, walkways + nWalkways);

		fSum = 0;
		if (nWalkways > 0) {
			fSum += walkways[0].fStart;
		}

		for (int nWalkway = 0; nWalkway < nWalkways; ++nWalkway) {
			walkways[nWalkway].fStart -= fSum;
			walkways[nWalkway].fEnd -= fSum;
			double fStart = (nWalkway + 1 < nWalkways) ? (walkways[nWalkway + 1].fStart) : fCoridor;
			fSum += fStart - (walkways[nWalkway].fEnd + fSum);
		}

		if (nWalkways > 0) {
			walkways[nWalkways].fStart = walkways[nWalkways - 1].fEnd;
		}else{
			walkways[nWalkways].fStart = 0;
		}

		walkways[nWalkways].fEnd = fCoridor;
		walkways[nWalkways].fSpeed = 0;


		for (int nWalkway = 0; nWalkway <= nWalkways; ++nWalkway) {
			std::cerr
				<< "[ " << walkways[nWalkway].fStart
				<< ", " << walkways[nWalkway].fEnd
				<< ", " << walkways[nWalkway].fSpeed
				<< " ], ";
		}
		std::cerr << std::endl;
		std::sort(walkways, walkways + nWalkways + 1, CSortRev());

		fCur = 0;

		for (int nWalkway = 0; nWalkway <= nWalkways; ++nWalkway) {
			double fBestRunSpeed = walkways[nWalkway].fSpeed + fRunSpeed;
			double fBestRunTime = ((walkways[nWalkway].fEnd - walkways[nWalkway].fStart) / fBestRunSpeed);

			//std::cerr << walkways[nWalkway].fSpeed + fRunSpeed<< std::endl;
			//std::cerr << fBestRunTime << std::endl;

			if (fMaxRunTime > 0 && fBestRunTime <= fMaxRunTime) {
				fCur += fBestRunTime;
				std::cerr << "Run for " << fBestRunTime << std::endl;
				fMaxRunTime -= fBestRunTime;
			}else if (fMaxRunTime > 0){
				walkways[nWalkway].fStart += fBestRunSpeed * fMaxRunTime;
				fCur += fMaxRunTime;
				//std::cerr << "Run h for: " << fMaxRunTime << std::endl;
				std::cerr << "New start: " << walkways[nWalkway].fStart << std::endl;
				fMaxRunTime = 0;
				--nWalkway;
			}else{
				double fBestWalkSpeed = walkways[nWalkway].fSpeed + fWalkSpeed;
				double fBestWalkTime = ((walkways[nWalkway].fEnd - walkways[nWalkway].fStart) / fBestWalkSpeed);

				fCur += fBestWalkTime;
				std::cerr << "walk for " << fBestWalkTime << std::endl;
			}
		}

		std::cout << "Case #" << nTest << ": " << std::fixed << std::setprecision(9) << fCur << std::endl;
	}

	in.close();

	return 0;
}
