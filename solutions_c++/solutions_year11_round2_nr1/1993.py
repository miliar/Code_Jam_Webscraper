#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T;
	int N;
	int i, j, k;
	char r[200][200];
	long double RPI[200];
	long double WP[200], OWP[200], OOWP[200];
	long double win[200], lose[200], cnt[200];


	//freopen("D:\\VC2005\\google\\2011\\R2\\A\\test.txt","r",stdin);
	freopen("D:\\VC2005\\google\\2011\\R2\\A\\A-large.in","r",stdin);
	freopen("D:\\VC2005\\google\\2011\\R2\\A\\large.out","w",stdout);

	scanf("%d\n", &T);
	
	for(i=1;i<=T;i++)
	{
		scanf("%d\n", &N);
		for(j=0;j<N;j++)
		{
			scanf("%s\n", r[j]);
			WP[j] = OWP[j] = OOWP[j] =win[j] = lose[j] = cnt[j] = 0.0;
		}

		for(j=0;j<N;j++)
		{
			for(k=j+1;k<N;k++)
			{
				if(r[j][k]=='1')
				{
					cnt[j]++;
					cnt[k]++;
					win[j]++;
				}
				else if(r[j][k]=='0')
				{
					cnt[j]++;
					cnt[k]++;
					win[k]++;
				}
			}
		}

		for(j=0;j<N;j++)
		{
			int c=0;

			WP[j] = win[j]/cnt[j];
			for(k=0;k<N;k++)
			{
				if(j==k || r[j][k]=='.') continue;

				if(r[j][k]=='1') OWP[j] += win[k]/(cnt[k]-1);
				else OWP[j] += (win[k]-1)/(cnt[k]-1);
				c++;
			}
			OWP[j] =OWP[j]/c;
		}

		for(j=0;j<N;j++)
		{
			for(k=j+1;k<N;k++)
			{
				if(r[j][k]!='.')
				{
					OOWP[j] += OWP[k];
					OOWP[k] += OWP[j];
				}
			}
		}

		for(j=0;j<N;j++) OOWP[j] = OOWP[j]/cnt[j];

		printf("Case #%d:\n", i);
		for(j=0;j<N;j++) printf("%0.12f\n", WP[j]*0.25+OWP[j]*0.5+OOWP[j]*0.25);
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
