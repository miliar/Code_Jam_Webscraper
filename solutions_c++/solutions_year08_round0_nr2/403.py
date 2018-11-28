#include<iostream>
#include<algorithm>
using namespace std;
struct node
{
	int start;
	int end;
	int color;
};
node v[209];
int cnta[2000];
int cntb[2000];
int n,m;
int totime(char ch[])
{
	return ((ch[0]-'0')*10+(ch[1]-'0'))*60+(ch[3]-'0')*10+(ch[4]-'0');
}
bool cmp(node a,node b)
{
	return a.start<b.start;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int ca;
	int n,m,t;
	scanf("%d",&ca);
	int i,j;
	int tca=0;
	char a[10];
	char b[10];
	while(tca++<ca)
	{
		scanf("%d%d%d",&t,&n,&m);
		int tp=0;
		for(i=1;i<=n;i++)
		{
			scanf("%s %s",&a,&b);
			v[++tp].start=totime(a);
			v[tp].end=totime(b);
			v[tp].color=1;
		}
		for(i=1;i<=m;i++)
		{
			scanf("%s %s",&a,&b);
			v[++tp].start=totime(a);
			v[tp].end=totime(b);
			v[tp].color=2;
		}
		memset(cnta,0,sizeof(cnta));
		memset(cntb,0,sizeof(cntb));
		int nowa=0;
		int nowb=0;
		int tota=0;
		int totb=0;
		tp=1;
		sort(v+1,v+n+m+1,cmp);
		for(i=0;i<=24*60;i++)
		{
			nowa+=cnta[i];
			nowb+=cntb[i];
			while(v[tp].start==i)
			{
				if(v[tp].color==1)
				{
					while(nowa<1)
					{
						nowa++;
						tota++;
					}
					nowa--;
					cntb[v[tp].end+t]++;
				}
				else 
				{
					while(nowb<1)
					{
						nowb++;
						totb++;
					}
					nowb--;
					cnta[v[tp].end+t]++;
				}
				tp++;
				if(tp>=m+n+1)
					goto out;
			}
		}
		out:
		printf("Case #%d: %d %d\n",tca,tota,totb);
	}
}
