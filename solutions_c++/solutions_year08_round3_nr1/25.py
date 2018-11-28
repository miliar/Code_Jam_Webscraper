#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "in.txt"
#define OUTPUT "out.txt"

long long s[1001], tmp;

void Quick(int b, int e)
{
	int i = b, j = e;
	long long X = s[(e+b)/2];
	while (i<=j) {
		while (s[i] > X) i++;
		while (s[j] < X) j--;

		if (i<=j) {
			tmp = s[j];
			s[j] = s[i];
			s[i] = tmp;

			i++;
			j--;
		}
	}
	if (i<e) Quick(i,e);
	if (b<j) Quick(b,j);
}

int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;
	for (int i=0; i<t; i++) {
		int p,k,l; cin >> p >> k >> l;
		for (int u=0; u<l; u++) cin >> s[u];
		if (l>0) Quick(0,l-1);
		long long sum = 0;
		long long mn=1;
		for (int u=0; u < l; u++) {
			sum += s[u]*mn;
			if ( (u+1)%k == 0 ) mn++;
		}
		cout << "Case #" << i+1 << ": " << sum << endl;
	}
	return 0;
}