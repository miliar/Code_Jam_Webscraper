#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<stack>
#include<cmath>
using namespace std;
char mass[12][12];
int r,c,d;
bool validate(int I,int J,int k)
{
	double ci=0,cj=0;
	double bi=0,bj=0;
	for (int i=I+1;i<I+k-1;i++)
	{
		double sum=0;
		for (int j=J;j<J+k;j++)
		{
			sum+=mass[i][j]-'0'+d;
		}
		bi+=sum;
		ci+=sum*i;
	}
	{
		double sum=0;
		for (int j=J+1;j<J+k-1;j++)
		{
			sum+=mass[I][j]-'0'+d;
		}
		bi+=sum;
		ci+=sum*I;
	}
	{
		double sum=0;
		for (int j=J+1;j<J+k-1;j++)
		{
			sum+=mass[I+k-1][j]-'0'+d;
		}
		bi+=sum;
		ci+=sum*(I+k-1);
	}
	ci/=bi;
	for (int j=J+1;j<J+k-1;j++)
	{
		double sum=0;
		for (int i=I;i<I+k;i++)
		{
			sum+=mass[i][j]-'0'+d;
		}
		bj+=sum;
		cj+=sum*j;
	}
	{
		double sum=0;
		for (int i=I+1;i<I+k-1;i++)
		{
			sum+=mass[i][J]-'0'+d;
		}
		bj+=sum;
		cj+=sum*J;
	}
	{
		double sum=0;
		for (int i=I+1;i<I+k-1;i++)
		{
			sum+=mass[i][J+k-1]-'0'+d;
		}
		bj+=sum;
		cj+=sum*(J+k-1);
	}
	cj/=bj;
	if (k&1)
	{
		if (ci==(I+(k-1)/2)&&cj==(J+(k-1)/2))
		{
			return 1;
		}
	}
	else
	{
		if (ci==(I+(k-1.0)/2)&&cj==(J+(k-1.0)/2))
		{
			return 1;
		}
	}
	return 0;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);	
    freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for (int curt=1;curt<=test;curt++)
	{

		cin>>r>>c>>d;
		for (int i=1;i<=r;i++)
		{
			for (int j=1;j<=c;j++)
			{
				cin>>mass[i][j];
			}
		}
		int res;
		bool ok=0;
		for (int tt=3;tt<=min(r,c);tt++)
		{
			for(int i=1;i<=r-tt+1;i++)
			{
				for (int j=1;j<=c-tt+1;j++)
				{
					if (validate(i,j,tt))
					{
						ok=1;
						res=tt;
					}
				}
			}
		}
		cout<<"Case #"<<curt<<": ";
		if (ok)
			cout<<res;
		else
			cout<<"IMPOSSIBLE";
		cout<<endl;
	}


	return 0;
}