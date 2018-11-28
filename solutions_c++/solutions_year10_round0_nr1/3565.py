#include <iostream>
using namespace std;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int n;
	int a,b;
	cin >> n;
	for (int i = 0;i < n;++i)
	{
		cin >> a >> b;
		cout << "Case #" << i + 1 << ": ";
		int k;
		for (k = 0;k < a;++k)
			if (!((b >> k) & 1))break;
		if (k == a)cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
	return 0;
}
