#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	std::freopen("stdout.txt", "w", stdout);
	int totNum;
	ifstream mFile("A-large.in");
	mFile >> totNum;
	for (int i=0;i<totNum;i++) {
		long long Ans=0;
		int max,keynum,alpha,temp;
		mFile >> max >> keynum >> alpha;
		vector <int > freq;
		for (int j=0;j<alpha;j++) {
			mFile >>temp;
			freq.push_back(temp);
		};

		if (max*keynum<alpha) {
			cout << "Case #" << i+1 << ": Impossible" << endl;
		}
		else {
			sort(freq.rbegin(),freq.rend());
			for (int j=0;j<freq.size();j++)
				Ans+=freq[j]*(j/keynum+1);

			cout << "Case #" << i+1 << ": " << Ans << endl;
		}

	};
	return 0;
};