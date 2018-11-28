#include <iostream>
#include <string>
#include <cstring>

#define EL 5000

using namespace std;

string el[EL+1];
char tem[15][26] = {0,};
int main()
{
	string sr;
	long word_cnt, len, n;
	cin >> len >> word_cnt >> n;
	long y, j, z;
	for(y = 0; y < word_cnt; y++)
	{
		cin >> el[y];
	}
	for(y = 0; y < n; y++)
	{
		memset(tem, 0, sizeof(tem));
		cin >> sr;
		long pos = 0;
		for(j = 0; j < sr.size(); j++)
		{
			if (sr[j] != '(')
			{
				tem[pos][sr[j]] = 1;
			}
			else
			{
				j++;
				for(; sr[j] != ')'; j++)
				{
					tem[pos][sr[j]] = 1;
				}
			}
			pos++;
		}
		// reading complete
		long ans = 0;
		for(j = 0; j < word_cnt; j++)
		{
			long flag = 1;
			for(z = 0; z < len; z++)
			{
				if (!tem[z][el[j][z]])
				{
					flag = 0;
					break;
				}
			}
			if (flag)
			{
				ans++;
			}
		}	
		cout << "Case #" << y+1 << ": " << ans << "\n";
	}
	
	
}