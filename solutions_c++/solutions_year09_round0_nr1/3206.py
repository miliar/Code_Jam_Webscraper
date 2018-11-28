#include <iostream>
#include <string>

using namespace std;

const int MAX_D = 5004;
const int MAX_L = 17;

string dic[MAX_D];
bool f[MAX_L][30];
int l, d, n;

int main()
{
	cin >> l >> d >> n;
	for (int i = 0; i < d; ++i)
	{
		cin >> dic[i];
	}
	for (int i = 0; i < n; ++i)
	{
		string s;
		cin >> s;
		int j = 0, k = 0;
		memset(f, false, sizeof(f));
		while (j < s.length())
		{
			if (s[j] >= 'a' && s[j] <= 'z')
			{
				f[k++][s[j] - 'a'] = true;
				++j;
			}
			else
				if (s[j] == ')') 
				{	
					++j;
					++k;
				}
				else
					while (s[++j] != ')')
					{
						f[k][s[j] - 'a'] = true;
					}
		}
		int res = 0;
		for (int x = 0; x < d; ++x)
		{
			bool ok = true;
			for (int y = 0; y < dic[x].length(); ++y)
				if (!f[y][dic[x][y] - 'a'])
				{
					ok = false;
					break;
				}
				
			res += int(ok);
		}
		
		cout << "Case #" << i + 1 << ": " << res << endl;
	}
	return 0;
}

