#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <vector>
#include <map>
#include <list>
#include <cmath>

using namespace std;

void processCase(istream& in, ostream& out)
{
	int n;
	in >> n;

	int pos[2];
	pos[0] = 1;
	pos[1] = 1;
	int time[2];
	time[0] = 0;
	time[1] = 0;

	for (int i=0; i<n; i++) {
		char r;
		in >> r;
		int p;
		in >> p;

		int cur = r == 'O'? 0 : 1;

		time[cur] = max(abs(p - pos[cur]) + time[cur], time[1-cur]) + 1;
		pos[cur] = p;
	}

	// Print result
	out << max(time[0], time[1]);
}

int main()
{
	ifstream in("A-large.in");
	//ostream& out = cout;
	ofstream out("A-large.out", std::ios_base::out);

	int nCases;
	in >> nCases;
	char tmp[2];
	//in.getline(tmp, 2);
	for (int i=0; i<nCases; i++) {
		out << "Case #" << (i+1) << ": ";
		processCase(in, out);
		out << endl;
	}

	out.flush();
}
