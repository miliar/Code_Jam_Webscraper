#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#define MAXN 2000007
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(a,b,c) for(int a=b;a<=(c);a++)
#define FORD(a,b,c) for (int a=b;a>=(c);a--)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();i++)

using namespace std;

typedef long long LL;  

int cykl[MAXN],bylo[MAXN];
int t,a,b;
LL result;

int obroc(int v, int p)
{
	int cyfra = v/p;
	v %= p;
	v *= 10;
	v += cyfra;
	return v;
}

int main()
{
	FOR(i,1,9) cykl[i] = -1;
	int potega = 10;
	while (potega < MAXN)
	{
		FOR(i,potega,min(2000000,potega*10-1))
		{
			int liczba = obroc(i,potega);
			while (liczba < potega || liczba > min(2000000,potega*10-1)) liczba = obroc(liczba,potega);
			if (i == liczba) cykl[i] = -1;
				else cykl[i] = liczba;
		}
		potega *= 10;
	}
	//printf("%d %d %d\n",cykl[10],cykl[100]);
	scanf("%d",&t);
	FOR(j,1,t)
	{
		result = 0LL;
		scanf("%d%d",&a,&b);
		FOR(i,a,b)
		{
			//printf("robimy %d\n",i);
			if (bylo[i] != j && cykl[i] != -1)
			{
				bylo[i] = j;
				int ilosc = 1;
				int liczba = cykl[i];
				while (liczba != i) 
				{
					bylo[liczba] = j;
					if (liczba >= a && liczba <= b) ++ilosc;
					liczba = cykl[liczba];
				}
				//printf("znaleziono %d obrotow\n",ilosc);
				result += LL(ilosc)*LL(ilosc-1);
			}
		}
		result >>= 1;
		printf("Case #%d: %lld\n",j,result);
	}
	return 0;
}
