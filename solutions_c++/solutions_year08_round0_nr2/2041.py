
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
#define all(c)                 (c).begin(),(c).end()
#define forc(i,c)              for(int i=0;i<(c).size();i++)
#define F0R(i,N)               for(int i=0;i<N;++i)
#define forn(i,x,n)            for(int i=x;i<=(n);i++)
#define forit(it,c)            for(__typeof((c).begin()) it((c).begin());it!=(c).end();it++)

#define Vmax(vi)               *max_element (all(vi))
#define Vpb(vi,c)              vi.push_back(c)
template<class a, class b> a cst(b x) {stringstream s; s<<x; a r; s>>r; return r;}

/// end of templates & utils

enum TcTimeType {ttDepA, ttDepB, ttArrA, ttArrB};

struct TcTime {
	int time;
	TcTimeType typ;
	bool operator<(const TcTime& t) const {
		if(time != t.time)
			return time < t.time;
		else
			return typ > t.typ;
	}
};

int decodeTime(string s) {
	int pos = s.find(":", 0);
	int h = atoi((s.substr(0, pos)).c_str());
	int m = atoi((s.substr(pos + 1, 100)).c_str());
	return h*60 + m;
}

string func(ifstream &line) {
	int turnTime, AB_cnt, BA_cnt;
	vector<TcTime> times;
	string tmp;

	line >> turnTime;
	line >> AB_cnt;
	line >> BA_cnt;

	F0R(i,AB_cnt) {
		string stime;
		TcTime tt;

		line >> stime;
		tt.time = decodeTime(stime);
		tt.typ = ttDepA;
		times.push_back(tt);

		line >> stime;
		tt.time = decodeTime(stime) + turnTime;
		tt.typ = ttArrB;
		times.push_back(tt);
	}

	F0R(i,BA_cnt) {
		string stime;
		TcTime tt;

		line >> stime;
		tt.time = decodeTime(stime);
		tt.typ = ttDepB;
		times.push_back(tt);

		line >> stime;
		tt.time = decodeTime(stime) + turnTime;
		tt.typ = ttArrA;
		times.push_back(tt);
	}

	sort( times.begin(), times.end() );

	int trainReqA = 0;
	int trainReqB = 0;
	int onStationA = 0;
	int onStationB = 0;

	forc(i,times) {
		if (times[i].typ == ttDepA) {
			if (!onStationA)
				trainReqA++;
			else
				onStationA--;
		}
		if (times[i].typ == ttDepB) {
			if (!onStationB)
				trainReqB++;
			else
				onStationB--;
		}
		if (times[i].typ == ttArrA)
			onStationA++;
		if (times[i].typ == ttArrB)
			onStationB++;
	}
	string result;
	stringstream ss;
	ss << trainReqA << " " << trainReqB;
	getline(ss, result);
	return result;
}

int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("B-large.out", ios::out);

	int fileLen = 0;
	infile >> fileLen;
	for (int i = 0; i < fileLen; i++) {
		outfile << "Case #" << i+1 << ": " << func(infile) << endl;
	}

	outfile.close();

	return 0;
}
//---------------------------------------------------------------------------

