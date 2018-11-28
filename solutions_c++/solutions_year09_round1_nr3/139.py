#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

double C(int n,int k) {
	double res = 1;
	if (k > n or k <0)
		return 0;
	if (k > n - k)
		k = n - k;

	for (int i = n - k + 1;i <= n;i++)
		res *= i;
	for (int i = 1;i <= k;i++)
		res /= i;
	return res;
}
double prob(int c,int n,int m,int k) {

	return (double) C(m,n-k) * (double) C(c-m,k) / C(c,n);
}
int main(int argc, char **argv) {
	int n,c,T;
	cin >> T;

	for (int t = 1;t <= T;t++) {
		cin >> c >> n;
		vector<double> average(3 * c+1,0);
		average[c] = 0;
		for (int m = c - 1;m >= n;m--)
		{
			double sum = 1;
			for (int k = 1;k <= n;k++)
				sum += average[m + k] * prob(c,n,m,k);
			average[m] = sum / (1 - prob(c,n,m,0));
//			cout << average[m] << endl;

		}
		cout << "Case #" << t << ": " << average[n] + 1 << endl;

	}



}

