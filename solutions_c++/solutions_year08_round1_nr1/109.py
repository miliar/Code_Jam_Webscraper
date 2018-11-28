#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

typedef unsigned nat;
typedef long long int integer;

int main() {
	nat tc;
	cin >> tc;

	for (nat cs = 0; cs != tc; ++cs) {
		nat n;
		cin >> n;
		vector<integer> A(n), B(n);
		for (nat i = 0; i != n; ++i)
			cin >> A[i];
		for (nat i = 0; i != n; ++i)
			cin >> B[i];
		sort(A.begin(), A.end());
		sort(B.begin(), B.end(), greater<integer>());
		integer v = 0;
		for (nat i = 0; i != n; ++i)
			v+= A[i]*B[i];
		cout << "Case #" << (cs+1) << ": " << v << '\n';
	}

	return 0;
}


