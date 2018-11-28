#include<iostream>

using namespace std;

char s[50][51];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	cin>>T;
	for(int tt=1;tt<=T;++tt)
	{
		int n,k;
		cin>>n>>k;
		for(int i=0;i<n;i++)
			scanf("%s",s[i]);

		for(int i=n-1;i>=0;i--)
		{
			int p = n-1;
			while(p>=0&&s[i][p]!='.') --p;
			for(int j=p-1;j>=0;j--)
			{
				if (s[i][j]!='.')
				{
					s[i][p]=s[i][j];
					if (p!=j) s[i][j]='.';
					--p;
				}
			}
		}

		bool red = false, blue = false;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				int cnt,p,q;

				if (!red)
				{
					cnt = 0;
					p = i; q = j;
					while(q<n&&s[p][q]=='R') { ++cnt; ++q; }
					if (cnt>=k) red = true;

					cnt = 0;
					p = i; q = j;
					while(p<n&&s[p][q]=='R') { ++cnt; ++p; }
					if (cnt>=k) red = true;

					cnt = 0;
					p = i; q = j;
					while(p<n&&q<n&&s[p][q]=='R') { ++cnt; ++p; ++q; }
					if (cnt>=k) red = true;

					cnt = 0;
					p = i; q = j;
					while(p>=0&&q<n&&s[p][q]=='R') { ++cnt; --p; ++q; }
					if (cnt>=k) red = true;
				}

				if (!blue)
				{
					cnt = 0;
					p = i; q = j;
					while(q<n&&s[p][q]=='B') { ++cnt; ++q; }
					if (cnt>=k) blue = true;

					cnt = 0;
					p = i; q = j;
					while(p<n&&s[p][q]=='B') { ++cnt; ++p; }
					if (cnt>=k) blue = true;

					cnt = 0;
					p = i; q = j;
					while(p<n&&q<n&&s[p][q]=='B') { ++cnt; ++p; ++q; }
					if (cnt>=k) blue = true;

					cnt = 0;
					p = i; q = j;
					while(p>=0&&q<n&&s[p][q]=='B') { ++cnt; --p; ++q; }
					if (cnt>=k) blue = true;
				}

			}

			printf("Case #%d: %s\n",tt,red?blue?"Both":"Red":blue?"Blue":"Neither");

	}

	return 0;
}
