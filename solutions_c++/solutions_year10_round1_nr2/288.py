#include<iostream>
#include<fstream>
using namespace std;

int f[102][256];
int a[102];
int d,inc,m,n,t,c;
int minn;
int sum;

int calc(int k,int j,int t)
{
	int min=1000000000;
	int sum;
	//shanshu
	sum=d+inc*(abs(j-k)/m);
	if (sum<min) min=sum;

	//bushan
	sum=inc*(abs(j-t)-1/m)+inc*(abs(t-k)-1/m);
		if (sum<min) min=sum;

	//gaishu
	for (int i=0;i<256;i++)
	{
		sum=inc*(abs(j-i)-1/m)+inc*(abs(i-k)-1/m);
		if (sum<min) min=sum;
	}
	return min;
}

	




int main()
{
	cin>>t;
	for (int c=1;c<=t;c++)
	{
		cin>>d>>inc>>m>>n;
		for (int i=1;i<=n;i++) cin>>a[i];
	
	for (int i=0;i<256;i++) f[0][i]=0;
	for (int i=1;i<=n;++i)
	{
		for (int j=0;j<256;j++)
		{
			minn=1000000000;
			for (int k=0;k<256;k++)
			{
				sum=calc(k,j,a[i])+f[i-1][k];
				//if (sum==0) cout<<j<<' '<<k<<' '<<a[i]<<endl;
				if (sum<minn) minn=sum;
			}
			f[i][j]=minn;
			cout<<i<<' '<<j<<' '<<f[i][j]<<endl;
		}
		system("pause");
	}

	minn=1000000000;
	for (int i=0;i<256;i++)
		if (f[n][i]<minn) minn=f[n][i];
	cout<<"Case #"<<c<<": "<<minn<<endl;
}
	return 0;
}

