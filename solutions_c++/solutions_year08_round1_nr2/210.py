#include <iostream>
#include <fstream>
using namespace std;
struct arr1
{
	int num;
	int x[100][2];
};
arr1 a[200];
int b[20],final[20];
int n,m,res;
bool check()
{
	int i,j;
	bool p;
	for (i=1;i<=m;i++)
	{
		p=false;
		for (j=1;j<=a[i].num;j++)
			if (b[a[i].x[j][0]]==a[i].x[j][1]) 
			{
				p=true;
				break;
			}
		if (!p) return false;
	}
	return true;
}

void dfs(int step)
{
	int i,t;
	if (step>n)
	{
		if (check()) 
		{
			t=0;
			for (i=1;i<=n;i++)
				t+=b[i];
			if (t<res)
			{
				res=t;
				memcpy(final,b,sizeof(final));
			}
		}
		return;
	}	
	for (i=0;i<=1;i++)
	{
		b[step]=i;
		dfs(step+1);
		b[step]=0;
	}
}
int main()
{
	int nn,ii,i,j;
	ifstream cin("b-small.in");
	ofstream cout("b-small.out");
	cin >>nn;
	for (ii=1;ii<=nn;ii++)
	{
		cin >>n >>m;
		for (i=1;i<=m;i++)
		{
			cin >>a[i].num;
			for (j=1;j<=a[i].num;j++)
				cin >>a[i].x[j][0] >>a[i].x[j][1];
		}
		res=10000;
		memset(b,0,sizeof(b));
		dfs(1);
		cout <<"Case #" <<ii <<":";
		if (res==10000)
			cout <<" IMPOSSIBLE" <<endl;
		else
		{
			for (i=1;i<=n;i++)
			cout <<" " <<final[i];
			cout <<endl;
		}
	}
	return 0;
}

