#include <iostream>
#include <vector>
#include <string>

using namespace std;

void print_ret(int i, int ret) {
	cout << "Case #" << i << ": ";
	if (ret == 0) cout << "NO";
	else 
		cout << ret;
	cout << endl;
}

int abs(int i) {
	if (i < 0) return -i;
	else return i;
}

int main(void) { 
	int t, n;
	cin >> t;

	for (int i=0; i<t; i++) {
		cin >> n;
		vector<int> num;
		int digit = 60;
		vector<int> cnt(digit);
		for (int j=0; j<n; j++) {
			int k;
			cin >> k;
			num.push_back(k);
//			cout << k << endl;
		}

		for (int j=0; j<digit; j++) {
                  cnt[j] = 0;
		}

		int max = -1;
		for (int j=0; j<n; j++) {
                   int tmp = num[j];
		   for (int k=0; k<digit; k++) {
	              if ((tmp & 0x01) == 1) {
			cnt[k]++;
		      }
		      tmp = tmp >> 1;
		      if (max < k) max = k;
		      if (tmp == 0) break;
		   }
		}

		bool flg = true;
		for (int j=0; j<=max; j++) {
		  if ((cnt[j]%2) == 1) {
			  flg = false;
			  break;
		  }
		}

		if (flg) {
			sort(num.begin(), num.end());
			int ret =0;
			for (int j=1; j<num.size(); j++) {
				ret += num[j];
			}
			print_ret(i+1, ret);
		} else {
			print_ret(i+1, 0);
		}
	}
}


