#include <iostream>
using namespace std;

const int maxn=200010;

int test;
long long n,a,b,c,d,xx,yy,m,x[maxn],y[maxn],tak[3][3],dota[3][3],inyeki[maxn][3][3],sol;

int main()
{
	cin >> test;
	for (int w=1;w<=test;w++)
	{
		cin >> n >> a >> b >> c >> d >> xx >> yy >> m;
		x[1]=xx;
		y[1]=yy;
		for (int i=2;i<=n;i++)
		{
			x[i]=(a*x[i-1]+b)%m;
			y[i]=(c*y[i-1]+d)%m;
		}
		for (int j=0;j<3;j++)
			for (int k=0;k<3;k++)
			{
				tak[j][k]=dota[j][k]=0;
				for (int i=0;i<=n;i++)
					inyeki[i][j][k]=0;
			}
		for (int i=1;i<=n;i++)
		{
			x[i]%=3;
			y[i]%=3;
		}
		sol=0;
		for (int i=1;i<=n;i++)
			tak[x[i]][y[i]]++;
		for (int i=1;i<=n;i++)
			for (int j=0;j<3;j++)
				for (int k=0;k<3;k++)
				{
					int numx=(j-x[i]+300)%3;
					int numy=(k-y[i]+300)%3;
					long long num=tak[numx][numy];
					if (x[i]==numx && y[i]==numy)
						num--;
					inyeki[i][j][k]=num;
					dota[j][k]+=num;
				}
		for (int i=1;i<=n;i++)
		{
			int numx=(3-x[i])%3;
			int numy=(3-y[i])%3;
			sol+=dota[numx][numy]-2*inyeki[i][numx][numy];
		}
		cout << "Case #"<<w<<": "<<sol/6 << endl;
	}
	return 0;
}
