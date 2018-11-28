#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;
ifstream fin("in.in");
int main()
{
	int t,i,k,j,l,n,c,mi,ff;
	long long m;
	long long f[1001][3];
	int a[1000];
	fin>>t;
	for(j=1;j<=t;j++)
	{
		fin>>l>>m>>n>>c;
		//scanf("%d%d%d%d",&l,&m,&n,&c);
		//cout<<"Case #"<<j<<": "<<l<<' '<<m<<' '<<n<<' '<<c<<endl;
		for(i=0;i<c;i++)
			fin>>a[i];
			//scanf("%d",&a[i]);
		f[0][0]=0;
		for(i=1;i<=n;i++)
			f[i][0]=f[i-1][0]+2*a[(i-1)%c];
		for(k=1;k<=l;k++)
		{
			f[0][k]=1000000000;
			for(i=1;i<=n;i++)
			{
				//f[i][k]=min(f[i-1][k]+2*a[(i-1)%c],f[i-1][k-1]+a[(i-1)%c]+zj(t,f[i-1][k-1]));
				ff=f[i][k]=f[i-1][k]+2*a[(i-1)%c];
				if(f[i-1][k-1]>=m)
					ff=f[i-1][k-1]+a[(i-1)%c];
				else if(f[i-1][k-1]+2*a[(i-1)%c]>m)
					ff=m+(f[i-1][k-1]+2*a[(i-1)%c]-m)/2;
				//cout<<i<<' '<<k<<' '<<ff<<' '<<(2*a[(i-1)%c])<<endl;
				if(ff<f[i][k]) f[i][k]=ff;
			}
		}
		//for(k=0;k<=l;k++)
		//	for(i=0;i<=n;i++)
		//		cout<<i<<' '<<k<<' '<<f[i][k]<<endl;
		mi=f[n][0];
		for(k=1;k<=l;k++)
			if(f[n][k]<mi) mi=f[n][k];
		
		cout<<"Case #"<<j<<": "<<mi<<endl;
		//for(i=0;i<c;i++) cout<<a[i]<<' ';
		//c//out<<endl;
	}
	//system("pause");
}
