#include <cstdio>
#include <cstring>

char mp[200][200];

double wp[200];
double owp[200];
double oowp[200];

int n;

double calc_wp(int line, int ignore)
{
	int i;
	int count=0,total=0;
	for(i=0;i<n;i++)
	{
		if(i==ignore) continue;
		if(mp[line][i]!='.') total++;
		if(mp[line][i]=='1') count++;
	}
	return (double)count/total;
}

double calc_owp(int line)
{
	int i;
	double sum=0;
	int total=0;
	for(i=0;i<n;i++)
	{
		if(mp[line][i]!='.') sum+=calc_wp(i,line),total++;
	}
	return sum/total;
}

double calc_oowp(int line)
{
	int i;
	double sum=0;
	int total=0;
	for(i=0;i<n;i++)
	{
		if(mp[line][i]!='.') sum+=owp[i],total++;
	}
	return sum/total;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int ca=1;
	int i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		gets(mp[0]);
		for(i=0;i<n;i++)
			gets(mp[i]);
		for(i=0;i<n;i++)
		{
			wp[i]=calc_wp(i,-1);
		}
		for(i=0;i<n;i++)
		{
			owp[i]=calc_owp(i);
		}
		for(i=0;i<n;i++)
		{
			oowp[i]=calc_oowp(i);
		}
		printf("Case #%d:\n",ca++);
		for(i=0;i<n;i++)
			printf("%.7lf\n",wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25);
	}
	return 0;
}