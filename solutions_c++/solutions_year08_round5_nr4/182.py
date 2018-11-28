#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>
#define MOD 10007
#define LLD long long int

using namespace std;

int main()
{
	int lw;
	scanf("%d",&lw);

	for (int L=1;L<=lw;L++)
	{
		LLD Num[101][101];
		int Zle[101][101];
		int h,w,r;
		scanf("%d%d%d",&h,&w,&r);
		for (int i=1;i<=h;i++)
			for (int j=1;j<=w;j++)
				Num[i][j] = Zle[i][j] = 0;
		Num[1][1] = 1;
		while (r--)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			Zle[x][y] = 1;
		}
		for (int i=1;i<=h;i++)
			for (int j=1;j<=w;j++)
			{
				if (i==1 && j==1) continue;
				if (Zle[i][j]) continue;
				int x,y;
				x = i-1;
				y = j-2;
				if (x >= 1 && y >= 1)
					Num[i][j] += Num[x][y];
				x = i-2;
				y = j-1;
				if (x >= 1 && y >= 1)
					Num[i][j] += Num[x][y];
				Num[i][j]%=MOD;
			}
			printf("Case #%d: %d\n",L,Num[h][w]);
	}

	return 0;
}
