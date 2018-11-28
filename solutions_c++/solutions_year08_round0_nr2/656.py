#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int nn,ii,delay;
int a[500][3],b[500];
bool g[500][500];
bool vis[500];
int n;
bool dfs(int x)
{
	int i,t;
	for (i=1;i<=n;i++)
		if ((!vis[i])&&(g[x][i]))
		{
			vis[i]=true;
			t=b[i];
			b[i]=x;
			if ((t==0)||(dfs(t))) return true;
			b[i]=t;
		}
	return false;
}
int main()
{
	int na,nb,i,j,t1,t2,t,num1,num2;
	char ch;
	ifstream cin("b-large.in");
	ofstream cout("b-large.out");
	cin >>nn;

	for (ii=1;ii<=nn;ii++)
	{
		cin >>delay;
		cin >>na >>nb;
		for (i=1;i<=na;i++)
		{
			cin >>t1 >>ch >>t2;
			a[i][0]=t1*60+t2;
			cin >>t1 >>ch >>t2;
			a[i][1]=t1*60+t2;
			a[i][2]=0;
		}
		for (i=1;i<=nb;i++)
		{
			cin >>t1 >>ch >>t2;
			a[i+na][0]=t1*60+t2;
			cin >>t1 >>ch >>t2;
			a[i+na][1]=t1*60+t2;
			a[i+na][2]=1;
		}
		n=na+nb;
		for (i=1;i<=n-1;i++)
			for (j=i+1;j<=n;j++)
				if ((a[i][0]>a[j][0])||((a[i][0]==a[j][0])&&(a[i][1]>a[j][1])))
				{
					t=a[i][0];a[i][0]=a[j][0];a[j][0]=t;
					t=a[i][1];a[i][1]=a[j][1];a[j][1]=t;
					t=a[i][2];a[i][2]=a[j][2];a[j][2]=t;
				}
		num1=0;num2=0;
		memset(g,false,sizeof(g));
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
				if ((a[i][0]>=a[j][1]+delay)&&(a[i][2]==1-a[j][2]))
					g[i][j]=true;
		memset(b,0,sizeof(b));
		for (i=1;i<=n;i++)
		{
			memset(vis,false,sizeof(vis));
			dfs(i);
		}
		memset(vis,false,sizeof(vis));
		for (i=1;i<=n;i++)
			if (b[i]>0)
				vis[b[i]]=true;
		for (i=1;i<=n;i++)
			if (!vis[i])
			{
				if (a[i][2]==0) num1++; else num2++;
			}

		cout <<"Case #" <<ii <<": " <<num1 <<" " <<num2 <<endl;
	}
	return 0;
}






