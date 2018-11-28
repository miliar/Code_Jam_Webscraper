#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <cmath>

using namespace std;

std::pair<char, char> getKey(char a, char b) {
	if (a < b) return std::pair<char, char>(a, b);
	else return std::pair<char, char>(b, a);
}

void processCase(istream& in, ostream& out)
{
	std::map<std::pair<char, char>, char> combines;
	std::set<std::pair<char, char> > opposites;

	int c;
	in >> c;
	char buf[128];
	for (int i=0; i<c; i++) {
		in >> buf;
		buf[3] = 0;
		combines[getKey(buf[0], buf[1])] = buf[2];
	}

	int d;
	in >> d;
	for (int i=0; i<d; i++) {
		in >> buf;
		buf[2] = 0;
		opposites.emplace(getKey(buf[0], buf[1]));
	}

	int n;
	in >> n;
	in >> buf;
	buf[n] = 0;
	std::vector<char> result;
	for (int i=0; i<n; i++) {
		char elem = buf[i];
		if (!result.empty()) {
			std::map<std::pair<char, char>, char>::iterator iter = combines.find(getKey(result.back(), elem));
			if (iter != combines.end()) {
				result[result.size()-1] = iter->second;
				continue;
			}

			bool jump = false;
			for (size_t j=0; j<result.size(); j++) {
				if (opposites.find(getKey(result[j], elem)) != opposites.end()) {
					result.clear();
					jump = true;
					continue;
				}
			}
			if (jump) continue;
		}

		result.push_back(elem);
	}

	// Print result
	out << "[";
	for (size_t i=0; i<result.size(); i++) {
		if (i > 0) out << ", ";
		out << result[i];
	}
	out << "]";
}

int main()
{
	ifstream in("B-large.in");
	//ostream& out = cout;
	ofstream out("B-large.out", std::ios_base::out);

	int nCases;
	in >> nCases;
	for (int i=0; i<nCases; i++) {
		out << "Case #" << (i+1) << ": ";
		processCase(in, out);
		out << endl;
	}

	out.flush();
}
