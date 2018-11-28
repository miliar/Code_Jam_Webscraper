#include<cstdio>
#include<vector>
using namespace std;

char s[105][105];
int main()
{
	freopen("d:\\data\\A-large.in","r",stdin);
	freopen("d:\\data\\A-large.out","w",stdout);
	int t,c=0,n,i,j,a,b;
	scanf("%d",&t);
	while(t--)
	{
		double ans[105]={0},wp[105]={0},owp[105]={0},oowp[105]={0},x,y;
		vector<int> v[105];
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",s[i]);
		for(i=0;i<n;i++)
		{
			x=y=0;
			for(j=0;j<n;j++)
				if(s[i][j]!='.')
				{
					v[i].push_back(j);
					y++;
					if(s[i][j]=='1')
						x++;
				}
			if(y)
			wp[i]=x/y;
		}
		for(i=0;i<n;i++)
			for(j=0;j<v[i].size();j++)
			{
				a=v[i][j];
				//for(a=0;a<n;a++)
				{
					x=y=0;
					for(b=0;b<n;b++)
						if(b!=i&&s[a][b]!='.')
						{
							y++;
							if(s[a][b]=='1')
								x++;
						}
					if(y)	
					owp[i]+=x/y/v[i].size();
				}
			}
		for(i=0;i<n;i++)
			for(j=0;j<v[i].size();j++)
			{
				oowp[i]+=owp[v[i][j]]/v[i].size();
			}
		printf("Case #%d:\n",++c);	
		for(i=0;i<n;i++)
			//printf("%f %f %f\n",wp[i],owp[i],oowp[i]);
			printf("%f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
}
