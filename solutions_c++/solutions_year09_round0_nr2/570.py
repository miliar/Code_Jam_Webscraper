#include<iostream>
using namespace std;

int a[102][102],n,m,i,j,t,k;
char r[102][102],now;

int di[4] = {-1,0,0,1};
int dj[4] = {0,-1,1,0};

char go(int i,int j)
{
	if(r[i][j]) return r[i][j];
	int min = 0xffff,k;
	for(k=0;k<4;++k)
		if(a[i+di[k]][j+dj[k]] < min) min = a[i+di[k]][j+dj[k]];
	if(min>=a[i][j]) return (r[i][j]=(++now));
	for(k=0;k<4;++k)
		if(a[i+di[k]][j+dj[k]] == min)
			return (r[i][j]=go(i+di[k],j+dj[k]));
	return 0;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>t;k=0;
	while(t--)
	{
		memset(r,0,sizeof(r));
		++k; now = 'a' - 1;
		cin>>n>>m;
		for(i=1;i<=n;++i) for(j=1;j<=m;++j) cin>>a[i][j];
		for(i=0;i<=n+1;++i) a[i][0] = a[i][m+1] = 0xffff;
		for(i=0;i<=m+1;++i) a[0][i] = a[n+1][i] = 0xffff;
		for(i=1;i<=n;++i) for(j=1;j<=m;++j) go(i,j);
		cout<<"Case #"<<k<<":"<<endl;
		for(i=1;i<=n;++i)
		{
			for(j=1;j<=m;++j)
				cout<<r[i][j]<<" ";
			cout<<endl;
		}
	}
	fclose(stdout);
	return 0;
}
