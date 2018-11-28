#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int ti = 0; ti < t; ti++){
		int n;
		cin >> n;
		vector<int> as, bs;
		for(int i = 0; i < n; i++){
			int a, b;
			cin >> a >> b;
			as.push_back(a);
			bs.push_back(b);
		}
		int sum = 0;

		for(int i = 0; i < n - 1; i++){
			for(int l = i + 1; l < n; l++){
				int l1 = as[i] - as[l];
				int l2 = bs[i] - bs[l];
				l1 = l1 / abs(l1);
				l2 = l2 / abs(l2);
				if(l1 != l2){
					sum++;
				}
			}
		}

		cout << "Case #" << (ti+1) << ": " << sum << endl;
	}
}
