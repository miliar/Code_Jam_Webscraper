#include<iostream>
#include<cstdio>

using namespace std;

int d[1024];
int price[10][512];

int sol(int start,int level)
{
	bool need = false;
	for(int i=start;i<start+(1<<level);i++)
	{
		if (d[i]>0)
		{
			need = true;
			break;
		}
	}

	if (need)
	{
		int sum = 1;
		for(int i=start;i<start+(1<<level);i++)	
			if (d[i]>0) --d[i];
		sum+=sol(start,level-1)+sol(start+(1<<(level-1)),level-1);
		return sum;
	}
	else return 0;
}

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);

	int t;
	cin>>t;

	for(int tt=1;tt<=t;tt++)
	{
		int p;
		cin>>p;
		for(int i=0;i<(1<<p);i++)
		{
			cin>>d[i];
			d[i] = p-d[i];
		}
		for(int i=0;i<p;i++)
			for(int j=0;j<1<<(p-i-1);j++)
				cin>>price[i][j];

		int ans = sol(0,p);

		printf("Case #%d: %d\n",tt,ans);
	}

	return 0;
}
