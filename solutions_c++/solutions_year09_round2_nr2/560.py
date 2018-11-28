#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

char c[25];

int cnt[10];
int cnt2[10];

int main()
{
	freopen("C:\\b2.txt", "r" ,stdin);
	freopen("C:\\b2out.txt", "w" ,stdout);

	int te;
	scanf("%d", &te);
	for (int i = 1; i <= te; i++)
	{
		printf("Case #%d: ", i);

		memset(cnt, 0, sizeof(cnt));
		memset(cnt2, 0, sizeof(cnt2));
		scanf("%s", c);
		int j = 0;
		while (c[j] != '\0')
		{
			cnt[c[j]-'0']++;
			//cnt2[c[j]-'0']++;
			j++;
		}

		int k = j-1;
		int prev=0;
		int dig;
		do
		{
			dig = c[k] - '0';
			cnt2[dig]++;
			if (dig >= prev)
			{
				k--;
				prev = dig;
			}
		}
		while (dig >= prev && k >= 0);

		if (k == -1)
		{
			//+0
			cnt[0]++;
			dig = 1;
			while (cnt[dig] == 0) dig++;
			printf("%d", dig);
			cnt[dig]--;
			for (int q = 0; q < 10; q++)
			{
				for (int w = 0; w < cnt[q]; w++)
				{
					printf("%d", q);
				}
			}

		}
		else
		{
			for (int q = 0; q < k; q++)
			{
				printf("%c", c[q]);
			}
			dig++;
			while (cnt2[dig] == 0) dig++;
			printf("%d", dig);
			cnt2[dig]--;
			for (int q = 0; q < 10; q++)
			{
				for (int w = 0; w < cnt2[q]; w++)
				{
					printf("%d", q);
				}
			}
		}

		printf("\n");

		
	}

}