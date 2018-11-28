#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

bool maior(int a, int b)
{
	return (a > b);
}

int main()
{
	int cases;
	cin >> cases;
	for(int c = 0; c < cases; ++c) {
		int size;
		cin >> size;
		vector<int> a, b;
		a.clear();
		b.clear();

		for(int i = 0; i < size; ++i) {
			int qq;
			cin >> qq;
			a.push_back(qq);
		}

		for(int i = 0; i < size; ++i) {
			int qq;
			cin >> qq;
			b.push_back(qq);
		}

		sort(a.begin(), a.end(), maior);
		sort(b.begin(), b.end(), maior);

		int scalar = 0;
		for(int i = 0; i < size; ++i) {
			scalar += a[i]*b[size-i-1];
		}

		cout << "Case #" << c+1 << ": " << scalar << endl;
	}
	return 0;
}




