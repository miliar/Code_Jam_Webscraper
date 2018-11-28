#include <iostream>
#include <string>

using namespace std;




string dict[5011];
int l, d, n;

void Load()
{
	cin >> l >> d >> n;
	for (int i = 0; i < d; i++)
		cin >> dict[i];
}


bool can[21][257];

void Solve()
{
	int i, j, p, q;
	string s;
	bool isset;
	for (j = 0; j < n; j++)
	{
		cin >> s;
		memset(can, 0, sizeof(can));
		q = 0;
//		cerr << "set " << j << " " << s << "\n";
		isset = false;
		for (p = 0; p < (int)s.size(); p++)
		{
			if (s[p] == '(') isset = true;
			else if (s[p] == ')')
			{
				isset = false; q++;
			}
			else
			{
				can[q][(int)s[p]] = true;
//				cerr << q << " " << s[p] << "\n";
				if (!isset) q++;
			}        
		}

		q = 0;
		for (i = 0; i < d; i++)
		{
			for (p = 0; p < l; p++)
			{
				if (!can[p][(int)dict[i][p]]) break;
			}
			if (p == l) q++;
		}
		cout << "Case #" << j + 1 << ": " << q << "\n"; 

	}
}

int main()
{
	{
		Load();
		Solve();
	}
	return 0;
}
