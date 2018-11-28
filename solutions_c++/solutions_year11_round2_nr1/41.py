#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

string board[100];
double rp[100];
int w[100],t[100];
double owp[100];
double oowp[100];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int n,i,j,k,T;

	cin>>T;
	for(int test=1;test<=T;test++)
	{
		cin>>n;
		for(i=0;i<n;i++) cin>>board[i];
		memset(rp,0,sizeof(rp));
		memset(w,0,sizeof(w));
		memset(t,0,sizeof(t));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				if (board[i][j]!='.')
				{
					++t[i];
					if (board[i][j]=='1') ++w[i];
				}
		}
		for(i=0;i<n;i++)
		{
			int p=0;
			for(j=0;j<n;j++)
				if (board[i][j]!='.')
				{
					++p;
					owp[i]+=1.*(w[j]-(board[i][j]=='0'))/(t[j]-1);
				}
			owp[i]/=p;			
		}
		for(i=0;i<n;i++)
		{
			int p=0;
			for(j=0;j<n;j++)
				if (board[i][j]!='.')
				{
					++p;
					oowp[i]+=owp[j];
				}
			oowp[i]/=p;
			rp[i]=0.25*w[i]/t[i]+0.5*owp[i]+0.25*oowp[i];
		}
		printf("Case #%d:\n",test);
		for(i=0;i<n;i++) printf("%.8lf\n",rp[i]);
	}

	return 0;
}