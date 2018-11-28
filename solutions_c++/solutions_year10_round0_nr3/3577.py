#include <fstream>

using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("C-small-attempt4.in");
	fout.open("theme_park.out");
	int T;
	fin >> T;
	int groupSize[1002];
	int r; // number of times the roller coaster is run
	int n; // number of groups
	int k; // roller coater limit
	int profit;
	int round;
	int groupInd;
	int origGroup;
	//int tempProfit;
	int tempSize;
	for (int i=0; i!=T; ++i) {
		profit=groupInd=round=0;
		fin >> r >> k >> n;
		for (int j=0; j!=n; ++j) fin >> groupSize[j];
		while (round<r) {
			++round;
			tempSize=0;
			origGroup=groupInd;
			while (tempSize+groupSize[groupInd]<=k) {
				tempSize+=groupSize[groupInd];
				++groupInd;
				if (groupInd==n) groupInd=0;
				if (origGroup==groupInd) break;
			}
			profit+=tempSize;
		}
		fout << "Case #" << i+1 << ": " << profit << endl;
	}
	fin.close();
	fout.close();
	return 0;
}