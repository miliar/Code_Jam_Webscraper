#include <cstdio>
#include <cstring>

int n;
long long A,B,C,D,x0,y0,M;

int data[3][3];

void generate(void)
{
	long long X = x0, Y = y0;
	data[X%3][Y%3] += 1;
	for (int i = 1;i<=n-1;i++)
	{
		X = (A * X + B) % M;
  		Y = (C * Y + D) % M;
  		data[X%3][Y%3] += 1;
  	}
}

void inp(void)
{
	scanf("%d%lld%lld%lld%lld%lld%lld%lld",&n, &A, &B, &C, &D, &x0, &y0, &M);
}

long long solve(void)
{
	long long res = 0;
	for (int x1=0;x1<3;x1++)
		for (int y1=0;y1<3;y1++)
			for (int x2=0;x2<3;x2++)
				for (int y2=0;y2<3;y2++)
					for (int x3=0;x3<3;x3++)
						for (int y3=0;y3<3;y3++)
							if ((x1+x2+x3)%3==0 && (y1+y2+y3)%3==0)
							{
								if (x1==x2 && x2==x3 && y1==y2 && y2==y3)
								{
									res+=((long long)data[x1][y1])*((long long)data[x1][y1]-1)*((long long)data[x1][y1]-2);
									continue;
								}
								if ((x1==x2 && y1==y2))
								{
									res+=((long long)data[x1][y1])*((long long)data[x1][y1]-1)*((long long)data[x3][y3]);
									continue;
								}
								if (x1==x3 && y1==y3)
								{
									res+=((long long)data[x1][y1])*((long long)data[x1][y1]-1)*((long long)data[x2][y2]);
									continue;
								}
								if (x2==x3 && y2==y3)
								{
									res+=((long long)data[x2][y2])*((long long)data[x2][y2]-1)*((long long)data[x1][y1]);
									continue;
								}
								res+=((long long)data[x1][y1])*((long long)data[x2][y2])*((long long)data[x3][y3]);
							}
	return res/6;
}

int main(void)
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		memset(data,0,sizeof(data));
		inp();
		generate();
		printf("Case #%d: %lld\n",i,solve());
	}
	return 0;
}

