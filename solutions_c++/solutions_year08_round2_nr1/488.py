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

typedef long long quad;

typedef pair<quad, quad> point;
#include <set>
typedef set<point> pts;

void ProcessCase(istream &is, int caseNum) {
	cout << "Case #" << caseNum << ": ";
	quad n, A, B, C, D, x0, y0, M;
	is >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
	pts allPts;
	quad X=x0, Y=y0;
	for (int i = 0; i<n; ++i) {
		allPts.insert(point(X,Y));
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
	}
	vector<point> ptv(allPts.begin(), allPts.end());
	int hit=0;
	for (unsigned j=0; j<ptv.size(); ++j) {
		for (unsigned k=j+1; k<ptv.size(); ++k) {
			for (unsigned l=k+1; l<ptv.size(); ++l) {
				if ((ptv[j].first+ptv[k].first+ptv[l].first)%3 == 0 && (ptv[j].second+ptv[k].second+ptv[l].second)%3==0)
					++hit;
			}
		}
	}

	cout << hit << "\n";
}
