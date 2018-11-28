#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <stdint.h>
#include <list>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
using namespace std;

int gcd (int a, int b)
{
	if (a == 0) 
		return b;
	else 
		return gcd(b%a, a);
}

void handleCase(int T)
{
	int N, Pd, Pg;
	cin >> N >> Pd >> Pg;
	cout << "Case #" << T + 1<< ": ";
	int n = gcd (Pd, 100);
	n = 100/n;
	if (n <= N) {
		if ((Pd !=100) && (Pg == 100)) {
			cout << "Broken" << endl;
		} else if ((Pd != 0) && (Pg == 0)) {
			cout << "Broken" << endl;
		} else {
			cout << "Possible" << endl;
		}
	} else {
		cout << "Broken" << endl;
	}
}

int main(int argc, char *argv[])
{
	int N;

	cin >> N;

	for (int i = 0; i < N; i++) {
		handleCase(i);
	}
	return 0;
}
