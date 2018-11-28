#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <ctime>

using namespace std;

double posX[1001];
double posY[1001];
int dist[1001];
int rev[1001];
int _W, _L;
vector<pair<int,int> > arms;

bool check(int idx, double nX, double nY, double allowedDist) {
	if ((posX[idx] - nX) * (posX[idx] - nX) + (posY[idx] - nY) * (posY[idx] - nY) >= allowedDist * allowedDist) {
		return true;
	}
	return false;
}

bool bt(int pos) {
	if (pos >= arms.size()) {
		return true;
	}
	bool state = false;
	int iter = 0;
	while (state == false && iter++ < 10000) {
		int rX = rand() % RAND_MAX;
		int rY = rand() % RAND_MAX;
		double tryX = ((double)rX) / RAND_MAX * _W;
		double tryY = ((double)rY) / RAND_MAX * _L;
		// check if ok
		bool passAll = true;
		for (int i = 0; i < pos; i++) {
			if (!check(i, tryX, tryY, dist[i] + dist[pos])) {
				passAll = false;
				break;
			}
		}
		if (!passAll) continue;
		// try
		posX[pos] = tryX;
		posY[pos] = tryY;
		bool stat = bt(pos+1);
		if (stat) {
			return true;
		}
	}
	return false;
}

int main() 
{
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, W, L;
		cin >> N >> W >> L;
		_W = W; _L = L;
		arms.clear();
		for (int i = 0; i < N; i++) {
			int val; cin >> val;
			arms.push_back(make_pair(val,i));
		}
		sort(arms.begin(), arms.end());
		reverse(arms.end(), arms.end());
		for (int i = 0; i < arms.size(); i++) {
			rev[arms[i].second] = i;
			dist[i] = arms[i].first;
		}
		// simulate 4 corners
		/*
		for (int i = 0; i < min(4, (int)arms.size()); i++) {
			if (i == 0) {
				posX[0] = 0.0;
				posY[0] = 0.0;
			} else if (i == 1) {
				posX[1] = W;
				posY[1] = L;
			} else if (i == 2) {
				posX[2] = W;
				posY[2] = 0.0;
			} else if (i == 3) {
				posX[3] = 0.0;
				posY[3] = L;
			}
		}
		*/
		bool s = bt(0);
		if (!s) {
			printf("FAILED\n");
		}
		printf("Case #%d: ",t);
		for (int i = 0; i < arms.size(); i++) {
			int idx = rev[i];
			if (i != 0) printf(" ");
			printf("%.6f %.6f", posX[idx], posY[idx]);
		}
		printf("\n");
		// cout << "\n";
	}
	return 0;
}