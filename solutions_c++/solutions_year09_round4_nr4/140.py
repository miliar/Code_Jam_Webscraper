#include <iostream>
#include <utility>
#include <cmath>
using namespace std;
pair<pair<double, double>, double> data[3];
inline double dis(double x1, double y1, double x2, double y2){
	return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}
int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt < cases; ++tt){
		int n;
		cin >> n;
		double ans = 1000000000;
		for (int i = 0; i < n; ++i){
			double x, y, r;
			cin >> x >> y >> r;
			data[i] = make_pair(make_pair(x, y), r);
		}
		if (n == 1){
			ans = data[0].second;
		} else {
			if (n == 2){
				ans = max(data[0].second, data[1].second);
			} else {
				for (int i = 0; i < n; ++i){
					double t = data[i].second;
					double temp;
					switch (i){
						case 0:
							temp = dis(data[1].first.first, data[1].first.second,data[2].first.first, data[2].first.second);
							temp += data[1].second + data[2].second;
							break;
						case 1:
							temp = dis(data[2].first.first, data[2].first.second,data[0].first.first, data[0].first.second);
							temp += data[0].second + data[2].second;
							break;
						case 2:
							temp = dis(data[1].first.first, data[1].first.second,data[0].first.first, data[0].first.second);
							temp += data[1].second + data[0].second;
							break;
					}
					temp /= 2;
					t = max(t, temp);
					ans = min(ans, t);
				}
			}
		}
		printf("Case #%d: %lf\n", tt + 1, ans);
	}
	return 0;
}