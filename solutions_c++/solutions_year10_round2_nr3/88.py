#include <algorithm>
#include <iostream>
#include <vector>
unsigned int choose_[512][512];
using namespace std;

static const unsigned int M = 100003;

struct F {
	unsigned int value;
	F() { }
	F(unsigned int value): value(value) { }
	F operator+(F x) const { return F((value+x.value)%M); }
	F operator*(F x) const { return F((unsigned int)(((unsigned long long)value*x.value)%M)); };
	F pow(F x) const {
		F res(1);
		F b(*this);
		while (x.value!=0) {
			if (x.value%2==1)
				res = res * b;
			x.value /= 2;
			b = b * b;
		}
		return res;
	}
	F inverse() const { return pow(M-2); }
	F operator/(F x) const { return (*this) * x.inverse(); }
	operator unsigned int() const { return value; }
};

static F choose(unsigned int n, unsigned int k) {
	int i=n, j=k;
	if (choose_[i][j] != -1) return choose_[i][j];
	F res = 1;
	for (unsigned int i=k+1; i<=n; i++)
		res = res * F(i);
	for (unsigned int i=2; i<=n-k; i++)
		res = res / F(i);
	return choose_[i][j] = res;
}

struct Test {
	vector<vector<F> > m;
	Test(unsigned int n): m(n+1) {
		for (unsigned int i=0; i<=n; i++) {
			m[i].resize(n+1);
			fill(m[i].begin(), m[i].end(), F(-1));
		}
	}
	unsigned int get(unsigned int n, unsigned int size);
};

unsigned int cc = 0;
unsigned int Test::get(unsigned int n, unsigned int size) {
//cerr << n << ' ' << size << endl;
	if (size==1)
		return 1;
	if (size>=n)
		return 0;
	F &res = m[n][size];
	if (res!=(unsigned int)-1)
		return res;
	res = 0;
	for (unsigned int rank=1; rank<size; rank++) {
		if (n-size-1>=size-rank-1) {
			F leftPart = get(size, rank);
			F rightPart = choose(n-size-1, size-rank-1);
			res = res + leftPart*rightPart;
		}
	}
	return res;
}

void runTest() {
	int n;
	cin >> n;
	Test test(n);
	F res = 0;
	for (int size=1; size<n; size++)
		res = res + F(test.get(n, size));
	cout << res.value << endl;
}

int main() {
	for (int i=0; i<512; i++)
		for (int j=0; j<512; j++)
			choose_[i][j] = -1;
	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
		cout << "Case #" << (i+1) << ": ";
		runTest();
		cerr << i << endl;
	}
	return 0;
}

