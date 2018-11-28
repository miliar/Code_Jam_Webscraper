#include<stdio.h>
#include<vector>
#include<utility>
using namespace std;

typedef pair<int,int> PII;
#define MIN(A,B) ((A) < (B) ? (A) : (B))
#define MAX(A,B) ((A) > (B) ? (A) : (B))

vector<PII> b,nb,my;
//1=not bird, 2 = bird, 0=unknown
int N,M;
int stat[10000];

void PRINT()
{
	int i;

	for(i=0;i<M;i++)
	{
		if(stat[i]==0) printf("UNKNOWN\n");
		else if(stat[i]==1) printf("NOT BIRD\n");
		else printf("BIRD\n");
	}
}

void ZERO()
{
	int i,j;

	for(j=0;j<M;j++)
		for(i=0;i<nb.size();i++)
			if(my[j].first==nb[i].first && my[j].second==nb[i].second)
				stat[j]=1;

	PRINT();
}

inline int IN(int x,int y,int z)
{
	return (x>=y && x<=z);
}

void NONZERO()
{
	int x1,x2,a1,a2;
	int y2,y1,b1,b2;
	int i;

	x1=a1=-100000000;
	x2=a2=100000000;

	y2=y1=b[0].first;
	b2=b1=b[0].second;

	for(i=0;i<b.size();i++)
	{
		y1=MIN(y1,b[i].first);
		y2=MAX(y2,b[i].first);

		b1=MIN(b1,b[i].second);
		b2=MAX(b2,b[i].second);
	}

	for(i=0;i<nb.size();i++)
	{
		if( IN(nb[i].first,y1,y2) )
		{
			if(nb[i].second < b1) a1=MAX(a1,nb[i].second);
			else if(nb[i].second > b2) a2=MIN(a2,nb[i].second);
		}
		
		if( IN(nb[i].second,b1,b2) )
		{
			if(nb[i].first < y1) x1=MAX(x1,nb[i].first);
			else if(nb[i].first > y2) x2=MIN(x2,nb[i].first);
		}
	}

	for(i=0;i<M;i++)
	{
		if(IN(my[i].first,y1,y2) && IN(my[i].second,b1,b2)) stat[i]=2;
		if( my[i].first <= x1 || my[i].first>=x2 || my[i].second <= a1 || my[i].second >= a2) stat[i]=1;
	}

	PRINT();	
}

void SOLVE()
{
	int i,j;
	int h,w;
	char line[100];

	scanf("%d",&N);

	b.clear();
	nb.clear();

	for(i=1;i<=N;i++)
	{
		scanf("%d%d%s",&h,&w,line);
		

		if(line[0]=='B') b.push_back(PII(h,w));
		else nb.push_back(PII(h,w));

		if(line[0]=='N') scanf("%s",line);
	}

	scanf("%d",&M);
	my.clear();
	for(i=0;i<M;i++)
	{
		stat[i]=0;
		scanf("%d%d",&h,&w);
		my.push_back(PII(h,w));
	}

	if(b.size()==0) ZERO();
	else NONZERO();
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int T,ks;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d:\n",ks);
		SOLVE();
	}

	return 0;
}