#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

int l , d , n;

vector<string> dic;

string palavra , exp;

int main (void)
{

	int teste = 1;

	scanf("%d %d %d", &l , &d , &n);
	
	while(getchar() != '\n') ;
	
	for (int i = 0; i < d; ++i)
	{
		cin >> palavra;
		dic.push_back(palavra);
	}

	while (n > 0)
	{
		
		cin >> exp;
	
		int cont = 0;
		
		for (int j = 0; j < dic.size();++j)
		{
			int pos = 0;
			int num = 0;
		
			for (int k = 0; k < dic[j].size(); ++k)
			{
				if (exp[pos] == '(')
				{
					pos++;
					while(exp[pos] != ')')
					{
						if (dic[j][k] == exp[pos])
						{
							num++;
						}
						pos++;
					}
					pos++;
				}
				else if (dic[j][k] == exp[pos])
				{
					num++;
					pos++;
				}
			}
			
			if (num == l)
			{
				cont++;
			}
		}
	
		printf("Case #%d: %d\n", teste++, cont);
	
		n--;
	}
	
	return 0;
}
