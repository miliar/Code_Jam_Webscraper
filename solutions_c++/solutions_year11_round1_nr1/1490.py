#include <string>
#include <vector>
#include <iterator>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <algorithm>
#include <fstream>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <math.h>
using namespace std;

string getLine() {
        string res;
        getline(cin, res);
        return res;
}

vector<string> getLineFields() {
        string line = getLine();
        stringstream str;
        str << line;
        vector<string> fields;
        string temp;
        while(str>>temp)
        {
                fields.push_back(temp);
        }
        return fields;
}

template <typename S, typename R>
R convert(S a) { stringstream t; t << a; R b; t >> b; return b; }

int gcd (int a, int b) {
	while (b != 0) {
		int temp = a;
		a = b;
		b = temp % b;
	}
	return a;
}

int main() {
	string fname = "C:\\A-small-attempt1.in";
	string outname = "C:\\test.out";
	ifstream in;
	ofstream out;
	in.open(fname);
	out.open(outname);

	int T;
	in >> T;
	for (int i=0; i < T; ++i) {
		int N, pd, pg;
		in >> N >> pd >> pg;
		bool lost, win;
		lost = pd < 100;
		win = pd > 0;
		int minPlayed = 100 / gcd(pd, 100);
		if ((minPlayed > N) || (lost && (pg == 100)) || (win && (pg == 0))) 
			out << "Case #" << i+1 << ": Broken" << endl;
		else 
			out << "Case #" << i+1 << ": Possible" << endl;
	}
	in.close();
	out.close();
	return 0;
}