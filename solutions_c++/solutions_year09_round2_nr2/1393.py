#include <iostream>
#include <algorithm>
using namespace std;

char key[30];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B1.txt","w",stdout);
	int T;
	scanf("%d",&T);

	gets(key);

	int b=1;

	while (T--)
	{
		gets(key+1);

		printf("Case #%d: ",b++);

		int i;
		for(i=1;key[i]!='\0';++i);

		key[0]='0';

		int now=atoi(key);
		int mm=INT_MAX;
		int ag=INT_MAX;
		sort(key,key+i);
		while (next_permutation(key,key+i))
		{
			int x=atoi(key);

			if (x>now)
			{
				if (x<mm)
				{
					mm=x;
				}
			}

			if (x<ag)
			{
				ag=x;
			}
		}

		printf("%d\n",mm);

	}
	return 0;
}