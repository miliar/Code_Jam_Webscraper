#include <iostream>

#define f(x,y) for (int x = 0; x < y; ++x)

using namespace std;

int main() {
	int t;
	cin >> t;
	f(count,t) {
		int n;
		cin >> n;
		int num[n];
		f(i,n) num[i] = 0;
		f(i,n) f(j,n) {
			char c;
			cin >> c;
			if (c == '1') num[i] = j;
		}
		f(i,(n+1)*(n+1)) f(j,n) f(k,n) if(k > j) {
			if (num[j] == num[k]) ++num[k];
		}
		int sum = 0;
		f(i,(n+1)*(n+1)) for (int j = n-1; j >= 0; --j) {
			if (num[j] > j) {
				/*int k = j;
				while(num[k+1] > j) ++k;
				j = k;*/
				++sum;
				int tmp = num[j];
				num[j] = num[j+1];
				num[j+1] = tmp;
				//cout << j << endl;
				break;
			}
		}
		cout << "Case #" << (count+1) << ": " << sum << endl;
	}
	return 0;
}

