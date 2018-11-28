#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 128;

char m[MAXN][MAXN];
int N;

double rpi[MAXN][4];

double wp(int team,int exclude)
{
	int sum = 0;
	int cnt = 0;

	for(int j=1;j<=N;j++)
	{
		if(j == exclude)
			continue;
		if(m[team][j] == '1')
			sum++;
		if(m[team][j] != '.')
			cnt++;
	}

	return double(sum) / double(cnt);
}

void calc_RPI()
{
	for(int i=1;i<=N;i++)
	{
		rpi[i][0] = wp(i,-1);
	}


	for(int i=1;i<=N;i++)
	{
		double sum = 0;
		int cnt = 0;

		for(int j=1;j<=N;j++)
		{
			if(m[i][j] != '.')
			{
				sum += wp(j,i);
				cnt++;
			}
		}

		rpi[i][1] = sum / double(cnt);
	}

	for(int i=1;i<=N;i++)
	{
		double sum=0;
		int cnt=0;
		for(int j=1;j<=N;j++)
		{
			if(m[i][j]!='.')
			{
				sum += rpi[j][1];
				cnt++;
			}
		}
		rpi[i][2] = sum / (double)(cnt);
	}
	
}

void display_RPI()
{
	for(int i=1;i<=N;i++)
	{
		printf("%.14lf\n",(0.25 * rpi[i][0] + 0.5 * rpi[i][1] + 0.25 * rpi[i][2]));
	}
}

int main()
{
	int T;
	scanf("%d",&T);

	for(int t=1;t<=T;t++)
	{
		memset(m,0,sizeof(m));
		scanf("%d",&N);

		for(int i=1;i<=N;i++)
		{
			scanf("%s",m[i] + 1);
		}


		calc_RPI();

		printf("Case #%d:\n",t);
		display_RPI();
	}
}