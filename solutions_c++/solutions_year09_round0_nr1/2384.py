#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

char db[5000][15];

bool td[500][15][26];

bool cmp(int word, int tmp, int l)
{
	for (int i=0; i<l; i++)
	{
		if (!td[tmp][i][db[word][i] - 'a'])
		{
			return 0;
		}
	}
	
	return 1;
}

int main ()
{
    ifstream cin("input.txt");
	ofstream cout("output.txt");
	
	int l, d, n;
	
	cin >> l >> d >> n;
	
	for (int i=0; i<d; ++i)
	{
		for (int j=0; j<l; ++j)
		{
			cin >> db[i][j];
		}
	}
		
	for (int i=0; i<n; i++)
	{
		int pos = 0;
		char c;
		for (int j=0; j<l; j++)
		{
			cin >> c;
			
			if (c != '(')
			{
				td[i][pos][c - 'a'] = 1;
			}else
			{
				while (1)
				{
					cin >> c;
				
					if (c == ')')
					{
						break;
					}
					
					td[i][pos][c - 'a'] = 1;
				}
			}
		
			pos++;
			
		}
	}
	
	for (int i=0; i<n; i++)
	{
		int count = 0;
		for (int j=0; j<d; j++)
		{
			if (cmp(j, i, l))
			{
				count++;
			}
		}
		
		cout << "Case #" << i+1 << ": " << count << endl; 
		
	}
	
}
