#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
using namespace std;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

long long nextLong() {
	long long x;
	scanf("%I64d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

const int BUFSIZE = 1000000;
char buf[BUFSIZE + 1];
string nextString() {
	scanf("%s", buf);
	return buf;
}
string nextLine() {
	gets(buf);
	return buf;
}

int stringToInt(string s) {
	stringstream in(s);
	int x;
	in >> x;
	return x;
}

struct Point {
	typedef double T;
	T x, y;
	Point () : x(0), y(0) {}
	Point (T x, T y) : x(x), y(y) {}
	Point operator - (Point op) const { return Point(x - op.x, y - op.y); }
	Point operator + (Point op) const { return Point(x + op.x, y + op.y); }
	Point operator * (T op) const { return Point(x * op, y * op); }
	T operator * (Point op) const { return x * op.x + y * op.y; }
	T operator % (Point op) const { return x * op.y - y * op.x; }
	T length2() { return x * x + y * y; }
	double lengt() { return sqrt(length2()); }
};

Point nextPoint() {
	double x = nextDouble();
	double y = nextDouble();
	return Point(x, y);
}

typedef vector<vector<int> > Adj;

int main() {
	string sampleGooglerese = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	string sampleEnglish = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	vector<int> mapping(26, -1);
	for (int i = 0; i < sampleGooglerese.size(); ++i) {
		int x = sampleGooglerese[i] - 'a';
		int y = sampleEnglish[i] - 'a';
		mapping[x] = y;
	}
	mapping['q' - 'a'] = 'z' - 'a';
	mapping['z' - 'a'] = 'q' - 'a';

	string inp = nextLine();
	int T = stringToInt(inp);
	for (int cas = 1; cas <= T; ++cas) {
		inp = nextLine();
		for (int i = 0; i < inp.size(); ++i) {
			if (inp[i] != ' ') {
				inp[i] = mapping[inp[i] - 'a'] + 'a';
			}
		}
		printf("Case #%d: %s\n", cas, inp.c_str());
	}
	return 0;
}