
#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

char p[110][110];
double wp[110],owp[110],oowp[110],ret[110];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("tt.out","w",stdout);
	int T,n,beat,sum,cases=1;
	double x,y;
	cin >>T;
	while (T--)
	{
		cin >>n;
		for(int i=0;i<n;i++){
			scanf("%s",&p[i]);
			beat=sum=0;
			for(int j=0;j<n;j++)
			{
				if(p[i][j]=='1')
					sum++,beat++;
				if(p[i][j]=='0')
					sum++;
			}
			wp[i]=(double)beat/sum;
		}
		
		for(int i=0;i<n;i++)
		{
			x=0.0;
			sum=0;
			for(int j=0;j<n;j++){
				if(p[i][j]=='.')
					continue;
				int tb,ts;
				tb=ts=0;
				for(int k=0;k<n;k++)
				{
					if(k==i) continue;
					if(p[j][k]=='1')
						tb++,ts++;
					if(p[j][k]=='0')
						ts++;
				}
				x+=(double)tb/ts;
				sum++;
			}
			owp[i]=(double)x/sum;
		}
		for(int i=0;i<n;i++)
		{
			x=0.0;
			sum=0;
			for(int j=0;j<n;j++){
				if(p[i][j]=='.')
					continue;
				x+=owp[j];
				sum++;
			}
			oowp[i]=(double)x/sum;
		}
		for(int i=0;i<n;i++){
			ret[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		}
		cout <<"Case #"<<cases++<<":"<<endl;
		for(int i=0;i<n;i++)
			cout <<ret[i]<<endl;
	}
	return 0;
}