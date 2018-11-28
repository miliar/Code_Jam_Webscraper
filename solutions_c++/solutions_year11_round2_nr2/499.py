#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <queue>
#include <algorithm>
#include <iostream>
#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
using namespace std;

#define all(x) (x).begin(),(x).end()
#define sz(x) x.size()
#define ln(x) x.length()
#define forall(i,a,x) for(int i = a; i < sz(x); ++i)

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

template <typename T>
void printout(vector<T> x, string sep) {
	for (int i = 0; i < sz(x); ++i) {
		if ( i != 0 ) cout << sep;
		cout << x[i];
	}
}

template <typename R, typename S>
R convert(S a) {stringstream t;	t << a; R b; t >> b; return b; }

bool isSuff(string a, string b) {
	if (a.length() < b.length()) return false;
	return a.substr(a.length() - b.length(), b.length()) == b;
}

bool isPre(string a, string b) {
	if (a.length() < b.length()) return false;
	return a.substr(0, b.length()) == b;
}

vector<string> split(string str, string sep) {
	vector<string> res;
	int pos = -(int)sep.length();
	int oldPos = 0;
	while ((pos = str.find(sep, pos + sep.length())) != string::npos) {
		res.push_back(str.substr(oldPos, pos - oldPos));
		oldPos = pos + sep.length();
	}
	res.push_back(str.substr(oldPos, str.length() - oldPos));
	return res;
}


int main() {
	ifstream in;
	ofstream out;
	in.open("D://B-large.in");
	out.open("D://task.out");
	out.precision(20);
	int T;
	in >> T;
	for (int t = 1; t <= T; ++t) {
		int c;
		in >> c;
		long long d;
		in >> d;
		vector<long long> pts(c);
		vector<int> vs(c);
		for (int i = 0; i < c; ++i) {
			long long p, v;
			in >> pts[i] >> vs[i];
		}
		sort(all(pts));
		long long res = 0;
		long long lastCoord = pts[0] + (vs[0] - 1)*d;
		long long maxMove = (vs[0] - 1)*d;
		long long count = 1;
		for (int i = 1; i < pts.size(); ++i) {
			long long move = d - (pts[i] - lastCoord);
			if (move < 0) move = 0;
			move += (vs[i] - 1)*d;
			if (move == maxMove) count++;
			if (move > maxMove) { maxMove = move; count = 1; }
			lastCoord = pts[i] + move;
		}
		out.precision(20);
		out << "Case #" << t << ": " << (maxMove / double(2.0)) << endl;
	}
	return 0;

}