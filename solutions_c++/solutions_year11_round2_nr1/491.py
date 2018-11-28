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
	in.open("D://A-large.in");
	out.open("D://task.out");
	out.precision(20);
	int T;
	in >> T;
	for (int t = 1; t <= T; ++t) {
		int n;
		in >> n;
		vector<string> s(n);
		for (int i = 0; i < n; ++i) {
			string res;
			in >> s[i];
		}
		vector< pair<int,int> > winPlayed(n, make_pair(0,0));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (s[i][j] == '.') continue;
				winPlayed[i].second++;
				if (s[i][j] == '1') winPlayed[i].first++;
			}
		}
		vector<double> wp(n);
		vector<double> owp(n);
		vector<double> oowp(n);
		for (int i = 0; i < n; ++i) {
			wp[i] = winPlayed[i].first / double(winPlayed[i].second);
			double sum = 0;
			int op = 0;
			for (int j = 0; j < n; ++j) {
				if (i == j || s[i][j] == '.') continue;
				op++;
				if (winPlayed[j].second == 1) continue; 
				sum += (s[i][j] == '0') ? (winPlayed[j].first - 1) / double(winPlayed[j].second - 1) : winPlayed[j].first / double(winPlayed[j].second - 1) ;
			}
			owp[i] = sum / op;
		}

		for (int i = 0; i < n; ++i) {
			double sum = 0;
			int op = 0;
			for (int j = 0; j < n; ++j) {
				if (i == j || s[i][j] == '.') continue;
				op++;
				if (winPlayed[j].second == 1) continue; 
				sum += owp[j];
			}
			oowp[i] = sum / op;
		}
		out << "Case #" << t << ":";
		for (int i = 0; i < n; ++i)
			out << endl << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		out << endl;
	}
	return 0;

}