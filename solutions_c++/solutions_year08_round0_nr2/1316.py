#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<algorithm>
#include<queue>
#include<list>
#include<vector>
#include<string>
using namespace std;	

#define sq(a) ((a)*(a))
#define pb(a) push_back(a)
#define Min(a,b) (((a)<(b))?(a):(b))
#define Max(a,b) (((a)>(b))?(a):(b))
#define eps 1e-9
#define inf 1<<29
#define pye 2.*acos(0.)
#define SZ(v) ((int)(v).size())
#define For(i,a,b) for(i=(a);i<(b);++i)
#define Fore(i,a,b) for(i=(a);i<=(b);++i)
#define Forc(i,v) For(i,0,SZ(v))
#define Foro(i,a) For(i,0,a)

struct journey
{
	int st,nd;
}jora[105],jorb[105];

int calc(char s[])
{
	int ret,h,m;
	h=(s[0]-'0')*10+(s[1]-'0');
	m=(s[3]-'0')*10+(s[4]-'0');
	ret=h*60+m;
	return ret;
}

vector<int> train[2];

bool operator<(journey a,journey b)
{
	return a.st<b.st;
}

int main()
{
	int cs,T,na,nb,t,i,at,bt;
	vector<int>::iterator j;
	char s1[10],s2[10];
	freopen("out4.txt","w",stdout);
	scanf("%d",&T);
	Foro(cs,T)
	{
		scanf("%d%d%d",&t,&na,&nb);
		at=bt=0;
		train[0].clear();
		train[1].clear();
		Foro(i,na)
		{
			scanf("%s%s",s1,s2);
			jora[i].st=calc(s1);
			jora[i].nd=calc(s2);
			train[1].push_back(jora[i].nd+t);
		}
		sort(train[1].begin(),train[1].end());
		sort(jora,jora+na);
		Foro(i,nb)
		{
			scanf("%s%s",s1,s2);
			jorb[i].st=calc(s1);
			jorb[i].nd=calc(s2);
			train[0].push_back(jorb[i].nd+t);
		}
		sort(train[0].begin(),train[0].end());
		sort(jorb,jorb+nb);
		Foro(i,na)
		{
			int got=0;
			for(j=train[0].begin();j!=train[0].end();j++)
				if((*j)<=jora[i].st)
				{
					got=1;
					train[0].erase(j);
					break;
				}
			if(!got)
				at++;
		}
		Foro(i,nb)
		{
			int got=0;
			for(j=train[1].begin();j!=train[1].end();j++)
				if((*j)<=jorb[i].st)
				{
					got=1;
					train[1].erase(j);
					break;
				}
			if(!got)
				bt++;
		}
		printf("Case #%d: %d %d\n",cs+1,at,bt);
	}
	return 0;
}
