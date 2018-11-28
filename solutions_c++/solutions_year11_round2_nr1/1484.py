#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <sstream>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define INF 2000000000
#define EPS 1e-11
#define MAX_N 100002
using namespace std;

#ifdef _WIN32 
typedef __int64 int64; 
#else 
typedef long long int64; 
#endif 

typedef pair <int,int> ii;

int
main()
{
	int T,N,sum[105];
	char score[105][105];
	double WP[105], OWP[105], OOWP[105], RIP[105];;
	scanf("%d", &T);
	for(int i = 1;i <= T;i++)
	{
		scanf("%d", &N);
		for(int j = 0;j < N;j++)
		{
			scanf("%s",score[j]);
		}
		for(int j = 0;j < N;j++)
		{
			// WP
			WP[j] = 0;
			sum[j] = 0;
			for(int k = 0;k < N;k++)
			{
				if(score[j][k] == '1')
				{
					sum[j]++;
					WP[j]++;
				}
				else if(score[j][k] == '0')
				{
					sum[j]++;
				}
			}
			WP[j] = WP[j]/sum[j];
		}
		for(int j=0;j < N;j++)
		{
			//OWP
			OWP[j] = 0;
			for(int k = 0;k < N;k++)
			{
				if(score[j][k] == '1' || score[j][k] == '0')
				{
					if(score[k][j] == '0')
					{
						OWP[j] =  OWP[j] + ((WP[k]*sum[k])/(sum[k]-1));
					}
					else
					{
						OWP[j] =  OWP[j] + (((WP[k]*sum[k])-1)/(sum[k]-1));
					}
				}
			}
			OWP[j] = OWP[j] / sum[j];
		}
		printf("Case #%d:\n",i);
		for(int j = 0;j < N;j++)
		{
			OOWP[j] = 0;
			for(int k =0;k < N;k++)
			{
				if(score[j][k] == '1' || score[j][k] == '0')
				{
					OOWP[j] = OOWP[j] + OWP[k];
				}
			}
			OOWP[j] = OOWP[j] / sum[j];
			RIP[j] = (0.25 * WP[j]) + (0.5 * OWP[j]) + (0.25 * OOWP[j]);
			printf("%f\n", RIP[j]);
		}
	}
return 0;
}
