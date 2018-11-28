#include<stdio.h>
#include<algorithm>
using namespace std;

const int maxn = 27;
const int maxst = (1 << 16);

int MAT[maxn][maxn];
short VER[maxn][maxn],DIN[maxst];
int N,K;
short VER1[maxst];

int check1(int i,int j)
{
//	return 1;
	if (VER[i][j]) return (VER[i][j] > 0);	
	for(int k = 1;k <= K; ++k)
	{
		if (MAT[i][k] == MAT[j][k]) {VER[i][j] = 1;return 1;}
		if (MAT[i][k] > MAT[j][k] && MAT[i][k - 1] < MAT[j][k - 1]) {VER[i][j] = 1;return 1;}
		if (MAT[i][k] < MAT[j][k] && MAT[i][k - 1] > MAT[j][k - 1]) {VER[i][j] = 1;return 1;}
	}
	VER[i][j] = -1;
	return 0;
}

bool check(int stare)
{
//	return 1;
	if (VER1[stare]) return VER1[stare] > 0;
	for(int p = 0;p < N; ++p)
		for(int p1 = p + 1;p1 < N; ++p1)
			if  (check1(p + 1,p1 + 1) && (stare & (1 << p)) && (stare & (1 << p1))) {VER1[stare] = -1;
					return false;}
//	printf("%d\n",stare);
	VER1[stare] = 1;
	return true;
}


short solve(int stare)
{
//	printf("-> %d\n",stare);
	if (stare == 0) return 0;
	if (check(stare)) return 1;
	if (DIN[stare]) return DIN[stare];
	int cur = 10000;
	for(int j = 1;j < stare; ++j)
	{
		if ((j & stare) != j) continue;
		if (VER1[j] > 0)
		{
			cur = min(cur,1 + solve(stare ^ j));  		
			
		}
	}
	DIN[stare] = cur;
	return DIN[stare];
}

int main()
{
	freopen("stock.in","r",stdin);
	freopen("stock.out","w",stdout);
	int nrt = 0;
	scanf("%d\n",&nrt);
//	nrt = 2;
//	check(2);
	for(int nr = 1;nrt;++nr,--nrt)
	{
		scanf("%d %d\n",&N,&K);
		memset(MAT,0,sizeof(MAT));
		for(int i = 1;i <= N; ++i)
			for(int j = 1;j <= K; ++j)
				scanf("%d ",&MAT[i][j]);
		memset(VER1,0,sizeof(VER1));
		for(int i = 1;i < (1 << N); ++i) check(i);
//		for(int i = 1;i <= N; ++i)
//			for(int j = 1;j <= N; ++j) VER[i][j] = VER[j][i] = check1(i,j);	
//		check(2);
//		for(int i = 0;i <= (1 << N); ++i) DIN[i] = VER1[i] = 0;
//		memset(VER1,0,sizeof(VER1));
		memset(DIN,0,sizeof(DIN));
		memset(VER,0,sizeof(VER));
		printf("Case #%d: %d\n",nr,solve((1 << N) - 1));
	}
	return 0;
}

