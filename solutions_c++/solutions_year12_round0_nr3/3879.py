#include <cstdio>
#include <iostream>
#include <string>
#include <map>

using namespace std;


int log(int n) {
	int a = 0;

	do {
		n/=10;
		++a;
	} while (n > 0);

	return a;
}

int base(int n) {
	int a=1;
	for (int k = 0; k < n; k++) {
		a*=10;
	}
	return a;
}

static int LOG[2000001];
static int BASE[2000001];
static int marc[2000001];

int contRec(int n, int m, int id) {
	int N = LOG[n];
	int a = n, d;
	int c = 0;

	for (int i = 0; i <= N; ++i) {
		d = a % 10;
		a = d * (BASE[N]/10) + (a/10);

		if (a < 2000001){
			if (marc[a]!=id and a > n and a <=m){
				++c;
			}

			marc[a] = id;
		}
	}

	return c;
}

int main()
{
	LOG[0] = 1;
	BASE[0] = 10;

	for (int i = 1; i < 2000001; ++i) {
		marc[i] = -1;
		LOG[i] = log(i);
	}

	for (int i = 1; i < 10; ++i) {
		BASE[i] = base(i);
	}

	int T;
	int id = 0;
	int A, B;
	cin >> T;
	for (int c = 0; c < T; ++c) {
		cin>>A>>B;
		int ANS = 0;
		for (int i = A; i <= B; ++i){
			ANS += contRec(i, B, id);
			++id;
		}
		cout << "Case #" << c + 1 << ": " << ANS << endl;
		cerr << c<<endl;
	}
	return 0;
}
