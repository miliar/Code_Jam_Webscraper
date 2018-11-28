#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int kasus,jawab,temu[1000001],total;
long long banyak;
bool prima[1000001];

int search(int mau,long long x)
{
	int kiri = 0,kanan = total;
	while (kanan-kiri > 1)
	{
		int tengah = (kanan+kiri) / 2;
		long long coba = 1;
		bool bisa = true;
		
		for (int i=1;i<=mau;i++)
		{
			if (coba > banyak / (long long)temu[tengah])
			{
				bisa = false;
				break;
			}
			coba *= (long long)temu[tengah];
		}
		
		if (!bisa) kanan = tengah;
		else kiri = tengah;
	}
	return kiri;
}

int main()
{
	temu[0] = 1;
	for (int i=2;i<=1000000;i++)
	{
		if (prima[i]) continue;
		total++;
		temu[total] = i;
		for (int j=i;j<=1000000/i;j++) prima[i*j] = true;
	}
	total++;
	temu[total] = 1000001;

	scanf("%d",&kasus);
	for (int l=1;l<=kasus;l++)
	{
		scanf("%I64d",&banyak);
		if (banyak == 1)
		{
			printf("Case #%d: %d\n",l,0);
			continue;
		}
		
		jawab = 0;
		for (int j=2;j<=40;j++)
		{
			int batas = search(j,banyak);
			//printf("%d : %d\n",j,batas);
			if (!batas) break;
			jawab += batas;
		}
		
		printf("Case #%d: %d\n",l,jawab+1);
	}
	return 0;
}
