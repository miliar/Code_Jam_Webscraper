#include <iostream>
#include <fstream>
#include <string>
using namespace std;
string st;
int zhouqi,final;
int b[10];
bool vis[10];
char a[10000];
void check()
{
	int base=0,i,j,s;
	for (i=1;i<=st.length()/zhouqi;i++)
	{
		for (j=1;j<=zhouqi;j++)
			a[j+base]=st[b[j]+base-1];
		base+=zhouqi;
	}
	a[0]='1';s=0;
	for (i=1;i<=st.length();i++)
		if (a[i]!=a[i-1]) s++;
	if (s<final) final=s;
}


void dfs(int step)
{
	if (step>zhouqi)
	{
		check();
		return;
	}
	int i;
	for (i=1;i<=zhouqi;i++)
		if (!vis[i])
		{
			b[step]=i;
			vis[i]=true;
			dfs(step+1);
			vis[i]=false;
			b[step]=0;
		}
}

int main()
{
	ifstream cin("d-small.in");
	ofstream cout("d-small.out");
	int nn,ii;
	cin >>nn;
	for (ii=1;ii<=nn;ii++)
	{
		cin >>zhouqi;
		cin >>st;
		memset(vis,false,sizeof(vis));
		final=100000;
		dfs(1);
		cout <<"Case #" <<ii <<": ";
		cout <<final <<endl;
	}
	return 0;
}
