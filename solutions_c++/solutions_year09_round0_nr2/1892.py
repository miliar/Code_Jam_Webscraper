#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

#include<queue>
#include<cmath>
#include<map>
using namespace std;

#define maxn 10000+10
map<int,char>m;
int parent[maxn],num[maxn];
int g[105][105];
int size;
int w,h;
vector<int>v;

void init()
{
	m.clear();
	for(int i=0;i<size;i++)
	{
		parent[i]=i;
		num[i]=1;
	}
}
int find(int a)
{
	int i;
	for(i=a;parent[i]!=i;i=parent[i]);
	return i;
}
void unionset(int a,int b)
{
	a=find(a);
	b=find(b);
	if(a!=b)
	{
		if(num[a]>num[b])
		{
			parent[b]=a;
			num[a]+=num[b];
		}
		else 
		{
			parent[a]=b;
			num[b]+=num[a];
		}
	}
}
int getID(const int & i,const int & j)
{
	return i*w+j;
}
bool issink(const int & i,const int & j)
{
	return ( (i==0 || g[i-1][j]>=g[i][j]) && (i==h-1 || g[i+1][j]>=g[i][j])
		&& (j==0 || g[i][j-1]>=g[i][j]) && (j==w-1 || g[i][j+1]>=g[i][j]) );
}
int numFlow(int i,int j)
{
	int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
	int x,y,ansx,ansy;
	int smin=INT_MAX;
	for(int t=0;t<4;t++)
	{
		x=i+dir[t][0];
		y=j+dir[t][1];

		if(x>=0 && x<h && y>=0 && y<w && g[x][y]<smin)
		{
			smin=g[x][y];
			ansx=x,ansy=y;
		}
	}
	return getID(ansx,ansy);

}
void solve()
{

}
void print()
{

}
int main()
{
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		cin>>h>>w;
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				cin>>g[i][j];
		size=h*w;
		init();


		char ch='a';
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				if(!issink(i,j))
					unionset(i*w+j,numFlow(i,j));
			}
		}

		cout<<"Case #"<<cas<<":"<<endl;


		ch='a';
		int head;
		map<int,char>::iterator it;
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				head=find(i*w+j);
				it=m.find(head);
				if(it!=m.end())
					putchar(it->second);
				else
				{
					putchar(ch);
					m[head]=ch++;
				}
				putchar(' ');
			}
			putchar('\n');
		}
	}
}