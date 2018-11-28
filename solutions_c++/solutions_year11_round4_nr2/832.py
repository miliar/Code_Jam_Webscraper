#include <iostream>
#include <fstream>
using namespace std;

const long maxn = 15;
int W[maxn][maxn];
char str[maxn];
inline int min(int a,int b)
{
	return a>b?b:a;
}
inline int max(int a,int b)
{
	return a>b?a:b;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	int i,j,k;
	int ii,jj;
	int T,R,C,D;
	int cas = 0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d",&R,&C,&D);
		for(i=1;i<=R;i++)
		{
			cin>>str;
			for(j=0;j<C;j++)
			{
				W[i][j+1] = (str[j] - '0') + D;
			}
		}

		int ans = -1;
		int lv = -1;
		for(i=2;i<R;i++)
		{
			for(j=2;j<C;j++)
			{
				int minR = min(i-1,R-i);
				int minC = min(j-1,C-j);
				int minall = min(minR,minC);

				// 奇数的时候
				for(k=max(1,lv);k<=minall;k++)
				{
					int XX=0,YY=0;
					for(ii=i-k;ii<=i+k;ii++)
					{
						for(jj=j-k;jj<=j+k;jj++)
						{
							if((ii==i-k && jj==j-k) || (ii==i-k && jj==j+k) 
								|| (ii==i+k && jj==j-k) || (ii==i+k && jj==j+k))
							{
								continue;
							}
							XX += (ii-i) * W[ii][jj];
							YY += (jj-j) * W[ii][jj];
						}
					}

					if(0 == XX && 0 == YY)
					{
						if(k > lv)
						{
							lv = k;
						}
					}
				}
				
				//偶数的时候
				
			}
		}

		if(lv * 2 + 1 > ans)
			ans = lv * 2 + 1;

		
		for(i=2;i<R-1;i++)
		{
			for(j=2;j<C-1;j++)
			{
				int minR = min(i,R-i);
				int minC = min(j,C-j);
				int minall = min(minR,minC);
				
				for(k=max(2,lv);k<=minall;k++)
				{
					double XX=0.0,YY=0.0;
					for(ii=i-k+1;ii<=i+k;ii++)
					{
						for(jj=j-k+1;jj<=j+k;jj++)
						{
							if((ii==i-k+1 && jj==j-k+1) || (ii==i-k+1 && jj==j+k) 
								|| (ii==i+k && jj==j-k+1) || (ii==i+k && jj==j+k))
							{
								continue;
							}

							double numi = ii - i;					
							numi -= 0.5;
							XX += numi * W[ii][jj];

							double numj = jj - j;						
							numj -= 0.5;
							YY += numj * W[ii][jj];
						}
					}

					if(0.0 == XX && 0.0 == YY)
						if(lv < k)
							lv = k;
				}
			}
		}
		if(lv * 2 > ans)
			ans = lv * 2;

		printf("Case #%d: ",++cas);
		if(-1 == lv)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}