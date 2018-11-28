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

long long gcd(long long a, long long b) {
	while (b != 0) {
		long long temp = a;
		a = b;
		b = temp % b;
	}
	return a;
}

bool cmp(const pair<int, pair<int,int> >& a, const pair<int, pair<int,int> >&  b) {
	return a.second.first < b.second.first;
}

bool cmp1(const pair<pair<double,double>, pair<int,int> >& a, const pair<pair<double,double>, pair<int,int> >&  b) {
	return a.first.second < b.first.second;
}

int main() {
	ifstream in;
	ofstream out;
	in.open("D://A-large.in");
	out.open("D://task.out");
	out.precision(40);
	int T;
	in >> T;
	for (int t = 1; t <= T; ++t) {
		int N;
		long long x, s, r, tt, n;
		in >> x >> s >> r >> tt >> n;
		vector<pair<long long, pair<long long,long long> > > ss(n);
		for (long long i = 0; i < n; ++i) {
			in >> ss[i].second.first >> ss[i].second.second >> ss[i].first;
		}		
		sort(ss.begin(), ss.end(), cmp);

		vector<pair< pair<double, double>, pair<long long,long long> > > spl;
		long long lastPos = 0;
		long long j = 0;
		for(long long i = 0; i < n; ++i) {
			if (lastPos < ss[i].second.first) {
				long long l = ss[i].second.first - lastPos;
				//spl.push_back(make_pair(make_pair(l / double(s) - l / double(r), 0), make_pair(lastPos, ss[i].second.first))); ++j;
				spl.push_back(make_pair(make_pair(double(s)/double(r), 0), make_pair(lastPos, ss[i].second.first))); ++j;
			}

			spl.push_back(make_pair(make_pair(0, ss[i].first), make_pair(ss[i].second.first, ss[i].second.second))); ++j;
			long long l = ss[i].second.second - ss[i].second.first;
			//spl[j-1].first.first = l / double(ss[i].first + s) - l / double(ss[i].first + r);
			spl[j-1].first.first = double(ss[i].first + s) / double(ss[i].first + r);
			lastPos = ss[i].second.second;
		}
		if (lastPos < x) { 
			long long l = x - lastPos;
			//spl.push_back(make_pair( make_pair(l / double(s) - l / double(r), 0), make_pair(lastPos, x)));
			spl.push_back(make_pair( make_pair( double(s) / double(r), 0), make_pair(lastPos, x)));
		}

		double res = 0;
		double runTime = 0;
		sort(spl.begin(), spl.end(), cmp1);
		for (long long i = 0; i < spl.size(); ++i) {
			if (runTime < tt && spl[i].first.first > 0) {
				double run = (spl[i].second.second - spl[i].second.first) / (spl[i].first.second + r);
				if (run + runTime <= tt) {
					res += run;
					runTime += run;
				}
				else {
					double run1 = tt - runTime;
					res += run1;
					double distr1 = run1 * (r + spl[i].first.second);
					res += (spl[i].second.second - spl[i].second.first - distr1) / (spl[i].first.second + s);
					runTime = tt;
				}
			}
			else {
				res += (spl[i].second.second - spl[i].second.first) / (spl[i].first.second + s);
			}
		}
		out << "Case #" << t << ": " << res << endl;

	}
	return 0;
}