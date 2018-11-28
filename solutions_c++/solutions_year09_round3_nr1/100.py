#include<iostream>
#include<cstring>

using namespace std;

char kode[61];
int temu[256];
long long isi[61],dasar,jawab,total;
int i,l,banyak,panjang;

int main()
{
	scanf("%d",&banyak);
	for (l=1;l<=banyak;l++)
	{
		jawab = 0;
		scanf("%s",&kode);
		panjang = strlen(kode);
		memset(temu,255,sizeof(temu));

		temu[kode[0]] = 1;
		total = 0;
		for (i=0;i<panjang;i++)
		{
			if (temu[kode[i]] == -1)
			{
				total++;
				if (total == 1) temu[kode[i]] = 0;
				else temu[kode[i]] = total;
			}
			isi[i] = temu[kode[i]];
		}

		total++;
		if (total == 1) total = 2;
		dasar = 1;

		for (i=panjang-1;i>-1;i--)
		{
			jawab += (dasar * isi[i]);
			dasar *= total;
		}

		printf("Case #%d: %lld\n",l,jawab);
	}
	return 0;
}