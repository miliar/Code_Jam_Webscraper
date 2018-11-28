#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 900;
int x[maxn], y[maxn];

#define cin fin
#define cout fout

ifstream fin("a.in");
ofstream fout("a.out");

void mysort(int * a, int l)
{
	int i,j, tmp;
	for (i = 0;i < l;i ++)
		cin >> a[i];
	for (i = 0;i < l;i ++)
		for (j = i + 1;j < l;j ++)
			if (a[i] < a[j])
			{
				tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}
}

int main()
{
	int num = 0, t, n, i, ans;
	cin >> t;
	while (num < t)
	{
		num ++;
		cin >> n;
		mysort(x, n);
		mysort(y, n);
		ans = 0;
		for (i = 0;i < n;i ++) {
			//cout << x[i] << " " << y[n - i - 1] << endl;
			ans = ans + (x[i] * y[n - i - 1]);
		}
		cout << "Case #" << num << ": " << ans << endl;

	}
	fout.close();
	return 0;
}