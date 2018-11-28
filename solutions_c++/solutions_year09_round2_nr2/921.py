#include <iostream>
#include <algorithm>

using namespace std;

int T;
char str[30];
int a[30];
int num;
int tmp[30];
int main()
{
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	int i, j, t;
	scanf("%d", &T);
	getchar();
	for(i=1; i<=T; i++)
	{
		num = 0;
		gets(str);
		for(j=0; str[j]; j++)
		{
			a[j] = str[j]-'0';
			num++;
		}	
		printf("Case #%d: ", i);
		if(next_permutation(a,a+num))
		{
			for(j=0; j<num; j++)
		    	printf("%d", a[j]);
			printf("\n");
		}
		else
		{
			t = 0;
			for(j=0; j<num; j++)
			{
				if(a[j])
				{
					tmp[t++] = a[j];
				}
			}
			sort(tmp, tmp+t);
			printf("%d", tmp[0]);
			for(j=1; j<=num+1-t; j++)
				printf("0");
			for(j=1; j<t; j++)
				printf("%d", tmp[j]);
			printf("\n");
		}
	}

	system("pause");
	return 0;
}
