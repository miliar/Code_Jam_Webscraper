#include "iostream"
#include "string.h"


int main()
{
	int n;
	scanf("%d\n",&n);
	char search[100*100];
	int query[1000];
	char tmp[100];
	bool w[100];
	for (int c = 0; c < n; c++)
	{
		int s;
		scanf("%d\n",&s);
	//	printf("s=%d\n",s);
		for (int i = 0; i < s; i++)
		{
			gets(search+i*100);
			//printf("%s\n",search+i*100);
		}
		int q;
		scanf("%d\n",&q);
		for (int i = 0; i < q; i++)
		{
			gets(tmp);
			int j;
			for (j = 0; j < s; j++)
				if (strcmp(tmp,search+j*100) == 0)
					break;
			query[i] = j;
			//printf("%d\n",j);
		}
		int r = 0;
		int bad = -1;
		for (int t = 0; t < s; t++)
			w[t] = false;
		int a = 0;
		for (int i = q-1; i>=0; i--)
		{
			if (w[query[i]] == false)
			{
				a++;
				w[query[i]] = true;
				if (a == s)
				{
					r++;
					for (int t = 0; t < s; t++)
						w[t] = false;
					a=0;
					i++;
				}
			}
		}
		printf("Case #%d: %d\n",c+1,r);
	}
	return 0;
}
