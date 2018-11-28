#include "iostream"
#include "string.h"


int main()
{
	int n;
	scanf("%d\n",&n);
	int atob1[100];
	int atob2[100];
	int btoa1[100];
	int btoa2[100];
	for (int c = 0; c < n; c++)
	{
		int T;
		scanf("%d\n",&T);
		int NA, NB;
		scanf("%d %d\n",&NA,&NB);
		for (int i =0; i < NA; i++)
		{
			int a,b,c,d;
			scanf("%d:%d %d:%d\n",&a,&b,&c,&d);
			atob1[i] = a*60+b;
			atob2[i] = c*60+d+T;
		}
		for (int i =0; i < NB; i++)
		{
			int a,b,c,d;
			scanf("%d:%d %d:%d\n",&a,&b,&c,&d);
			btoa1[i] = a*60+b;
			btoa2[i] = c*60+d+T;
		}
		int needa = 0;
		int needb = 0;
		int A = 0;
		int B = 0;
		for (int i = 0; i < 60*24+60; i++)
		{
//			printf("%d:%d %d %d %d %d\n",i/60,i-(i/60)*60,A,B,needa,needb);
			for (int j = 0; j < NA; j++)
				if (atob2[j] == i)
				{
					B++;
				}
			for (int j = 0; j < NB; j++)
				if (btoa2[j] == i)
				{
					A++;
				}
			for (int j = 0; j < NA; j++)
				if (atob1[j] == i)
				{
					if (A == 0)
						needa++;
					else
						A--;
				}
			for (int j = 0; j < NB; j++)
				if (btoa1[j] == i)
				{
					if (B == 0)
						needb++;
					else
						B--;
				}
		}
		printf("Case #%d: %d %d\n",c+1,needa, needb);
	}
	return 0;
}
