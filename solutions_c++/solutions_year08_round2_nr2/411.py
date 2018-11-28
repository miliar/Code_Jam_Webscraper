#include <fstream>
#include <iostream>
#include <strstream>
#include <string>
#include <vector>

using namespace std;

void eol(istream &is) {
	string str;
	getline(is, str);
}

template <typename T>
T GetOneInALine(istream &inStream) {
	T toReturn;
	inStream >> toReturn;
	eol(inStream);
	return toReturn;
}

template <typename T>
vector<T> GetAllInALine(istream &inStream) {
	string line;
	getline(inStream, line);
	istrstream lineStream(line.c_str());
	vector<T> toReturn;
	T toAdd;
	while (!lineStream.eof()) {
		lineStream >> toAdd;
		toReturn.push_back(toAdd);
	}
	return toReturn;
}

void ProcessCase(istream &is, int caseNum);

int Run(istream &inStream) {
	int numLines=0;
	numLines = GetOneInALine<int>(inStream);
	for (int i=0; i<numLines; ++i) {
		cerr << "Processing case " << i+1 << "\n";
		ProcessCase(inStream, i+1);
	}
	return 0;
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return Run(cin);
	else {
		ifstream inStream(argv[1]);
		return Run(inStream);
	}
}

#include <set>
typedef set<int> Set;
typedef set<Set> SetS;
#include <math.h>
typedef long long quad;
bool IsPrime(quad n) {
	for (quad i=2; i*i<=n; ++i) {
		if (n%i==0)
			return false;
	}
	return true;
}

void ProcessCase(istream &is, int caseNum) {
	cout << "Case #" << caseNum << ": ";
	quad A, B, P;
	is >> A >> B >> P;

	vector<quad> setVec((unsigned)B-(unsigned)A+1);
	for (int id=0; id<(int)B-A+1; ++id) {
		setVec[id]=id;
	}
	for (quad p=P; p<=B-A; ++p) {
		if (IsPrime(p)) {
			quad start=(A%p==0) ? A : A+p-(A%p);
			quad source = setVec[(int)(start-A)];
			for (quad it=start+p; it<=B; it += p) {
				// Merge
				quad target = setVec[it-A];
				for (int id1=0; id1<(int)(B-A+1); ++id1) {
					if (setVec[id1]==target){
						setVec[id1] = source;
					}
				}
			}
		}
	}
	set<quad> s(setVec.begin(), setVec.end());
	cout << s.size() << "\n";
}
