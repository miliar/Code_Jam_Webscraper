#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		int ans = 0,n,s,p;
		cin>>n>>s>>p;
		for(int i=0;i<n;i++)
		{
			int t;
			cin>>t;
			int b = t/3;
			if (t<2) { ans+=p==t; continue; }
			if (t>27) { ++ans; continue; }

			switch(t%3)
			{
			case 0:
				if (b>=p) ++ans;
				else if (b+1==p&&s>0) { --s; ++ans; }
				break;
			case 1:
				if (t%3==1)
					if (b+1>=p) ++ans;
				break;
			case 2:
				if (b+1>=p) ++ans;
				else if (b+2==p&&s>0) { --s; ++ans; }
				break;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}