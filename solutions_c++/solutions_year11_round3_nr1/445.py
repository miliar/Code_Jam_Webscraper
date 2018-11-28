#include <iostream>
#include <cstring>
using namespace std;

char a[60][60];
int i,j,n,m,t,ca;
bool flg;

void work()
{
	int i,j;
	for (i=0;i<n;i++)
	for (j=0;j<m;j++)
	if (a[i][j]=='#')
	{
		if ((a[i][j+1]=='#')&&(a[i+1][j]=='#')&&(a[i+1][j+1]=='#'))
		{
			a[i][j]='/';
			a[i+1][j+1]='/';
			a[i][j+1]=92;
			a[i+1][j]=92;
		} else
		{
			flg=false;
			return;
		}
	}
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("ou.ou","w",stdout);
	cin>>t;
	while (t--)
	{
		ca++;
		cout<<"Case #"<<ca<<":"<<endl;
		memset(a,0,sizeof(a));
		cin>>n>>m;
		for (i=0;i<n;i++)
		for (j=0;j<m;j++) cin>>a[i][j];
		flg=1;
		work();
		if (!flg) cout<<"Impossible"<<endl;
		else
		{
			for (i=0;i<n;i++)
			{
				for (j=0;j<m;j++)
				if (a[i][j]!='@') cout<<a[i][j];
				else cout<<"\\";
				cout<<endl;
			}
		}
	}
}
