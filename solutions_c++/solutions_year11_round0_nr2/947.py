#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const int AL = 256;

char cm[AL][AL];
bool dm[AL][AL];

int main()
{
	int t, tn = 1;

	cin >> t;

	while (tn <= t)
	{
		int c, d, n;
		char a, b, e;
		bool f;
		vector<char> ans;

		memset(cm, 0, sizeof(cm));
		memset(dm, 0, sizeof(dm));

		cin >> c;
		for (int i = 0; i < c; i++)
		{
			cin >> a >> b >> e;
			cm[a][b] = cm[b][a] = e;
		}

		cin >> d;
		for (int i = 0; i < d; i++)
		{
			cin >> a >> b;
			dm[a][b] = dm[b][a] = true;
		}

		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> a;
			ans.push_back(a);
			f = false;
			
			while (ans.size() > 1 && cm[ans[ans.size() - 1]][ans[ans.size() - 2]] != 0)
			{
				a = ans.back();
				ans.pop_back();
				ans.back() = cm[a][ans.back()];
				f = true;
			}

			if (!f)
				for (int i = ans.size() - 2; i >= 0; i--)
					if (dm[ans[ans.size() - 1]][ans[i]])
					{
						ans.clear();
						break;
					}
		}

		cout << "Case #" << tn << ": [";
		for (vector<char>::iterator it = ans.begin(); it != ans.end(); it++)
		{
			if (it != ans.begin())
				cout << ", ";
			cout << *it;
		}
		cout << "]\n";
		tn++;
	}

	return 0;
}
