#include<iostream>
#include<cstring>

using namespace std;

int i,j,k,l,banyak,kasus,total,temp;
int akhir[50];
char s[50];

int main()
{
	scanf("%d",&kasus);
	for (l=1;l<=kasus;l++)
	{
		total = 0;
		scanf("%d\n",&banyak);
		for (i=1;i<=banyak;i++)
		{
			gets(s);
			akhir[i] = 0;
			for (j=banyak-1;j>-1;j--)
			{
				if (s[j] > 48)
				{
					akhir[i] = j+1;
					break;
				}
			}
		}

		//for (i=1;i<=banyak;i++) printf("%d\n",akhir[i]);

		for (i=1;i<banyak;i++)
		{
			j = i;
			while (akhir[j] > i) j++;
			for (k=j;k>i;k--)
			{
				total++;
				temp = akhir[k];
				akhir[k] = akhir[k-1];
				akhir[k-1] = temp;
			}
		}
		printf("Case #%d: %d\n",l,total);
	}
	return 0;
}