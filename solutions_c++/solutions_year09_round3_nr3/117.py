#include <iostream>

using namespace std;

int f[200][200];
int a[200], q[200];
int n, m, p;
int ans;

void init()
{
	cin>>n>>m;
	for (int i=0;i<m;i++)
		cin>>q[i];
}
void calc()
{
	sort(q,q+m);
	a[0] = 0;
	p = 1;
	for (int i=0;i<m;i++, p++)
		a[i+1] = q[i];
	a[p++] = n+1;
		
	memset(f,-1,sizeof(f));
	for (int i=0;i<p;i++)
	{
		f[i][i] = 0;
		if (i+1<p)
			f[i][i+1] = 0;
	}
	for (int l = 2;l<p;l++)
	for (int i=0;i+l<p;i++)
	{
		int j = i+l;
			for (int k=i+1;k<j;k++)
				if (f[i][k]!=-1 && f[k][j]!=-1)
			{
				int x = f[i][k]+f[k][j]+(a[j]-a[i]-2);
				if (f[i][j]==-1||x<f[i][j])
					f[i][j] = x;
			}
	}
//	cout<<f[0][2]<<' '<<f[2][4]<<' '<<a[4]-a[0]-2<<endl;
	ans = f[0][p-1];
}
int main()
{
	int t;
	cin>>t;
	for (int i=0;i<t;i++)
	{
		init();
		calc();
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}
