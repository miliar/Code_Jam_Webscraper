#include <iostream>
#include <sstream>
#include <vector>
#include <stdlib.h>
#include <queue>
#include <cmath>
#include <cstdio>

using namespace std;

int A;
int B;

void solve()
{
	long long ans = 0;	
	for (int n=A; n<B; n++) {
		int count = 0;
		int tmp = n;
		while (tmp) {
			count ++;
			tmp /= 10;
		}
		int a = n;
		int b = n;
		int ten = 1;
		for (int i=0; i<count-1; i++) ten*=10;
		for (int i=0; i<count-1; i++) {
			b = b / 10 + ten * (b % 10);
			if (a < b && b <= B) {
				//cout << a << " " << b << endl;
				ans ++;
			}
			if (a == b) break;
		}
	}
	cout << ans << endl;;
}


int main()
{
	int case_num;
	cin >> case_num;

	for (int t=1; t<=case_num; t++) {
		// initialization, IO
		cin >> A >> B;

		cout << "Case #" << t << ": ";
		solve();

	}
}
