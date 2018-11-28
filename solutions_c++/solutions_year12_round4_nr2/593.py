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
	cout << "Case #" << caseNumber << ":";
	for (size_t i = 0; i < ans.size(); i++) {
		cout << " " << ans[i].first << " " << ans[i].second;
	}
	cout << endl;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int n;
	int W;
	int L;
	cin >> n >> W >> L;
	vector< pair<int, int> > r(n);
	for (int i = 0; i < n; i++) {
		cin >> r[i].first;
		r[i].second = i;
	}
	sort(r.rbegin(), r.rend());
	
	vector< pair<int, int> > points(n, make_pair(-1, -1) );
	points[r[0].second].first = 0;
	points[r[0].second].second = 0;
	for (int i = 1; i < n; i++) {
		pair<int, int> nextPoint(-1, -1);
		for (int j = 0; j < i; j++) {
			pair<int, int> p1(points[r[j].second].first + r[j].first + r[i].first, points[r[j].second].second);
			
			if (p1.first >= 0 && p1.first <= W && p1.second >= 0 && p1.second <= L) {
				bool bad = false;
				for (int h = 0; h < i; h++) {
					if ( abs(p1.first - points[r[h].second].first) < r[i].first + r[h].first 
						&&  abs(p1.second - points[r[h].second].second) < r[i].first + r[h].first)
					{
						bad = true;
						break;
					}
				}
				if (!bad) {
					if (nextPoint.first == -1 || p1 < nextPoint) {
						nextPoint = p1;
					}
				}
			}
			pair<int, int> p2(points[r[j].second].first, points[r[j].second].second + r[j].first + r[i].first);
			
			if (p2.first >= 0 && p2.first <= W && p2.second >= 0 && p2.second <= L) {
				bool bad = false;
				for (int h = 0; h < i; h++) {
					if ( abs(p2.first - points[r[h].second].first) < r[i].first + r[h].first 
						&&  abs(p2.second - points[r[h].second].second) < r[i].first + r[h].first)
					{
						bad = true;
						break;
					}
				}
				if (!bad) {
					if (nextPoint.first == -1 || p2 < nextPoint) {
						nextPoint = p2;
					}
				}
			}
		}
		if (nextPoint.first == -1) {
			cerr << "Not found";
			return vector< pair<int, int> > ();
		}
		points[r[i].second] = nextPoint;
	}
	return points;
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
		PrintAnswerToTestCase(caseNumber, SolveTestCase< vector<pair<int, int> > >() );

	return 0;
}