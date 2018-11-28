#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int L, D, N;
	cin >> L >> D >> N;
	//string str="()";
	//cout<<str<<endl;
	vector<string> vs(D);
	vector<string> test(N);
	for (int i = 0; i < D; ++i)
		cin >> vs[i];
	//cout<<vs[0]<<endl;
	for (int i = 0; i < N; ++i)
		cin >> test[i];
	//cout<<test[N-1]<<endl;
	for (int i = 0; i < N; ++i) {
		int K = 0;
		for (int j = 0; j < D; ++j) {
			bool flag = false;
			bool in = false;
			int k = 0;
			for (unsigned int l = 0; l < test[i].size(); ++l) {
				if ('(' == test[i][l]) {
					in = true;
					flag = false;
					//k++;
					continue;
				}
				if (')' == test[i][l]) {
					if (false == flag)
						break;
					in = false;
					k++;
					continue;
				}

				if (true == in) {
					if (vs[j][k] == test[i][l])
						flag = true;
					continue;
				}
				if (false == in && vs[j][k] != test[i][l])
					break;
				k++;
			}
			if (L == k)
				K++;
		}
		cout << "Case #" << i + 1 << ": " << K << endl;
	}
}
