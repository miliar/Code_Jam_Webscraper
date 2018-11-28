#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;
int n,s,p,a[10005];
FILE *fp;
bool cmp(int a,int b)
{
	return a>b;
}
int main()
{
	fp=fopen("1.out","w");
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n,cmp);int cnt=0,ans=0;
		for(int i=0;i<n;i++)
		{
			int tem=a[i]%3,tep=a[i]/3;
			if(s-cnt<n-i)
			{
				if(tem==2)
				{
					if(tep+1>=p)ans++;
					else if(cnt<s)
					{
						if(tep+2>=p)ans++;
						cnt++;
					}
				}
				else if(tem==1)
				{
					if(tep+1>=p)ans++;
					else if(cnt<s)
					{
						if(tep+1>=p)ans++;
						cnt++;
					}
				}
				else 
				{
					if(tep>=p)ans++;
					else if(cnt<s&&tep>0)
					{
						if(tep+1>=p)ans++;
						cnt++;
					}
				}
			}
			else
			{
				if(tem==2&&tep+2>=p)
					ans++;
				else if(tem==1&&tep+1>=p)
					ans++;
				else if(tep>0&&tep+1>=p)
					ans++;
				cnt++;
			}
		}
		if(cnt<s)ans=0;
		printf("Case #%d: %d\n",t,ans);
		/*fprintf(fp,"Case #%d: %d\n",t,ans);*/
	}
	return 0;
}