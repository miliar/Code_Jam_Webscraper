#include <iostream>
#include <sstream>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <fstream>

using namespace std;

const int MAX = 1000;

int arr[MAX];

int main () {

	ifstream in("A.in");
	ofstream out("A.out");
	int cases;
	in >> cases;
	for (int c = 0; c < cases; c++) {
		unsigned long long p, k ,l;
		in >> p >> k >> l;
		for (int i = 0; i < l; i++) {
			in >> arr[i];
		}
		sort(arr, arr + l);
		unsigned long long res = 0;
		for (unsigned long long i = 0, pos = l - 1; i < l; i++, pos--) {
			res += arr[pos] * ((i / k) + 1);
			//cout << arr[pos] << " " << res << endl;
		}
		//system("pause");
		out << "Case #" << (c + 1) << ": " << res << endl;
		//out << res << endl;
	}
	in.close();
	out.close();
	return 0;

}