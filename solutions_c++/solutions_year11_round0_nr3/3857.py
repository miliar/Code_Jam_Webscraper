#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <iostream>
using namespace std;

int comp(const void* a, const void* b) { return ( *(int*)a - *(int*)b ); }

int n;
int c[1000], sum=0, xor=0;
int csum, xor1, xor2;

int find(int i)
{
	if (i==0) {
		csum = sum;
		xor1 = 0;
		xor2 = xor;
	}
	for (int j=i; j<n; j++) {
		csum -= c[j];
		xor1 ^= c[j];
		xor2 ^= c[j];
		if (xor1 == xor2)
			return csum;
		else {
			int ret = -1;
			if (j+1<n)
				ret = find(j+1);
			if (ret != -1)
				return ret;
			else {
				csum += c[j];
				xor1 ^= c[j];
				xor2 ^= c[j];
			}
		}
	}
	return -1;
}

int main()
{
//	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
//	freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);
	freopen("C-small-attempt1.in","r",stdin); freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);

//	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
//	freopen("C-small-practice.in","r",stdin); freopen("C-small-practice.out","w",stdout);
//	freopen("C-large-practice.in","r",stdin); freopen("C-large-practice.out","w",stdout);

	int t;
	cin >> t;

	for (int i=0; i<t; i++) {		
		cin >> n;

		sum=0, xor=0;
		for (int j=0; j<n; j++) {
			cin >> c[j];
			sum += c[j];
			xor ^= c[j];
		}

		qsort(c, n, sizeof(int), comp);

		int y = find(0);
		if (y == -1)
			cout << "Case #" << i+1 << ": " << "NO" << endl;
		else
			cout << "Case #" << i+1 << ": " << y << endl;
	}

	return 0;
}
