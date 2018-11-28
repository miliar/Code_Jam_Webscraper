#include <iostream>
using namespace std;

string aa;
string bb;

void puts(int x)
{
	aa = "";
	while (x)
	{
		aa += '0' + x%10;
		x = x/10;
	}
	aa = aa + aa;
}

int main(void)
{
	freopen ("test.in", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int t;
	cin >> t;
	int a, b;
	int cnt;
	for (int x=1; x<=t; x++)
	{
		cout << "Case #" << x << ": ";
		cin >> a >> b;
		aa = "";
		bb = "";
		cnt = 0;
		for (int ii=a; ii <= b; ii++)
		{
			puts(ii);
			for (int jj=ii+1; jj<=b; jj++)
			{
				int tmp = jj;
				bb = "";
				while (tmp)
				{
					bb += '0' + tmp%10;
					tmp = tmp/10;
				}
				if ((int) (aa.find (bb)) != -1) cnt++;
			}
		}
		cout << cnt << endl;
	}
	return 0;
}
