#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<cmath>

#define ll long long


using namespace std;
int n;
double x[100], y[100], r[100];

double f(double x, double y, double r, double x1, double y1, double r1){
	return (sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1)) + r + r1) / 2.0;
}

double solve(){
	if (n == 1)
		return r[0];
	if (n == 2)
		return max(r[0], r[1]);
	

	double mini = max(f(x[0], y[0], r[0], x[1], y[1], r[1]), r[2]);
	mini = min(max(f(x[0], y[0], r[0], x[2], y[2], r[2]), r[1]), mini);
	mini = min(max(f(x[1], y[1], r[1], x[2], y[2], r[2]), r[0]), mini);
	return mini;

}

int main(){
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> x[i] >> y[i] >> r[i];
		double p = solve();
		cout << "Case #" << t+1 << ": " << p << endl;
	}
	return 0;
}