#pragma comment(linker,"/STACK:256000000")
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <math.h>
#include <set>
#include <map>
using namespace std;



int main()
{
	//freopen("1.txt","rt",stdin);
	//freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-large.in","rt",stdin);
	//freopen("OutSmall_A.txt","wt",stdout);
	freopen("OutLarge_A.txt","wt",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		scanf("%d\n",&n);
		vector<string> s(n);
		for(int j=0;j<n;j++)
			getline(cin,s[j]);
		vector<int> null(n,-1);
		vector<vector<int>> d(n,null);
		pair<int,int> n0=make_pair(0,0);
		vector<pair<int,int>> wp(n,n0);
		for(int j=0;j<n;j++)
			for(int k=0;k<n;k++)
			{
				if(s[j][k]=='1')
				{
					d[j][k]=1;
					wp[j].first++;
					wp[j].second++;
				}
				if(s[j][k]=='0')
				{
					d[j][k]=0;
					wp[j].second++;
				}
			}
		vector<pair<double,int>> owp(n,n0);
		for(int j=0;j<n;j++)
			for(int k=0;k<n;k++)
			{
				if(d[j][k]==1 || d[j][k]==0)
				{
					if(d[j][k]==1)
					{
						owp[j].first+=(double)wp[k].first/(wp[k].second-1);
					}
					else
						owp[j].first+=(double)(wp[k].first-1)/(wp[k].second-1);
				}
			}
		vector<double> oowp(n,0);
		for(int j=0;j<n;j++)
			for(int k=0;k<n;k++)
			{
				if(d[j][k]==1 || d[j][k]==0)
				{
					oowp[j]+=owp[k].first/wp[k].second;
				}
			}
		printf("Case #%d:\n",i);
		for(int j=0;j<n;j++)
			printf("%.12lf\n",double(0.25*wp[j].first+0.5*owp[j].first+0.25*oowp[j])/wp[j].second);
	}

	





			



fclose(stdout);
}