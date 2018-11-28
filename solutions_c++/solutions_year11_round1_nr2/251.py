#include<iostream>
#include<cstring>
#include<string>

using namespace std;

char kata[105][15],urut[30];
bool buang[105];
int panjang[105];
int kasus,kamus,tebak;

int main()
{
	scanf("%d",&kasus);
	for (int l=1;l<=kasus;l++)
	{
		scanf("%d %d",&kamus,&tebak);
		for (int i=0;i<kamus;i++)
		{
			scanf("%s",kata[i]);
			panjang[i] = strlen(kata[i]);
		}

		printf("Case #%d:",l);
		for (int i=1;i<=tebak;i++)
		{
			scanf("%s",urut);
			int ambil = 0;
			int best = -1;
			
			for (int j=0;j<kamus;j++)
			{
				memset(buang,0,sizeof(buang));
				for (int k=0;k<kamus;k++) if (panjang[j] != panjang[k]) buang[k] = true;
				int total = 0;
				
				for (int k=0;k<26;k++)
				{
					bool temu = false;
					for (int m=0;m<panjang[j];m++) if (kata[j][m] == urut[k])
					{
						temu = true;
						break;
					}
					
					if (!temu)
					{
						for (int m=0;m<kamus;m++)
						{
							if (buang[m]) continue;
							for (int n=0;n<panjang[m];n++)
							{
								if (kata[m][n] == urut[k])
								{
									temu = true;
									buang[m] = true;
								}
							}
						}
						if (temu) total++;
					}
					else
					{
						for (int m=0;m<kamus;m++)
						{
							if (buang[m]) continue;
							for (int n=0;n<panjang[m];n++)
							{
								if ((kata[m][n] == urut[k]) || (kata[j][n] == urut[k]))
									if (kata[m][n] != kata[j][n])
									{
										buang[m] = true;
										break;
									}
							}
						}
					}
				}
				
				if (total > best)
				{
					best = total;
					ambil = j;
				}
			}
			printf(" %s",kata[ambil]);
		}
		printf("\n");
	}
	return 0;
}
