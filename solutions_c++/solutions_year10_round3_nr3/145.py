#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <deque>
using namespace std;

#define Max_num 600

int mat[Max_num][Max_num];

bool visit[Max_num][Max_num];

int M_Row,N_Col;

map<int,int> Map_Store;

inline bool Illegal(int i,int j,int &lowi,int &highi,int &lowj,int &highj)
{
	return i>=lowi && i<=highi && j>=lowj && j<=highj;
}

int Direction[4][2]={0,1,-1,0,0,-1,1,0};


bool CanBeDone(int x,int y,int &lowi,int &highi,int &lowj,int &highj)
{
	if( visit[x][y] ) return false;

	for(int in=0;in<4;in++)
	{
		int t_x=x+Direction[in][0];
		int t_y=y+Direction[in][1];

		if( Illegal(t_x,t_y,lowi,highi,lowj,highj) )
		{
			if( mat[t_x][t_y] == mat[x][y] ) return false;
		}
	}
	return true;
}

int Dark();

int Again(int,int);

void Solve(int,int,int);

int main()
{
	freopen("C-small.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int CAS,Te=1;
	cin>>CAS;
	while(CAS--)
	{
		cin>>M_Row>>N_Col;

		Map_Store.clear();

		for(int i=1;i<=M_Row;i++)
		{
			string s;
			cin>>s;
			int ind=1;
			for(int j=1;j<=N_Col/4;j++)
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
		Map_Store.clear();

		for(int size=min(N_Col,M_Row);size>=1;size--)
		{
			for(int i=1;i<=M_Row;i++)
				for(int j=1;j<=N_Col;j++)
					Solve(i,j,size);
		}
		printf("Case #%d: %d\n",Te++,Map_Store.size());
		map<int,int>::iterator it;
		for(it=Map_Store.begin();it!=Map_Store.end();it++)
		{
			printf("%d %d\n",-it->first,it->second);
		}
	}
}



void Solve(int i,int j,int size)
{
	int lowi=i,highi=i+size-1,lowj=j,highj=j+size-1;
	if( highi>M_Row || highj>N_Col) return;

	bool flag=true;
	for(int I=lowi;I<=highi && flag;I++)
	{
		for(int J=lowj;J<=highj && flag;J++)
		{
			if( !CanBeDone(I,J,lowi,highi,lowj,highj) ) 
				flag=false;
		}
	}

	if( flag )
	{
		Map_Store[-size]++;
		for(int I=lowi;I<=highi && flag;I++)
		{
			for(int J=lowj;J<=highj && flag;J++)
			{
				visit[I][J]=true;
			}
		}
	}
}

int Dark()
{
	int i,j;
	return 0;
}

int Again(int,int)
{
	int i,j;
	return 1000;
}