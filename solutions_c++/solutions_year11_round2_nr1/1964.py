#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

vector<int > duishou[105];
double wp1[105];
double wp2[105];
double owp[105];
double oowp[105];
int num1[105];
int num2[105];
int win1[105];
int win2[105];

char a[105][105];

int main()
{
	int cas;
	int k = 1;

	int n,i,j;
	freopen("A-largeAAA.in","r",stdin);
	freopen("A-largeAAA.out","w",stdout);
	scanf("%d",&cas);

	while(cas --)
	{
		scanf("%d",&n);

		for(i=0;i<n;i++)
		{
			scanf("%s",a[i]);

			duishou[i].clear();
		}
		memset(win1,0,sizeof(win1));
		memset(num1,0,sizeof(num1));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));

		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[i][j] != '.')
				{
					num1[i] ++;
					duishou[i].push_back(j);
				}

				if(a[i][j] == '1')

					win1[i] ++;
			}

		}
		
		for(i=0;i<n;i++)

			wp1[i] = win1[i] * 1.0 / num1[i];

		int len ;
		int ii,jj;

		for(i=0;i<n;i++)	
		{

				len = duishou[i].size();
				
				for(j=0;j<len;j++)
				{
					int temp = duishou[i][j];

					if(a[temp][i] == '1')

						owp[i] += (win1[temp] - 1 )*1.0 / (num1[temp] - 1);
					else
						owp[i] += (win1[temp]) * 1.0 /(num1[temp] - 1);
				}

				if(len > 0)
					owp[i] = owp[i] / len ;
		}
		
		for(i=0;i<n;i++)
		{
			len = duishou[i].size();

			for(j=0;j<len;j++)

				oowp[i] += owp[ duishou[i][j] ];

			oowp[i] = oowp[i] / len;
		}

		printf("Case #%d:\n",k++);

		for(i=0;i<n;i++)

			printf("%.6lf\n",0.25 * wp1[i] + 0.50 * owp[i] + 0.25 *oowp[i]);

	}

	return 0;
}

/*
2
4
.11.
0.00
01.1
.10.
*/