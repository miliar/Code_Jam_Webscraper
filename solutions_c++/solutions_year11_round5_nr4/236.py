#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

unsigned long long pangkat[65],total;
char kata[65];
int kasus,temu,letak[65],panjang;

bool find(unsigned long long x)
{
	unsigned long long kiri = 0;
	unsigned long long kanan = 1LL<<30;
	bool temu = false;
	
	while ((kiri <= kanan)&&(!temu))
	{
		unsigned long long tengah = (kiri+kanan) / 2LL;
		if (tengah*tengah == x) temu = true;
		else if (tengah*tengah < x) kiri = tengah+1;
		else kanan = tengah-1;
	}
	return temu;
}

int main()
{
	pangkat[0] = 1;
	for (int i=1;i<60;i++) pangkat[i] = pangkat[i-1]*2LL;
	
	scanf("%d",&kasus);
	for (int l=1;l<=kasus;l++)
	{
		scanf("%s",kata);
		total = 0; temu = 0;
		panjang = strlen(kata);
		for (int i=0;i<panjang;i++)
		{
			if (kata[i] == '?')
			{
				letak[temu] = panjang-i-1;
				temu++;
			}
			else if (kata[i] == '1') total += pangkat[panjang-i-1];
		}
		
		for (int i=0;i<(1<<temu);i++)
		{
			unsigned long long sem = total;
			for (int j=0;j<temu;j++) if (i & (1<<j)) sem += pangkat[letak[j]];

			if (find(sem))
			{
				for (int j=0;j<temu;j++)
				{
					if (i & (1<<j)) kata[panjang-letak[j]-1] = '1';
					else kata[panjang-letak[j]-1] = '0';
				}
				printf("Case #%d: %s\n",l,kata);
				break;
			}
		}
	}
	return 0;
}
