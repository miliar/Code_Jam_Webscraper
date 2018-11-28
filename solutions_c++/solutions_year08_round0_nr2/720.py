#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int casen,ii,delay;
int a[500][3],b[500];
int g[500][500];
int vis[500];
int n;
int find(int x)
{
	int i,t;
	for (i=1;i<=n;i++)
		if ((!vis[i])&&(g[x][i]))
		{
			vis[i]=true;
			t=b[i];
			b[i]=x;
			if ((t==0)||(find(t))) return true;
			b[i]=t;
		}
	return 0;
}
int main()
{
	int na,nb,i,j,t1,t2,t,cnt1,cnt2;
	char ch;
	ifstream cin("data.in");
	ofstream cout("data.out");
	cin >>casen;

	for (ii=1;ii<=casen;ii++)
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
		cnt1=0;cnt2=0;
		memset(g,0,sizeof(g));
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
				if ((a[i][0]>=a[j][1]+delay)&&(a[i][2]==1-a[j][2]))
					g[i][j]=true;
		memset(b,0,sizeof(b));
		for (i=1;i<=n;i++)
		{
			memset(vis,0,sizeof(vis));
			find(i);
		}
		memset(vis,0,sizeof(vis));
		for (i=1;i<=n;i++)
			if (b[i]>0)
				vis[b[i]]=true;
		for (i=1;i<=n;i++)
			if (!vis[i])
			{
				if (a[i][2]==0) cnt1++; else cnt2++;
			}

		cout <<"Case #" <<ii <<": " <<cnt1 <<" " <<cnt2 <<endl;
	}
	return 0;
}






