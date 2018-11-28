#include <cstdio>

char s[111][111];
double wp[111], owp[111], oowp[111];

int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		int n;
		scanf("%d", &n);
		for (int j=0;j<n;j++)
			scanf("%s", s[j]);

		for (int j=0;j<n;j++)
		{
			int val=0, win=0;
			for (int hh=0;hh<n;hh++)
				if (s[j][hh]=='1')
				{
					val++;
					win++;
				}
				else if (s[j][hh]=='0')
					val++;
			wp[j]=1.0*win/val;
		}
		for (int j=0;j<n;j++)
		{
			double win1=0;
			int val1=0;
			for (int h=0;h<n;h++)
				if (s[j][h]!='.')
				{
					val1++;
					int val=0, win=0;
					for (int k=0;k<n;k++)
						if (k!=j)
						{
							if (s[h][k]=='1')
							{
								val++;
								win++;
							}
							else if (s[h][k]=='0')
								val++;
						}
					win1 += 1.0*win/val;
				}
			owp[j]=win1/val1;
		}
		for (int j=0;j<n;j++)
		{
			int val=0;
			double win=0;
			for (int h=0;h<n;h++)
				if (s[j][h]!='.')
				{
					val++;
					win+=owp[h];
				}
			oowp[j]=1.0*win/val;
		}
		printf("Case #%d:\n", i);
		for (int j=0;j<n;j++)
			printf("%.7lf\n", 0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]);
	}
	return 0;
}