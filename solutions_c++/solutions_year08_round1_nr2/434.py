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
#include <algorithm>

typedef pair<int, bool> pref;
typedef set<pref> cust;
typedef set<cust> group;

void satisfy(const group &g, pref p, group &s) {
	for (group::const_iterator it=g.begin(); it!=g.end(); ++it) {
		if (it->find(p) == it->end())
			s.insert(*it);
	}
}

typedef set<int> malts;

int ScoreGroup(const group &g, int flav, int max, malts &m) {
	if (g.empty())
		return 0;
	if (flav == max)
		return -1;
	pref p1(flav,false), p2(flav,true);
	group g1, g2;
	satisfy(g, p1, g1);
	satisfy(g, p2, g2);
	malts m1;
	int s1 = ScoreGroup(g1, flav+1, max, m1);
	malts m2;
	int s2 = ScoreGroup(g2, flav+1, max, m2);
	if (s1 == -1) {
		if (s2 == -1)
			return -1;
		m.insert(flav);
		m.insert(m2.begin(), m2.end());
		return s2 + 1;
	}
	if (s2 == -1 || s1 < s2+1) {
		m.insert(m1.begin(), m1.end());
		return s1;
	}
	m.insert(flav);
	m.insert(m2.begin(), m2.end());
	return s2+1;
}

void ProcessCase(istream &is, int caseNum) {
	cout << "Case #" << caseNum << ": ";
	int N, M;
	is >> N;
	is >> M;
	set<cust> all;
	for (int i=0; i<M; ++i) {
		int numT;
		is >> numT;
		cust c;
		for (int j=0; j<numT; ++j) {
			int f,m;
			is >> f >> m;
			c.insert(make_pair<int,bool>(f,m?true:false));
		}
		all.insert(c);
	}
	malts m;
	int s=ScoreGroup(all, 1, N+1, m);
	if (s==-1)
		cout << " IMPOSSIBLE";
	else {
		for(int k=1; k<=N; ++k) {
			if (m.find(k)==m.end())
				cout << " 0";
			else
				cout << " 1";
		}
	}
	cout << "\n";
}
