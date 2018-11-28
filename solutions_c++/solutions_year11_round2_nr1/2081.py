#include <stdio.h>
#include <string.h>

char tb[102][102];
double wp[102];
double owp[102];
double oowp[102];
int N;

void CalcWp()
{
	for (int i=1; i<=N; i++)
	{
		double cnt=0,win = 0;
		for (int j=1; j<=N; j++)
		{
			if (tb[i][j]!='.')
			{
				cnt++;
				if (tb[i][j] == '1')
				{
					win++;
				}
			}
		}
		wp[i] = win/cnt;
	}
}


double CalcWpK(int k,int b)
{
	double cnt=0,win=0;
	for (int i=1; i<=N; i++)
	{	
		if (tb[b][i]!='.' && i!=k)
		{
			cnt++;
			if (tb[b][i]=='1')
			{
				win ++;
			}
		}
	}
	return win/cnt;
}

void CalcOwp()
{
	
	for (int i=1; i<=N; i++)
	{
		double totowp = 0;
		int cnt = 0;
		for (int j=1; j<=N; j++)
		{
			if (tb[i][j]!='.')
			{
				cnt++;
				totowp += CalcWpK(i,j);
			}
			
		}
		owp[i] = totowp/cnt;
	}
}

void CalcOowp()
{
	for (int i=1;i<=N;i++)
	{
		double totoowp = 0;
		int cnt = 0;
		
		for (int j=1;j<=N;j++)
		{
			if (i==j || tb[i][j]=='.')
			{
				continue;
			}
			cnt++;
			totoowp += owp[j];
		}
		oowp[i] = totoowp/cnt;
	}
}

void Solve()
{
	CalcWp();
	CalcOwp();
	CalcOowp();
	for (int i=1; i<=N; i++)
	{
		double rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
		printf("%.12lf\n",rpi);
	}
}


int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int ncase;
	scanf("%d",&ncase);
	for (int c=1; c<=ncase; c++)
	{
		printf("Case #%d:\n",c);
		memset(tb,0,sizeof(tb));
		scanf("%d\n",&N);
		for (int i=1; i<=N; i++)
		{
			scanf("%s",tb[i]+1);
		}
		Solve();
	}
	return 0;
}