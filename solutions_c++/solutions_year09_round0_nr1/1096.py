#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve()
{
	int L, D, N;
	cin >> L >> D >> N;
	string ss[5000];
	for (int i = 0; i < D; i++) cin >> ss[i];
	
	for (int i = 0; i < N; i++)
	{
		vector<int> p;
		string s;
		cin >> s;
		//cout << s << endl;
		int cur = 0;
		int op = 0;
		for (int j = 0; j < (int)s.length(); j++)
		{
			if (s[j] == '(') op = true;
			else
			{
				if (s[j] == ')')
				{
					p.push_back(cur); cur = 0; op = false;
				}
				else
				{
					if (op)
					{
						cur |= (1 << (s[j] - 'a'));
					}
					else
					{
						p.push_back(1 << (s[j] - 'a'));
					}
				}
			}
		}
		//for (int j = 0; j < p.size(); j++) cout << p[j] << ' ';
		//cout << endl;
		int res = 0;
		for (int j = 0; j < D; j++)
		{
			bool ok = true;
			for (int k = 0; k < L; k++) if (!(p[k] & (1 << (ss[j][k] - 'a')))) ok = false;
			if (ok) res++;
		}
		cout << "Case #" << i + 1 << ": " << res << endl;
	}
}

int main()
{
	solve();
	return 0;
}