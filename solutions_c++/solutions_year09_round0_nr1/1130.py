#include <iostream>
using namespace std;

char dict[7550][20];
char pat[700];
bool mat[20][26];
int l, d, n;

int main()
{
	cin >> l >> d >> n;
	for(int i=0; i<d; i++)
	{
		//string t;
		cin >> dict[i];
	}
	for(int i=1; i<=n; i++)
	{
		cin >> pat;
		{
			int k = 0;
			for(int j=0; j<l; j++)
			{
				for(int r = 0; r < 26; r++) mat[j][r] = false;
				if(pat[k] == '(')
				{
					for(k++;pat[k]!=')';k++) mat[j][pat[k]-'a'] = true;
				}
				else
				{
					mat[j][pat[k]-'a'] = true;
				}
				k++;
			}
		}
		//for(int j=0; j<l; j++, cout << endl) for(int k=0; k<5; k++) cout << (mat[j][k]?'x':'.');
		{
			int y=0;
			for(int j=0; j<d; j++)
			{
				int k;
				for(k=0; k<l; k++) if(!mat[k][dict[j][k]-'a']) break;
				if(k == l) y++;
			}
			cout << "Case #" << i << ": " << y << endl;
		}
	}
	return 0;
}
