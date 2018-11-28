#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <stdio.h>
#include <queue>



using namespace std;
int T,test,a[1000][1000];
double wp[1000],owp[1000],oowp[1000],rpi[1000];
char c;
__int64 ans,n;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	for(test=1;test<=T;test++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				cin>>c;
				if(c=='1')
					a[i][j]=1;
				if(c=='.')
					a[i][j]=-1;
				if(c=='0')
					a[i][j]=0;
			}

		for(int i=0;i<n;i++)
		{
			int A=0,B=0;
			for(int j=0;j<n;j++)
			{
				if(a[i][j]==1)
					A++,B++;
				if(a[i][j]==0)
					B++;
			}
			if(B!=0)
				wp[i]=1.0*A/B;
			else
				wp[i]=0;
		}
		for(int i=0;i<n;i++)
		{
			int k=0;
			double cur=0,w=0;
			for(int j=0;j<n;j++)
			{
				if(a[i][j]!=-1)
				{
					k++;
					int A=0,B=0;
					for(int l=0;l<n;l++)
					{
						if(l==i)
							continue;
						if(a[j][l]==1)
							A++,B++;
						if(a[j][l]==0)
							B++;
					}
					if(B!=0)
						w=1.0*A/B;
					else
						w=0;
					cur+=w;
				}
			}
			owp[i]=cur/k;
		}
		for(int i=0;i<n;i++)
		{
			int k=0;
			double cur=0;
			for(int j=0;j<n;j++)
			{
				if(a[i][j]!=-1)
					k++,cur+=owp[j];
			}
			oowp[i]=cur/k;
		}
		for(int i=0;i<n;i++)
			rpi[i]=wp[i]/4+owp[i]/2+oowp[i]/4;
		cout<<"Case #"<<test<<": "<<endl;
		for(int i=0;i<n;i++)
			printf("%.6lf\n" ,rpi[i]);
	}
	return 0;
}