#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

typedef struct
{
	int jauh,cepat;
} data;

int kasus,panjang,jalan,lari,banyak,j,k;
double total,hitung,waktu;
data rel[10001];

bool cf(const data &a,const data &b)
{
	if (a.cepat != b.cepat) return a.cepat < b.cepat;
	return a.jauh < b.jauh;
}

int main()
{
	scanf("%d",&kasus);
	for (int l=1;l<=kasus;l++)
	{
		scanf("%d %d %d %lf %d",&panjang,&jalan,&lari,&waktu,&banyak);
		rel[0].jauh = panjang;
		rel[0].cepat = 0;
		for (int i=1;i<=banyak;i++)
		{
			scanf("%d %d %d",&j,&k,&rel[i].cepat);
			rel[i].jauh = k-j;
			rel[0].jauh -= rel[i].jauh;
		}
		sort(rel,rel+banyak+1,cf);
		
		double total = 0;
		int indeks = 0;
		while ((waktu > 0) && (indeks <= banyak))
		{
			hitung = (double)rel[indeks].jauh / (double)(rel[indeks].cepat + lari);
			if (waktu-hitung >= 0)
			{
				waktu -= hitung;
				total += hitung;
			}
			else
			{
				total += waktu;
				hitung = (rel[indeks].jauh-waktu*(double)(rel[indeks].cepat + lari)) / (double)(rel[indeks].cepat+jalan);
				total += hitung;
				waktu = 0;
			}
			indeks++;
		}
		
		while (indeks <= banyak)
		{
			total += (double)(rel[indeks].jauh)/(double)(rel[indeks].cepat+jalan);
			indeks++;
		}
		
		printf("Case #%d: %.6lf\n",l,total);
	}
	return 0;
}
