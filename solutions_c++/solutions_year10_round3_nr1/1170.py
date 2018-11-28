#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool intx(double a, double b, double c, double d, double &res) {

}

int main() {
	int n;
	cin >> n;
	for (int z=1; z<=n; z++) {
		int N;
		cin >> N;
		vector<int> as(N), bs(N);
		long long ret= 0;
		for (int i=0; i<N; i++)
			cin >> as[i] >> bs[i];
		for (int i=0; i<N; i++)
			for (int j=i+1; j<N; j++) {
				//cout << as[i] << " " << bs[i] << " " << as[j] << " " << bs[j] << endl;
				if ((as[i] > as[j] && bs[i] < bs[j]) || (as[i] < as[j] && bs[i] > bs[j])) ret ++;
			}
		cout << "Case #" << z << ": " << ret << endl;
	}
}
