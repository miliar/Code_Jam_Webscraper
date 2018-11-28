#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <map>
#include <cmath>
#include <sstream>
using namespace std;

typedef long long LL;
typedef unsigned int UINT32;

vector<pair<int,int> > birds;
vector<pair<int,int> > no;

int minh, maxh;
int minw, maxw;

/*
int calc(int h, int w)
{
	int i;

	pair<int,int> cur(h,w);

	if (birds.size() == 0) {
		for (i=0; i<no.size(); ++i) {
			if (no[i] == cur) return 0;
		}

		return 2;
	}

	if (maxh == -1) {
		return 2;
	}

	if (h>=minh && h<=maxh) return 1;

	int i;
	if (h < minh) {
		for (i=0; i<noh.size(); ++i) {
			if (noh[i] > maxh) continue;

		}
	}
}
*/

bool canno(int h, int w)
{
	if (birds.size() == 0) return true;

	if (h>=minh && h<=maxh && w>=minw && w<=maxw) return false;

	return true;
}

bool canbird(int h, int w)
{
	int myminh = minh;
	int mymaxh = maxh;
	int myminw = minw;
	int mymaxw = maxw;

	if (h < myminh) myminh = h;
	if (h > mymaxh) mymaxh = h;
	if (w < myminw) myminw = w;
	if (w > mymaxw) mymaxw = w;

	int i;
	pair<int,int> cur(h,w);
	for (i=0; i<no.size(); ++i) {
		if (cur == no[i]) return false;
		if (no[i].first>=myminh && no[i].first<=mymaxh && \
				no[i].second>=myminw && no[i].second<=mymaxw) return false;
	}

	return true;
}

int main(void)
{
	int cases;
	cin >> cases;

	int i;
	for (int c=1; c<=cases; ++c) {
		int N;
		cin >> N;
		int h, w;
		string b;
		birds.clear();
		no.clear();
		for (i=0; i<N; ++i) {
			cin >> h >> w >> b;
			if (b == "BIRD") {
				birds.push_back(make_pair(h,w));
			} else {
				cin >> b;
				no.push_back(make_pair(h,w));
			}
		}

		minh = 0x7fffffff;
		minw = 0x7fffffff;
		maxh = -1;
		maxw = -1;
		for (i=0; i<birds.size(); ++i) {
			if (birds[i].first < minh) minh = birds[i].first;
			if (birds[i].first > maxh) maxh = birds[i].first;
			if (birds[i].second < minw) minw = birds[i].second;
			if (birds[i].second > maxw) maxw = birds[i].second;
		}

		cout << "Case #" << c << ":" << endl;

		int M;
		cin >> M;
		for (i=0; i<M; ++i) {
			cin >> h >> w;
			bool b1 = canbird(h, w);
			bool b2 = canno(h, w);
			string s;
			if (b1 && b2) {
				s = "UNKNOWN";
			} else if (b1) {
				s = "BIRD";
			} else {
				s = "NOT BIRD";
			}
			cout << s << endl;
		}
	}

	return 0;
}
