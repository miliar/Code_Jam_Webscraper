#include <iostream>
#include <string>

using namespace std;

string names[100];
int f[100], f1[100];

int main()
{
	int n, s, q;
	int i, testno, j, k;
	cin >> n;
	for (testno = 1; testno <= n; testno++)
	{
		cin >> s;
		string tmp;
		getline(cin, tmp);
		for (i = 0; i < s; i++)
			getline(cin, names[i]);
		cin >> q;
		getline(cin, tmp);
		memset(f, 0, sizeof(f));
		for (i = 0; i < q; i++)
		{
			getline(cin, tmp);
			for (j = 0; j < s; j++)
				if (tmp == names[j])
				{
					int last = f[j];
					f[j] = q + 1;
					for (k = 0; k < s; k++)
						if (k != j && f[k] > last + 1)
							f[k] = last + 1;
				}
		}
		int ans = q + 1;
		for (i = 0; i < s; i++)
			if (f[i] < ans)
				ans = f[i];
		cout << "Case #" << testno << ": " << ans << endl;
	}
}