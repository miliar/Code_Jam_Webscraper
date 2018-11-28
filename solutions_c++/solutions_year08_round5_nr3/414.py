#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(a,n) for(a=0;a<n;a++)
#define memset0(v) memset(v,0,sizeof(v))
typedef vector<string> vs;
typedef vector<int> vi;

int best[11][1024];

int bits[1024];

int W,H;

char crow1[11];
char crow2[11];
char tab[11][11];

int isgood(int conf1, int conf2, int row)
{
	memset0(crow1);
	memset0(crow2);
	int a;
	fo(a,W)
	{
		if((conf1 & (1<<a))!=0) crow1[a]=1;
		if((conf2 & (1<<a))!=0) crow2[a]=1;
	}

	fo(a,W)
	if(crow2[a]==1 && tab[row][a]==1) return 0;

	fo(a,W)
	{
		if(crow1[a]==1 && a>0 && crow1[a-1]==1) return 0;
		if(crow1[a]==1 && a+1<W && crow1[a+1]==1) return 0;
		if(crow2[a]==1 && a>0 && crow2[a-1]==1) return 0;
		if(crow2[a]==1 && a+1<W && crow2[a+1]==1) return 0;

		if(crow1[a]==1 && a>0 && crow2[a-1]==1) return 0;
		if(crow1[a]==1 && a+1<W && crow2[a+1]==1) return 0;
	}

	return 1;
}

inline int countbits(int num)
{
	int res=0;
	while(num>0)
	{
		if(num%2==1) res++;
		num/=2;
	}
	return res;
}

int main()
{
	int a,b,c,d,tests;

	const string strFile = "c-small";
	string fin = strFile+".in";
	string fout = strFile+".out";

	freopen(fin.c_str(), "rt", stdin);
	freopen(fout.c_str(), "wt", stdout);

	scanf("%d\n", &tests);
	char buf[100];
	int x,y;

	int MAXC;

	fo(a,1024) bits[a]=countbits(a);

for(int test=1;test<=tests;test++)
{

	scanf("%d%d\n",&H,&W);
	fo(y,H)
	{
		gets(buf);
		fo(x,W)
			if(buf[x]=='.') tab[y][x]=0; else tab[y][x]=1;
	}

	memset0(best);
	MAXC=1;
	fo(a,W) MAXC*=2;

	fo(a,MAXC)
		if(isgood(0,a,0)) 
			best[0][a]=bits[a];

	for(y=1;y<H;y++)
	{
		fo(a,MAXC)
		fo(b,MAXC)
		if(isgood(a,b,y))
			best[y][b]=max(best[y][b], best[y-1][a]+bits[b]);
	}

	int res=0;
	fo(a,MAXC)
		res=max(res,best[H-1][a]);

	printf("Case #%d: %d\n", test, res);

}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
