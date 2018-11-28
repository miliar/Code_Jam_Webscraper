#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

char peta[50];
int isi[11][11],kasus,baris,kolom,D;

bool brute(int ukur,int baris,int kolom)
{
	int totalx = 0;
	int totaly = 0;
	
	if (ukur % 2)
	{
		int y = baris + (ukur-1) / 2;
		int x = kolom + (ukur-1) / 2;

		for (int i=baris;i<baris+ukur;i++)
		{
			if (i==baris || i==baris+ukur-1)
			{
				for (int j=kolom+1;j<kolom+ukur-1;j++)
				{
					totaly += isi[i][j]*(i-y);
					totalx += isi[i][j]*(j-x);
				}
			}
			else
			{
				for (int j=kolom;j<kolom+ukur;j++)
				{
					totaly += isi[i][j]*(i-y);
					totalx += isi[i][j]*(j-x);
				}
			}
		}
		
		if ((totaly != 0)||(totalx != 0)) return false;
		return true;
	}
	else
	{
		int y = baris + (ukur-1) / 2;
		int x = kolom + (ukur-1) / 2;

		for (int i=baris;i<baris+ukur;i++)
		{
			if (i==baris || i==baris+ukur-1)
			{
				for (int j=kolom+1;j<kolom+ukur-1;j++)
				{
					totaly += isi[i][j]*(2*(i-y)-1);
					totalx += isi[i][j]*(2*(j-x)-1);
				}
			}
			else
			{
				for (int j=kolom;j<kolom+ukur;j++)
				{
					totaly += isi[i][j]*(2*(i-y)-1);
					totalx += isi[i][j]*(2*(j-x)-1);
				}
			}
		}
		
		//printf("%d %d\n",totalx,totaly);
		if ((totaly != 0)||(totalx != 0)) return false;
		return true;
	}
}

int main()
{
	scanf("%d",&kasus);
	for (int l=1;l<=kasus;l++)
	{
		scanf("%d %d %d",&baris,&kolom,&D);
		for (int i=0;i<baris;i++)
		{
			scanf("%s",peta);
			for (int j=0;j<kolom;j++) isi[i][j] = peta[j]-48;
		}

		int jawab = -1;
		for (int i=3;i <= min(baris,kolom);i++)
		{
			for (int j=0;j<=baris-i;j++)
			{
				for (int k=0;k<=kolom-i;k++)
				{
					if (brute(i,j,k))
					{
						jawab = i;
						break;
					}
				}
				if (jawab == i) break;
			}
		}
		
		printf("Case #%d: ",l);
		if (jawab == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n",jawab);
	}
	return 0;
}
