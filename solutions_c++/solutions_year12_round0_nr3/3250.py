#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

bool haveDifferentCharacters(string A, string B) {
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());

	return A.compare(B) != 0;
}

bool pairValid(int n, int m) {
	stringstream sn;
	sn<<n;
	string nString = sn.str();

	stringstream sm;
	sm<<m;
	string mString = sm.str();

	if(!haveDifferentCharacters(nString, mString)) {
		// check if m can be obtained by moving n characters towards front
		for(size_t movedChars = 1; movedChars < nString.length(); movedChars++){
			string temp = "";
			temp.append(nString.end() - movedChars, nString.end());
			temp.append(nString.begin(), nString.end() - movedChars);

			if(temp.compare(mString) == 0)
				return true;
		}
	}

	return false;
}

int computeRecycledPairs(int A, int B) {
	int pairs = 0;

	for(int n = A; n < B; n++) {
		for(int m = n + 1; m <= B; m++) {
			if(pairValid(n, m)) {
				//cout<<n<<" & "<<m<<endl;
				pairs++;
			}
		}
	}

	return pairs;
}

int main(int argc, char** argv) {
	ifstream in("input.in");
	ofstream out("out.txt");

	size_t T;
	in>>T;

	for(size_t i = 0; i < T; i++) {
		int A, B;
		in>>A>>B;

		int y = computeRecycledPairs(A, B);

		out<<"Case #"<<(i+1)<<": "<<y<<endl;
	}

	in.close();
	out.close();

	return 0;
}
