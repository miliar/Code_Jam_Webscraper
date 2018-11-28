#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>

#define VI vector <int>
#define VVI vector < vector<int> >
#define VS vector <string>
#define rep(i,n) for(int i=0;i<(n);++i)
#define repab(i,a,b) for(int i=(a);i<=(b);++i)
#define PB push_back
#define SORT(v) sort(v.begin(), v.end())

using namespace std;

int m, v, sr, li;
int bramka[15000]; // 1->AND, 0->OR
int change[15000];
int wart[15000];

int policz(int w, int val)
{
	int best = 100000000;
	int tmp,tmp2;
	if (wart[w]==val) return 0;
	if (w>sr) return 100000000;
	if (bramka[w]==1)
	{
		if (wart[2*w]==1)
		{
			if (wart[2*w+1]==1)
			{
				best = policz(2*w,0);
				tmp = policz(2*w+1,0);
				if (tmp<best) best=tmp;
				return best;
			}
			else
			{
				if (change[w]) return 1;
				return policz(2*w+1,1);
			}
		}
		else
		{
			if (wart[2*w+1]==1)
			{
				if (change[w]) return 1;
				return policz(2*w,1);
			}
			else
			{
				tmp = policz(2*w,1);
				tmp2 = policz(2*w+1,1);
				if (best > tmp+tmp2) best = tmp+tmp2;
				if (change[w])
				{
					if (tmp2<tmp) tmp=tmp2;
					tmp++;
					if (best>tmp) best=tmp;
				}
				return best;
			}
		}
	}
	else
	{
		if (wart[2*w]==1)
		{
			if (wart[2*w+1]==1)
			{
				tmp = policz(2*w,0);
				tmp2 = policz(2*w+1,0);
				if (best > tmp+tmp2) best = tmp+tmp2;
				if (change[w])
				{
					if (tmp2<tmp) tmp=tmp2;
					tmp++;
					if (best>tmp) best=tmp;
				}
				return best;
			}
			else
			{
				if (change[w]) return 1;
				return policz(2*w,0);
			}
		}
		else
		{
			if (wart[2*w+1]==1)
			{
				if (change[w]) return 1;
				return policz(2*w+1,0);
			}
			else
			{
				tmp = policz(2*w+1,1);
				tmp2 = policz(2*w,1);
				if (tmp2<tmp) tmp=tmp2;
				return tmp;
			}
		}
	}
}

void licz(void)
{
	int q1,q2;
	scanf("%d%d",&m, &v);
	sr = (m-1)/2;
	li = (m+1)/2;
	repab(i,1,m)
	{
		if (i<=sr)
		{
			scanf("%d%d",&q1,&q2);
			bramka[i]=q1;
			change[i]=q2;
		}
		else
		{
			scanf("%d",&q1);
			wart[i]=q1;
		}
	}
	for(int i=sr; i>=1; i--)
	{
		if (bramka[i])
		{
			if (wart[2*i] + wart[2*i+1] == 2) wart[i]=1;
			else wart[i]=0;
		}
		else
		{
			if (wart[2*i] + wart[2*i+1] >= 1) wart[i]=1;
			else wart[i]=0;
		}
	}
	int ret=policz(1,v);
	if (ret>=10000000) printf("IMPOSSIBLE\n");
	else printf("%d\n",ret);
}

int main(void)
{
	int dd;
	scanf("%d",&dd);
	for(int yy=0;yy<dd;yy++)
	{
		printf("Case #%d: ", yy+1);
		licz();
	}
	return 0;
}
