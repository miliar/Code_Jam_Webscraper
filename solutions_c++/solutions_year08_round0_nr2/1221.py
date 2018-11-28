#include<stdio.h>
#include<algorithm>
using namespace std;
struct node
{
	int b;
	int e;
	int st;
	bool operator <(node d)
	{
		if(b==d.b) return e<d.e;
		else return b<d.b;
	}
}p[500];
int main()
{
	int n;
	int i,t;
	int a,b,cn;
	char s1[10],s2[10];
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&n);
	for(cn=1;cn<=n;cn++)
	{
		int c=0;
		scanf("%d",&t);
		scanf("%d%d",&a,&b);
		for(i=0;i<a;i++)
		{
			scanf("%s%s",&s1,&s2);
			p[c].b = ((s1[0]-'0')*10+(s1[1]-'0'))*60+(s1[3]-'0')*10+(s1[4]-'0');
			p[c].e = t + ((s2[0]-'0')*10+(s2[1]-'0'))*60+(s2[3]-'0')*10+(s2[4]-'0');
			p[c++].st = 0;
		}
		for(i=0;i<b;i++)
		{
			scanf("%s%s",&s1,&s2);
			p[c].b = ((s1[0]-'0')*10+(s1[1]-'0'))*60+(s1[3]-'0')*10+(s1[4]-'0');
			p[c].e = t + ((s2[0]-'0')*10+(s2[1]-'0'))*60+(s2[3]-'0')*10+(s2[4]-'0');
			p[c++].st = 1;
		}
		sort(p,p+c);
		bool v[300]={0};
		int k=0,sa=0,sb=0;
		while(k<c)
		{
			int state = -1, end=0;
			for(i=0;i<c;i++)
			{
				if(!v[i] && p[i].st != state && p[i].b>=end)
				{
					if(state==-1)
					{
						if(p[i].st==0) sa++;
						else sb++;
					}
					state=p[i].st;
					v[i]=1;
					end = p[i].e;
					k++;
				}
			}
		}
		printf("Case #%d: %d %d\n",cn,sa,sb);
	}
	return 0;
}