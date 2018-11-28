#include <iostream>
using namespace std;

int n,t;
char a[50][50];
int b[50],f[50],g[50];
void init()
{
	cin>>n;
	int i,j;
	memset(b,0,sizeof(b));
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++)
		{
			cin>>a[i][j];
			if (a[i][j]=='1') b[i]=j;
		}
	memset(f,0,sizeof(f));
	for (i=1;i<=n;i++)
	{
		j=b[i];
		if (j==0) j=1;
		while (f[j]>0) j++;
		g[i]=j;
		f[j]=i;
	}

}
void search(int k)
{
	int j,i;
	j=f[k];
	if (j==k) return;
	for (i=j-1;i>=k;i--)
	{
		f[g[i]]+=1;
		g[i+1]=g[i];
		t++;
	}
}
void make()
{
	int i;
	t=0;
	for (i=1;i<=n;i++) 
	{
		search(i);
	}
	cout<<t<<endl;
}

int main()
{
	freopen("A-large.in","r",stdin);
 	freopen("output.txt","w",stdout);
	int cs;
	cin>>cs;
	int i;
	for (i=1;i<=cs;i++)
	{
		init();
		cout<<"Case #"<<i<<": ";
		make();
	}

	return 0;
}