#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

typedef vector<int> vi;
typedef vector<double> vd;

#define PI 3.1415926535897932384626433832795

struct p
{
	int x, y;
};

int main()
{
	int cases;
	cin >> cases;
	for(int c = 0; c < cases; ++c) {
		
		int64 n, A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		vector<p> trees;

		p point;
		point.x = x0;
		point.y = y0;

		trees.push_back(point);

		for(int i = 0; i < n-1; ++i) {
			point.x = (A*point.x + B)%M;
			point.y = (C*point.y + D)%M;
			trees.push_back(point);
		}

		int sum = 0;
		for(int i = 0; i < trees.size(); ++i) {
			for(int j = i+1; j < trees.size(); ++j) {
				for(int k = j+1; k < trees.size(); ++k) {
					double x1 = (trees[i].x + trees[j].x + trees[k].x)/3.0;
					double y1 = (trees[i].y + trees[j].y + trees[k].y)/3.0;

					int64 x2 = (int64)x1;
					int64 y2 = (int64)y1;

					if((x1 > x2)||(y1 > y2)) continue;
					++sum;
				}
			}
		}

		cout << "Case #" << c+1 << ": " << sum << endl;
	}
	return 0;
}





