#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
char a[105][105];
double WP[105],OWP[105],OOWP[105];
int n;
int cnt[105];
double wp(int i,int x)
{
	int m = 0;
	double	k = 0;
	for(int j=0;j<n;j++)
		if(j == x) continue;
		else if(a[i][j]!='.')
		{
			m++;
			k+=a[i][j]-'0';
		}
		return k/m;
}
int main()
{
	freopen("A-small.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int TC,m;
	int i,j,k;
	scanf("%d",&TC);
	for(int tc=1;tc<=TC;tc++)
	{
		cerr<<tc<<endl;
		memset(WP,0,sizeof(WP));
		memset(OWP,0,sizeof(OWP));
		memset(OOWP,0,sizeof(OOWP));

		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",a+i);
			cnt[i] = n-count(a[i],a[i]+n,'.');
		}
	
		for(i=0;i<n;i++)
			WP[i] = wp(i,-1);
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				if(i==j || a[i][j]=='.') continue;
				else OWP[i]+=wp(j,i);
			OWP[i]/=(cnt[i]);
		}
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(i==j || a[i][j]=='.') continue;
				else OOWP[i]+=OWP[j]/cnt[i];
		
		
		printf("Case #%d:\n",tc);
		for(i=0;i<n;i++)
			printf("%.12lf\n",WP[i]/4+OWP[i]/2+OOWP[i]/4);
	}
	return 0;
}