#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <ctime>
using namespace std;

typedef long long i64;

const int INF = ~(1 << 31);
const double EPS = 1e-5;
const int MAXN = 1000;
//const int n = 5;
const double lambda = 1e-5;

double knorm(vector<double> & a);
vector<double> zeidel(vector<vector<double> > & A, vector<double> & B);
double solve(double x0, vector<double> & x, vector<double> & y, vector<double> & m);

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	vector<vector<double> > A(n, vector<double>(n));
	vector<double> B(n), x(n), y(n);
	for(int i = 0; i < n; i++) cin >> x[i];
	for(int i = 0; i < n; i++) cin >> y[i];
	double x0, h = x[1] - x[0];
	cin >> x0;
	A[0][0] = A[n - 1][n - 1] = 2;
	A[0][1] = A[n - 1][n - 2] = 1;
	B[0] = (y[1] - y[0]) * 3 / h;
	B[n - 1] = (y[n - 1] - y[n - 2]) * 3 / h;
	for (int i = 1; i < n - 1; i++) {
		A[i][i] = 4;
		A[i][i - 1] = A[i][i + 1] = 1;
		B[i] = (y[i + 1] - y[i - 1]) * 3 / h;
	}
	cout << solve(x0, x, y, zeidel(A, B)) << endl;
	return 0;
}

double knorm(vector<double> & a){
	double sum = 0;
	for(int i = 0; i < a.size(); i++) sum += a[i] * a[i];
	return sqrt(sum);
}

vector<double> zeidel(vector<vector<double> > & A, vector<double> & B){
	int n = B.size();
	double mx = -1, temp = 0;
	for(int i = 0; i < n; i++, temp = 0){
		for(int j = 0; j < n; j++)
			if(i != j) temp += fabs(A[i][j]);
		if(temp > fabs(A[i][i])) {
			cout << "Sufficient convergence condition is not performed." << endl;
			break;
		}
	}
	for(int i = 0; i < n; i++, temp = 0){
		temp = A[i][i];
		B[i] /= temp;
		for(int j = 0; j < n; j++)
			A[i][j] = ((j == i) ? 0 : (- A[i][j] / temp));
	}
	for(int i = 0; i < n; i++, temp = 0){
		for(int j = 0; j < n; j++) 
			temp += fabs(A[i][j]);
		mx = max(mx, temp);
	}
	if(!(mx < 1)){
		cout << "Convergence condition is not performed." << endl;
		cout << "Check your input." << endl;
		return vector<double>();
	}
	vector<double> X_cur(n), X_prev(n);
	for(int i = 0; i < n; i++) 
		X_cur[i] = B[i];
	do{
		for(int i = 0; i < n; i++) X_prev[i] = X_cur[i];
		for(int i = 0; i < n; i++, temp = 0){
			for(int j = 0; j < n; j++){
				temp += A[i][j] * X_cur[j];
			}
			X_cur[i] = temp + B[i];
		}
	}while(fabs(knorm(X_cur) - knorm(X_prev)) > EPS);
	return X_cur;
}

double solve(double x0, vector<double> & x, vector<double> & y, vector<double> & m){
	double h = x[1] - x[0];
	int i = 0;
	for (; i < x.size() - 1; i++) {
		if (x0 >= x[i] && x0 <= x[i + 1]) break;
	}
	//return 0;
	return (pow(x[i + 1] - x0, 2.0) * (2 * (x0 - x[i]) + 1) * y[i] / (h * h * h) + pow(x0 - x[i], 2.0) * (2 * (x[i + 1] - x0) + 1) * y[i + 1] / (h * h * h) + pow(x[i + 1] - x0, 2.0) * (x0 - x[i]) * m[i] / (h * h) + pow(x0 - x[i], 2.0) * (x0 - x[i + 1]) * m[i + 1] / (h * h));
}
