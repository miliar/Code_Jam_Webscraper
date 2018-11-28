#include<iostream>
#include <cmath>
#include<iomanip>

using namespace std;

int a,b;
int cc[200][20];
int mu=9999;
string ms;

void diu(int p,string q)
{
	//cout<<p<<q<<endl;
	if (p==a+1)
	{
		for (int i=0;i<b;i++)
		{
			bool xd=0;
			for (int j=1;j<=a;j++)
			{
				int t=cc[i][j];
				if (t==-1)
					continue;
				if (t==q[j]-'0')
				xd=1;
			}
			if (!xd)
				return;
		}
		int uu=0;
		for (int i=1;i<q.size();i++)
			if (q[i]=='1')
				uu++;
		//cout<<uu<<" "<<q<<endl;
		if (uu<mu)
		{
			mu=uu;
			ms=q;
		}
		return;
	}
	diu(p+1,q+"0");
	diu(p+1,q+"1");
}

int main()
{
	int n;
	cin>>n;
	
	for (int p=0;p<n;p++)
	{
		mu=9999;
		for (int i=0;i<200;i++)
			for (int j=0;j<20;j++)
				cc[i][j]=-1;
		cin>>a>>b;
		for (int i=0;i<b;i++)
		{
			int t;
			cin>>t;
			for (int j=0;j<t;j++)
			{
				int x,y;
				cin>>x>>y;
				cc[i][x]=y;
			}
		}
		//for (int i=0;i<b;i++){
		//	for (int j=0;j<=a;j++)
			//	cout<<cc[i][j]<<' ';
		//cout<<endl;}
		diu(1," ");
		cout<<"Case #"<<p+1<<":";//<<ans[u+1]<<endl;
		if (mu!=9999)
		{
			for (int i=1;i<=a;i++)
				cout<<' '<<ms[i];
			cout<<endl;
		}
		else
			cout<<" IMPOSSIBLE\n";
	}
	return 0;
}