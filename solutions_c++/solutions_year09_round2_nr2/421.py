#include<iostream>
using namespace std;

char str[30];
int T;
int d[30];
int main()
{
	scanf("%d\n",&T);
	for (int t = 0; t < T; t++)
	{
		scanf("%s\n",str);
		int len = strlen(str);
		for (int i = 0; i < len; i++)
			d[i] = str[i] - 48;
		printf("Case #%d: ",t + 1);
		if (next_permutation(d,d + len))
		{	
			for (int i = 0; i < len; i++)
				printf("%d",d[i]);
			printf("\n");
		}
		else 
		{
			int now = 0;
			while(d[now] == 0) now++;
			printf("%d",d[now]);
			for (int i = 0; i <= now; i++) printf("0");
			for (int i = now + 1; i <= len - 1; i++) printf("%d",d[i]);
			printf("\n");
		}
	}
	return 0;
}
