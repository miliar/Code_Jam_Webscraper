#include<iostream>
#include<cstdio>
#define Max 105

using namespace std;

char map[Max][Max];

double wp[Max], owp[Max], oowp[Max];
int p[Max];

int main()
{
	int z, zi, i, j, n, t;
	double tb;

	scanf("%d", &z);

	for(zi=1;zi<=z;zi++)
	{
		scanf("%d", &n);

		for(i=0;i<n;i++)
			scanf(" %s", map[i]);

		for(i=0;i<n;i++)
		{
			t = 0;
			tb = 0.0;
			for(j=0;j<n;j++)
			{
				if(map[i][j] != '.')
					t++;

				if(map[i][j] == '1')
					tb += 1;
			}
			wp[i] = tb/t;
			p[i] = t;
		}

		for(i=0;i<n;i++)
		{
			t = 0;
			tb = 0.0;
			for(j=0;j<n;j++)
			{
				if(map[i][j] != '.')
				{
					t++;
					tb += (wp[j] * p[j] - (map[i][j]=='0')) / (p[j] - 1);
				}
			}
			owp[i] = tb/t;
		}

		for(i=0;i<n;i++)
		{
			t = 0;
			tb = 0.0;
			for(j=0;j<n;j++)
			{
				if(map[i][j] != '.')
				{
					t++;
					tb += owp[j];
				}
			}
			oowp[i] = tb/t;
		}

		printf("Case #%d:\n", zi);
		for(i=0;i<n;i++)
		{
			//cout<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<"\n";
			printf("%.7lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
	}
}
