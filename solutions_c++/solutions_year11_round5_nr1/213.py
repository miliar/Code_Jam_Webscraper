#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

template<class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
	cout << "Case #" << caseNumber << ":" << endl;
	for (int i = 0; i < ans.size(); i++) {
		cout.precision(18);
		cout << ans[i] << endl;
	}
}

struct Point {
	double x;
	double y;
	Point(double xx = 0, double yy = 0) {
		x = xx;
		y = yy;
	}
};

const double b = -1000;

double GetSquare(const vector<Point>& lower, const vector<Point>& upper) {
	double square = 0;
	for (int i = 0; i < upper.size() - 1; i++)
		square += (upper[i].y - b + upper[i + 1].y - b) * ( upper[i + 1].x - upper[i].x);

	for (int i = 0; i < lower.size() - 1; i++)
		square -= (lower[i].y - b + lower[i + 1].y - b) * ( lower[i + 1].x - lower[i].x);

	return square;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int width, m, n;
	int guests;
	cin >> width >> m >> n >> guests;

	vector<Point> lower(m);
	vector<Point> upper(n);
	for (int i = 0; i < m; i++) {
		cin >> lower[i].x >> lower[i].y;
	}

	for (int i = 0; i < n; i++) {
		cin >> upper[i].x >> upper[i].y;
	}

	double square = GetSquare(lower, upper) / guests;

	const double EPS = 1e-11; 
	vector<double> ans(guests - 1);
	vector<Point> lc;
	vector<Point> uc;
	lc.reserve(m);
	uc.reserve(n);
	for (int i = 0; i < guests - 1; i++) {
		double l = lower[0].x;
		double r = width;
		int pos1 = 0;
		int pos2 = 0;
		while (abs(r - l) > EPS) {
			double t = (r + l) / 2;
			pos1 = 0;
			pos2 = 0;
			lc.clear();
			uc.clear();
			for (; lower[pos1].x < t && pos1 < lower.size(); pos1++) 
				lc.push_back(lower[pos1]);
			for (; upper[pos2].x < t && pos2 < upper.size(); pos2++) 
				uc.push_back(upper[pos2]);
			lc.push_back(Point(t, lower[pos1 - 1].y + (t - lower[pos1 - 1].x) * (lower[pos1].y - lower[pos1 - 1].y) / (lower[pos1].x - lower[pos1 - 1].x) ));
			uc.push_back(Point(t, upper[pos2 - 1].y + (t - upper[pos2 - 1].x) * (upper[pos2].y - upper[pos2 - 1].y) / (upper[pos2].x - upper[pos2 - 1].x) ));
			double cur = GetSquare(lc, uc);
			if (cur > square) {
				r = t;
			} else {
				l = t;
			}
		}
		ans[i] = lc.back().x;
		vector<Point> nl;
		vector<Point> nu;
		nl.reserve(m);
		nu.reserve(n);
		nl.push_back(lc.back());
		nu.push_back(uc.back());
		for (int j = pos1; j < lower.size(); j++)
			nl.push_back(lower[j]);
		for (int j = pos2; j < upper.size(); j++)
			nu.push_back(upper[j]);
		upper = nu;
		lower = nl;
	}
	return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase< vector<double> >() );

	return 0;
}