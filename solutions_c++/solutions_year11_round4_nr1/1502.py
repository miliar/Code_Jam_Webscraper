#include<iostream>
#include<cstdio>
#include<algorithm>
using std::cin;
using std::cout;
using std::endl;

int main()
{
	freopen("gin","r",stdin);
	freopen("gout","w",stdout);
	int ca, cou;
	cin>>ca;
	for (cou=1;cou<=ca;cou++)
	{
		int n,org,run,lim,m;
		int h[201]={0};
		cin>>n>>org>>run>>lim>>m;
		
		int begin=0, end=0, w=0;
		for (int i=0;i<m;i++)
		{
			int tbegin, tend, tw;
			cin>>tbegin>>tend>>tw;
			h[org]+=tbegin-end;
			h[org+tw]+=tend-tbegin;
			begin=tbegin;
			end=tend;
			w=tw;
		}
		h[org]+=n-end;			

		double limit=lim;
		double sum=0;
		for (int i=1;i<200;i++)
		{
			if (limit>=(double)h[i]/(double)(i+run-org))
			{
				limit-=(double)h[i]/(double)(i+run-org);
				sum+=(double)h[i]/(double)(i+run-org);
			}
			else
			{
				sum+=limit+(double)(h[i]-limit*(i+run-org))/(double)i;
				limit=0;
			}
		}
		printf("Case #%d: %.9lf\n", cou, sum);
	}
}
