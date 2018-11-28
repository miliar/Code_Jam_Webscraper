#include<iostream>
#include<cstdio>
#include<cstring>
#include<set>

using namespace std;

char s[10];
char t[10];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		int a,b,ans = 0;
		cin>>a>>b;
		for(int n=a;n<=b;n++)
		{
			set<int> se;
			sprintf(s,"%d",n);
			for(int i=1;s[i];i++)
			{
				if (s[i]=='0') continue;
				int j;
				for(j=0;s[i+j];j++) t[j] = s[i+j];
				for(int k=0;s[j];j++) t[j] = s[k++];
				t[j] = 0;
				int m;
				sscanf(t,"%d",&m);
				if (m>=a&&m<=b&&m>n) se.insert(m);
			}
			ans+=se.size();
		}
		printf("%d\n",ans);
	}
	return 0;
}