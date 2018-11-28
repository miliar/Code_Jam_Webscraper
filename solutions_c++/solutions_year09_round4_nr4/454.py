#include <iostream> 
#include <sstream> 
#include <cstdlib> 
#include <cstdio> 
#include <cmath> 
#include <memory.h> 
#include <cstring> 
#include <string> 
#include <vector> 
#include <list> 
#include <stack> 
#include <queue> 
#include <map> 
#include <algorithm> 
#include <functional> 
using namespace std; 

template<class T> 
inline T MAX(const T& a, const T& b) {return (a>=b)?a:b;} 
template<class T> 
inline T MIN(const T& a, const T& b) {return (a<=b)?a:b;} 

double needR(int x1, int y1, int r1, int x2, int y2, int r2)
{
	double res = sqrt((double)((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))) + r1 + r2;
	return res / 2.0;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <=T; t++) {
		int n;
		scanf("%d", &n);
		vector<pair<pair<int, int>, int > > plants;
		for (int i = 0; i < n; i++) {
			int x, y, r;
			scanf("%d%d%d", &x, &y, &r);
			plants.push_back(make_pair(make_pair(x, y), r));
		}
		double res = 0;
		if (n <= 2) {
			int maxR = 0;
			for (int i = 0; i < n; i++) maxR = MAX(maxR, plants[i].second);
			res = maxR;
		}
		else {
			res = 1e10;
			res = MIN(res, MAX(needR(plants[0].first.first, plants[0].first.second, plants[0].second, plants[1].first.first, plants[1].first.second, plants[1].second), (double)plants[2].second));
			res = MIN(res, MAX(needR(plants[1].first.first, plants[1].first.second, plants[1].second, plants[2].first.first, plants[2].first.second, plants[2].second), (double)plants[0].second));
			res = MIN(res, MAX(needR(plants[2].first.first, plants[2].first.second, plants[2].second, plants[0].first.first, plants[0].first.second, plants[0].second), (double)plants[1].second));
		}
		printf("Case #%d: %.10lf\n", t, res);
	}
	return 0;
}
