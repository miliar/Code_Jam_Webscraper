#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	vector<string> mat;
	int cn, t, n, i, j, k, ans;
	bool sk;

	cin >> t;
	mat.resize(40);
	for (cn = 1; cn <= t; cn++)
	{
		ans = 0;
		cin >> n;
		for (i = 0; i < n; i++)
			cin >> mat[i];

		for (i = 0; i < n; i++)
		{
			sk = true;
			for (k = i + 1; k < n; k++)
				if (mat[i][k] == '1')
					sk = false;

			if (sk)
				continue;

			for (j = i + 1; j < n; j++)
			{
				sk = true;
				for (k = i + 1; k < n; k++)
					if (mat[j][k] == '1')
						sk = false;
				if (sk)
					break;
			}

			for (k = j; j > i; j--)
			{
				swap(mat[j], mat[j - 1]);
				ans++;
			}
		}
		cout << "Case #" << cn << ": " << ans << endl;
	}

	return 0;
}
