#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <algorithm>
using namespace std;

const int MaxM=1000000000;
int c, d, p, v;
int l[101];
int f[600000][101];
int minp, maxp;

int main ()
{
	freopen("B-small-attempt1.in", "r", stdin);
	ofstream fout("b.txt");
//	freopen("b.txt", "w", stdout);
	int T;
	int tmp;
	int best;
	cin>>T;
	int n;
	for(int t=1; t<=T; ++t)
	{
		cin>>c>>d;
		n=0;
		d=d*2;
		minp=100000*2;
		maxp=-minp;
		for(int i=0; i<c; ++i)
		{
			cin>>p>>v;
			p*=2;
			for(int j=n; j<n+v; ++j)
				l[j]=p;
			n+=v;
			if (p>maxp)	maxp=p;
			if (p<minp) minp=p;
		}
		sort(l,l+n);
		minp-=d*n;
		//fout<<minp<<"!!!"<<n<<endl;
		maxp+=d*n;
		best=MaxM+1;
		for(int i=0; i<n; ++i)
		{
			l[i]-=minp;	
		}
		maxp-=minp; minp=0;
		//cout<<maxp<<" "<<minp;
		for(int i=0; i<maxp; ++i)
		{
			//fout<<i<<"!"<<maxp<<endl;
			tmp=labs(l[0]-i);
			if (i!=0)
				f[i][0]=tmp<f[i-1][0]? tmp:f[i-1][0];
			else f[i][0]=tmp;
			
			for(int j=1; j<n; ++j)
			{
				if (i>0) f[i][j]=f[i-1][j]; else f[i][j]=MaxM;
				if (i-d>=0)
				{
					tmp=labs(l[j]-i);
					tmp=f[i-d][j-1]>tmp? f[i-d][j-1]:tmp;
					f[i][j]=tmp<f[i][j]? tmp:f[i][j];
				}
				//if (f[i-1][j]==MaxM && f[i][j]!=MaxM) fout<<i<<" ! "<<j<<endl;
			//fout<<i<<" "<<j<<" "<<f[i][j]<<endl;
			}
		}
	//	for(int i=0; i<maxp; ++i)
		//	fout<<i<<"   "<<double(f[i][n-1])/2 <<endl;
		best=f[maxp-1][n-1];

		fout<<"Case #"<<t<<": "<<fixed<<setprecision(1)<<double(best)/2<<endl;
	}
//			while (1){};
}
