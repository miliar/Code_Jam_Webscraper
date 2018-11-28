#include<iostream>
using namespace std;
#define  maxn 210
int nx,ny,m,cx[maxn],cy[maxn];
bool map[maxn][maxn],sy[maxn];
bool path(int u)
{
	int v;
	for(v=1;v<=ny;v++)
		if(map[u][v]&&!sy[v])
		{ 
			sy[v]=true;
			if(!cy[v]||path(cy[v]))
			{ 
				cx[u]=v;cy[v]=u; 
				return true;
			}
		} 
		return false;
}
int MaximumMatch()
{ 
	int i,ret=0;
	memset(cx,0,sizeof(cx));
	memset(cy,0,sizeof(cy));
	for(i=1;i<=nx;i++) 
		if(!cx[i]) 
		{
			memset(sy,0,sizeof(sy));
			ret+=path(i); 
		} 
	return ret;
}

int a[210][2],b[210][2];;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int l,Ncase;  cin>>Ncase;
	int i,k,T,NA,NB,answer1,answer2;
	char s1[10],s2[10];
	for(l=1;l<=Ncase;l++)
	{
		scanf("%d%d%d",&T,&NA,&NB);
		for(i=1;i<=NA;i++)
		{
			scanf("%s%s",s1,s2);
			a[i][0]=(s1[0]-'0')*600+(s1[1]-'0')*60+(s1[3]-'0')*10+(s1[4]-'0');
			a[i][1]=(s2[0]-'0')*600+(s2[1]-'0')*60+(s2[3]-'0')*10+(s2[4]-'0');
		}
		for(i=1;i<=NB;i++)
		{
			scanf("%s%s",s1,s2);
			b[i][0]=(s1[0]-'0')*600+(s1[1]-'0')*60+(s1[3]-'0')*10+(s1[4]-'0');
			b[i][1]=(s2[0]-'0')*600+(s2[1]-'0')*60+(s2[3]-'0')*10+(s2[4]-'0');
		}

		memset(map,0,sizeof(map));
		for(i=1;i<=NA;i++)
			for(k=1;k<=NB;k++)
			{
				if(a[i][1]+T<=b[k][0])map[i][k+NA]=true;
				if(b[k][1]+T<=a[i][0])map[k+NA][i]=true;
			}
				
		nx=NA+NB;ny=NA;answer1=NA-MaximumMatch();
		nx=NA;ny=NA+NB;answer2=NB-MaximumMatch();
		printf("Case #%d: %d %d\n",l,answer1,answer2);
	}

	return 0;
}
