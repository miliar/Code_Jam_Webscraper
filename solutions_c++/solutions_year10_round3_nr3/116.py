#include<iostream>
#include<string>
#include<queue>
#include<algorithm>
#include<map>
#include<set>
#include<deque>
using namespace std;

#define maxn 35

int mat[maxn][maxn];
bool visit[maxn][maxn];
int M,N;

map<int,int> mp;

inline bool ill(int i,int j,int &lowi,int &highi,int &lowj,int &highj)
{
	return i>=lowi && i<=highi && j>=lowj && j<=highj;
}

int dir[4][2]={0,1,-1,0,0,-1,1,0};
bool can(int x,int y,int &lowi,int &highi,int &lowj,int &highj)
{
	if( visit[x][y] ) return false;

	for(int in=0;in<4;in++)
	{
		int t_x=x+dir[in][0];
		int t_y=y+dir[in][1];

		if( ill(t_x,t_y,lowi,highi,lowj,highj) )
		{
			if( mat[t_x][t_y] == mat[x][y] ) return false;
		}
	}
	return true;
}

void check(int i,int j,int size)
{
	int lowi=i,highi=i+size-1,lowj=j,highj=j+size-1;
	if( highi>M || highj>N) return;

	bool flag=true;
	for(int I=lowi;I<=highi && flag;I++)
	{
		for(int J=lowj;J<=highj && flag;J++)
		{
			if( !can(I,J,lowi,highi,lowj,highj) ) 
				flag=false;
		}
	}

	if( flag )
	{
		mp[-size]++;
		for(int I=lowi;I<=highi && flag;I++)
	{
		for(int J=lowj;J<=highj && flag;J++)
		{
			visit[I][J]=true;
		}
	}
	}
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int CAS,Te=1;
	cin>>CAS;
	while(CAS--)
	{
		cin>>M>>N;
		mp.clear();

		for(int i=1;i<=M;i++)
		{
			string s;
			cin>>s;
			int ind=1;
			for(int j=1;j<=N/4;j++)
			{
				char ch=s[j-1];
				int sign;
				if( ch>='A') sign=10+ch-'A';
				else sign=ch-'0';
				for(int k=3;k>=0;k--) 
					if( sign&(1<<k) ) mat[i][ind++]=1;
					else mat[i][ind++]=0;
			}
		}
		memset(visit,false,sizeof(visit));
		mp.clear();

		for(int size=min(N,M);size>=1;size--)
		{
			for(int i=1;i<=M;i++)
				for(int j=1;j<=N;j++)
					check(i,j,size);
		}
		printf("Case #%d: %d\n",Te++,mp.size());
		map<int,int>::iterator it;
		for(it=mp.begin();it!=mp.end();it++)
		{
			printf("%d %d\n",-it->first,it->second);
		}
	}
}