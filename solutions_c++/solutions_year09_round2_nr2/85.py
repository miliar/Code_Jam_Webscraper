#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	string s;
	int n, t, ile[10];
	
	scanf("%d", &t);
	
	for (int tc = 1; tc <= t; tc++)
	{
		printf("Case #%d: ", tc);
		
		cin >> s;
		n = (int)s.size();
		memset(ile, 0, sizeof(ile));
		
		bool found = false;
		for (int i = n - 1; i >= 0; i--)
		{
			ile[s[i] - '0']++;
			if (i <= n - 2 && s[i] < s[i + 1])
			{
				found = true;
				for (int j = 0; j < i; j++)
					printf("%c", s[j]);
				
				int mi = s[i] - '0' + 1;
				while (ile[mi] == 0)
					mi++;
				
				printf("%c", mi + '0');
				ile[mi]--;
				
				for (int j = 0; j < 10; j++)
					while (ile[j] != 0)
					{
						printf("%c", j + '0');
						ile[j]--;
					}
				break;
			}
		}
		
		if (!found)
		{
			ile[0]++;
			
			int mi = 1;
			while (ile[mi] == 0)
				mi++;
			
			printf("%c", mi + '0');
			ile[mi]--;
			for (int j = 0; j < 10; j++)
				while (ile[j] != 0)
				{
					printf("%c", j + '0');
					ile[j]--;
				}
		}
		
		printf("\n");
	}
	
	return 0;
}