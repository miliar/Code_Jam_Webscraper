#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
char box[505][505];
int r,c,d;
int main()
{
	int t;	freopen("B-small-attempt7.in","r",stdin);	freopen("B-small-attempt7.out","w",stdout);
	int g = 1;
	scanf("%d",&t);
	int i,j,k,l,m;
	while(t--)
	{
		int ans = 0;
		scanf("%d%d%d",&r,&c,&d);
		for( i = 0 ; i < r; i ++)
			scanf("%s",box[i]);
		for( i = 0 ; i < r ; i ++)
		{
			for(j = 0 ; j < c ; j ++)
			{
				for( k = 2 ; k + i < r && k  + j < c ; k ++)
				{
					double sum1 = 0 , sum2 = 0;
					double midx = (2 * i + k) * 0.5;
					double midy = (2 * j + k) * 0.5;
					for( l = i  ; l <= i + k ; l ++)
					{
						for( m = j  ; m <= j + k ; m ++)
						{
							if( (l == i || l == i +k)&& (m == j || m == j+k))
								continue;
							sum1 += (box[l][m]-'0') * (l - midx);
							sum2 += (box[l][m]-'0') * (m - midy);
						}
					}
					if(fabs(sum1) <= 1e-8 && fabs(sum2) <= 1e-8)
					{
						ans = ans > k ? ans : k;
					}
				}
			}
		}
		printf("Case #%d: ",g++);
		if(ans == 0)
			printf("IMPOSSIBLE\n");
		else
		printf("%d\n",ans+1);
	}
	return 0;
}
/*
2
5 6 2

122271
211521
329131
242121
122211
Case #1: 5
*/