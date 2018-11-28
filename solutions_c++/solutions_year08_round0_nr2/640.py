#include <stdio.h>
#include <iostream>
#define maxn 500
using namespace std;
struct Tpoi
{
	int t,type,add;
};
Tpoi s[maxn];
bool cmp(Tpoi a,Tpoi b)
{
	return (a.t < b.t) || (a.t == b.t && a.add > b.add);
}
int main(void)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int N;
	scanf("%d",&N);
	for (int cases = 1;cases <= N;cases++)
	{
		int NA,NB,T;
		scanf("%d%d%d",&T,&NA,&NB);
		for (int i = 0;i < NA;i++)
		{
			int st1,st2,st3,st4;
			scanf("%d:%d %d:%d",&st1,&st2,&st3,&st4);
			s[i + i].t = st1 * 60 + st2;
			s[i + i].type = 1;
			s[i + i].add = -1;
			s[i + i + 1].t = st3 * 60 + st4 + T;
			s[i + i + 1].type = 2;
			s[i + i + 1].add = 1;
		}
		for (int i = NA;i < NA + NB;i++)
		{
			int st1,st2,st3,st4;
			scanf("%d:%d %d:%d",&st1,&st2,&st3,&st4);
			s[i + i].t = st1 * 60 + st2;
			s[i + i].type = 2;
			s[i + i].add = -1;
			s[i + i + 1].t = st3 * 60 + st4 + T;
			s[i + i + 1].type = 1;
			s[i + i + 1].add = 1;
		}
		sort(s,s + (NA + NB) * 2,cmp);
		int ansA = 0,ansB = 0,nowa = 0,nowb = 0;
		for (int i = 0;i < (NA + NB) * 2;i++) if (s[i].type == 1)
		{
			nowa += s[i].add;
			if (nowa < 0)
			{
				ansA -= nowa;
				nowa = 0;
			}
		}
		else
		{
			nowb += s[i].add;
			if (nowb < 0)
			{
				ansB -= nowb;
				nowb = 0;
			}
		}
		printf("Case #%d: %d %d\n",cases,ansA,ansB);
	}
}
