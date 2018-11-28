#include <fstream>

using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("A-small.in");
	fout.open("snapper.out");
	int T;
	fin >> T;
	int n, k;
	bool power[32]; // true if there's power
	bool snapper[32]; // true if on
	for (int i=0; i!=T; ++i) {
		fin >> n >> k;
		if (k<n) {
			fout << "Case #" << i+1 << ": OFF" << endl;
			continue;
		}
		for (int j=0; j!=n+1; ++j) snapper[j]=power[j]=false;
		power[0]=true;
		for (int j=0; j!=k; ++j) {
			for (int l=0; l!=n; ++l) {
				if (power[l]) snapper[l]=!snapper[l];
			}
			for (int l=1; l!=n+1; ++l) {
				power[l]=((snapper[l-1] && power[l-1]) ? true : false);
			}
		}
		fout << "Case #" << i+1 << ": " << (power[n] ? "ON" : "OFF") << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
