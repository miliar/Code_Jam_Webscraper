#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<ctype.h>
using namespace std;
#define MAXN 102
struct
{
	char tg;	//'O' 'B'
	int btn;	//button
}a[MAXN];
int o[MAXN], b[MAXN];
int t;	//case
int n;	//
int numo, numb;	//
inline int Rint()	{int x; scanf("%d", &x); return x;}
int solve()
{
	int poso=1, posb=1;
	int ans=0;
	int io=0, ib=0;
	for(int i=0; i<n; i++)
	{
		if(a[i].tg == 'O')
		{
			int t = abs(a[i].btn - poso);		//当前移动要用的时间
			t+=1;	//push用的时间
			poso = a[i].btn;
			io+=1;
			int t2 = abs(b[ib] - posb);
			if(t2>t)
			{
				if(posb>b[ib]) posb-=t;
				else posb+=t;
			}
			else posb=b[ib];
			ans+=t;
		}
		else 
		{
			int t = abs(a[i].btn - posb);		//当前移动要用的时间
			t+=1;
			posb = a[i].btn;
			ib+=1;
			int t2 = abs(o[io] - poso);
			if(t2>t)
			{
				if(poso>o[io]) poso-=t;
				else poso+=t;
			}
			else poso=o[io];
			ans+=t;
		}
	}
	return ans;
}

int main()
{
	t = Rint();
	for(int i=1; i<=t; i++)
	{
		n = Rint();
		numo = numb = 0;
		for(int j=0; j<n; j++)
		{
			char t[2];
			scanf("%s%d", t, &a[j].btn);
			a[j].tg = t[0];
			if(a[j].tg == 'O') o[numo++] = a[j].btn;
			else b[numb++] = a[j].btn;
		}
		printf("Case #%d: %d\n", i, solve());
	}
}