// Author : Muhammad Rifayat Samee
// Problem : B
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>

#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;

double N[10005];

double l,t;
int n,c;
int main()
{
	freopen("b_s.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cases,i,j,k,ct=1;
	double res,r,temp,p;
	scanf("%d",&cases);

	while(cases--)
	{
		scanf("%lf %lf %d %d",&l,&t,&n,&c);

		for(i=0;i<c;i++)
		{
			scanf("%lf",&N[i]);
		}
		k = 0;
		for(i=c;i<n;i++)
		{
			N[i] = N[k];
			k = k + 1;
			if(k==c)
				k = 0;
		}
		
		res = 0;
		//for(i=0;i<n;i++)
		//	printf(" %lf",N[i]);
		//printf("\n");

		if(l == 0)
		{
			for(i=0;i<n;i++)
			{
				res = res + N[i]/0.5;
			}

		}
		else if(l==1)
		{
			res = INF;
			for(i=0;i<n;i++)
			{
				
				r = 0;
				for(j=0;j<n;j++)
				{
					if(j!=i)
					{
						r = r + N[j]/0.5;
					}
					else
					{
						if(r+eps>=t)
						{
							r = r + N[j];
						}
						else
						{
							if(res+(N[j]/0.5)+eps>t)
							{
								temp = t - r;

								r = r + temp;
								p = N[j] - ((0.5)*temp);
								r = r + p ;
							}

						}
					}
						
				}
				if(res>r+eps)
							res = r;
				
				
			}
			
		}
		else
		{
			res = INF;
			for(i=0;i<n;i++)
			{
				for(k=0;k<n;k++)
				{
					if(i!=k)
					{
						
						r = 0;
						for(j=0;j<n;j++)
						{
							if(j!=i && j!=k)
							{
								r = r + N[j]/0.5;
							}
							else
							{
								if(r+eps>=t)
								{
									r = r + N[j];
								}
								else
								{
									if(res+(N[j]/0.5)+eps>t)
									{
										temp = t - r;

										r = r + temp;
										p = N[j] - ((0.5)*temp);
										r = r + p ;
									}

								}
							}

							
						}
						if(res>r+eps)
								res = r;
					}
				}

			}
		}

		printf("Case #%d: %.0lf\n",ct++,res);

		
	}
	return 0;


}
