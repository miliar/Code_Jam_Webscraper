#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int T;
int p[1001],l[1001];
int order[1001];
double r[1001];
int n;

int main(){
	cin >>T;
	for (int times = 0; times < T; ++times){
		cin >> n;
		for (int i = 0 ;i <n;++i){
			cin >> l[i];
		}
		for (int i = 0; i<n;++i){
			cin >> p[i];
			order[i] = i;
			r[i] = double(p[i])/double(l[i]);
		}
		for (int i = 0; i < n-1; ++i){
			for (int j = n-1; j > i; --j) {
				if (r[order[j]] > r[order[j-1]]) {
					int tmp = order[j];
					order[j] = order[j-1];
					order[j-1] = tmp;
				}
			}
		}
		cout << "Case #" << times + 1 <<":";
		for (int i = 0; i < n; ++i) {
			cout << ' ' << order[i];
		}
		cout << endl;
	}
	return 0;
}