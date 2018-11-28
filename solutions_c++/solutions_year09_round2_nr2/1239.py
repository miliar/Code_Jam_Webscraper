#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
char num[22];
char s[22];
char t[22];
int main()
{
	int tcase;
	freopen("B-large.in", "r", stdin);
	freopen("blout.txt", "w", stdout);
	scanf("%d", &tcase);
	int n;
	for(int i = 1; i <= tcase; i++)
	{
		scanf("%s", num);
		printf("Case #%d: ", i);
		int len = strlen(num);

		strcpy(t, num);
		if(next_permutation(num, num+len))printf("%s\n", num);
		else
		{
			sort(t, t+len);
			int i = 0;
			while(i < len && t[i] == '0') i++;
			int j = i;
			printf("%c0", t[j]);			
			 for(int i = 0; i < len; i++)
			 {
					if(j == i) continue;
			 	printf("%c", t[i]);
			}
			printf("\n");
		}
		
	}
	return 0;
}
