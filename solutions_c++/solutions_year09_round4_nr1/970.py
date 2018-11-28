#include <stdio.h>
#include <string.h>
char str[40][41];
void swap(char *s1, char *s2)
{
	char temp[41];
	strcpy(temp, s1);
	strcpy(s1, s2);
	strcpy(s2, temp);
}
int n;
int main()
{
	int cases;
	scanf("%d", &cases);
	for (int c = 1; c <= cases; c++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%s", str[i]);
		int count = 0;
		for (int i = 0; i < n; i++)
		{
			bool right = true;
			for (int j = i + 1; j < n; j++)
				if (str[i][j] == '1') right = false;
			if (!right) {
				int p;
				bool check;
				for (p = i + 1; p < n; p++)
				{
					check = true;
					for (int j = i + 1; j < n; j++)
					       if (str[p][j] == '1') check = false;
					if (check) break;	
				}
				count += p - i;
				for (; p > i; p--)
					swap(str[p], str[p - 1]);
			}
		}
		printf("Case #%d: %d\n", c, count);
	}
	return 0;
}


