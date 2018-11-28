#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 1000+5;
long a[maxn], n;

bool cmp(long x, long y)
{
	return x>y;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);

	long Sxor, Sum;
	int TextNum, Num = 0;
	cin >> TextNum;
	while (TextNum--) {
		cout << "Case #" << ++Num << ": ";
		cin >> n;
		Sxor = 0;
		for (int i = 0; i != n; ++i) {
			cin >> a[i];
			Sxor = Sxor^a[i];
		}
		sort(a,a+n,cmp);
		if (Sxor==0) {
			Sum = 0;
			for (int i = 0; i < n-1; ++i) Sum += a[i];
			cout << Sum << endl;
		} else cout << "NO" << endl;
	}

	return 0;
}