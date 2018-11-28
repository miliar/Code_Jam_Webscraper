#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

bool v[810][11];
int d10[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
int bs[810][11];

int happyfy(int n, int k) {
	int b = 0;
	int m =0;
	do {
		b = b + (n % k) * d10[m];
		m++;
	} while(n /= k);
	//cout << b << endl;

	int s=0;
	while(b) {
		int t2 = (b%10);
		s += t2*t2;
		b /= 10;
	}
	return s;
}

int main()
{
	int b = 0;

    for(int i=2; i<=810; i++) {
		for(int k=2; k<=10; k++) {

			int t = i;
			for(int j=0; j<810 && !v[i][k]; j++) {
				t = happyfy(t, k);
				if (t==1) v[i][k] = true;
			}

		}
    }

	int t, tt=0;
	cin >> t;
	string ss;
	getline(cin, ss);


	while(tt++<t) {
		vector<int> ns;
		getline(cin, ss);
		istringstream cin2(ss);

		int n;
		while(cin2>>n)
			ns.push_back(n);

		for(int i=2; i<=100000000; i++) {
			bool flag = true;
			for(int j=0; j<ns.size(); j++)
				flag = flag && (i<=810 ? v[i][ns[j]] : v[happyfy(i,ns[j])][ns[j]]);

			if (flag) {
				cout << "Case #" << tt << ": " << i << endl;
				break;
			}
		}
	}

}
