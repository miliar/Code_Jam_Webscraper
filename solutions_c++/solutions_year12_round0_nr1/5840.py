#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>

using namespace std;

int main()
{
	int T, len;
	int A[] = {0, 25, 8, 5, 19, 15, 3, 22, 24, 4, 21, 9, 7, 12, 2, 11, 18, 26, 20, 14, 23, 10, 16, 6, 13, 1, 17};
	scanf("%d", &T);
	cin.ignore();	
	for(int i = 1; i <=T; i++)
	{
		string s;
		getline(cin, s);
		printf("Case #%d: ", i);
		for(int i = 0; s[i] != '\0'; i++)
		{
			if(s[i] != 32)
			{
				printf("%c", (A[s[i]-96] + 96));
			}
			else
				printf("%c", s[i]);
		}
		printf("\n");
	}
	return 0;
}
