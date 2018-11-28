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

#include <algorithm>
#include <deque>

int prod(const vector<int> &x, const vector<int> &y) {
	int prod=0;
	for (unsigned i=0; i<x.size(); ++i)
		prod += x[i]*y[i];
	return prod;
}

int lprod(const vector<int> &x, vector<int> y) {
	int toReturn = 0;
	for (unsigned i=0; i<x.size(); ++i) {
		int lj=0, cur = x[i]*y[0];
		for (unsigned j=1; j<y.size(); ++j) {
			if (x[i]*y[j] < cur) {
				cur = x[i]*y[j];
				lj = j;
			}
		}
		y.erase(y.begin()+lj);
		toReturn += cur;
	}
	return toReturn;
}

bool abscomp(int x, int y) {
	return x*x < y*y;
}

void ProcessCase(istream &is, int caseNum) {
	cout << "Case #" << caseNum << ": ";
	int vSize, j;
	is >> vSize;
	vector<int> x(vSize), y(vSize);
	for (j=0; j<vSize; ++j) {
		int n;
		is >> n;
		x[j]=n;
	}
	for (j=0; j<vSize; ++j) {
		int n;
		is >> n;
		y[j]=n;
	}
	sort(x.rbegin(), x.rend(), abscomp);
	cout << lprod(x,y) << "\n";
}
