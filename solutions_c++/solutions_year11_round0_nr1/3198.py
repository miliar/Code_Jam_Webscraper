// Author : Muhammad Rifayat Samee
// Problem : A
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
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif




using namespace std;

struct sqe
{
	char w;
	int num;
	int f;

}S[105];
int n;

int main()
{
	//freopen("A.in","r",stdin);
	//freopen("a_large.txt","w",stdout);
	int cases,i,j,k,num,t,o,b,tt,ct=1;
	char str[15];


	scanf("%d",&cases);

	while(cases--)
	{
		scanf("%d",&n);

		for(i=0;i<n;i++)
		{
			scanf("%s %d",str,&num);

			S[i].w = str[0];
			S[i].num = num;
			S[i].f = 0;

		}
		
		o = 1;
		b = 1;
		t = 0;
		
		for(i=0;i<n;i++)
		{
			if(S[i].w == 'O')
			{
				tt = 0;
				if(o==S[i].num)
				{
					t = t + 1;
					tt = tt + 1;
					S[i].f = 1;

				}
				else
				{
					t = t + abs(S[i].num - o) + 1;
					tt = abs(S[i].num - o) + 1;
					o = S[i].num;
				}

				for(j=i+1;j<n;j++)
					if(S[j].w == 'B')
						break;
					if(j!=n)
					{
						if(abs(S[j].num - b) <=tt)
						{
							b = S[j].num;
	
						}
						else
						{
							if(S[j].num<b)
								b = b - tt;
							else
								b = b + tt;
						}
					}
			}

			else if(S[i].w == 'B')
			{
				tt = 0;
				if(b==S[i].num)
				{
					t = t + 1;
					tt = tt + 1;
					S[i].f = 1;

				}
				else
				{
					t = t + abs(S[i].num - b) + 1;
					tt = abs(S[i].num - b) + 1;
					b = S[i].num;
				}

				for(j=i+1;j<n;j++)
					if(S[j].w == 'O')
						break;

					if(j!=n)
					{
						if(abs(S[j].num - o) <=tt)
						{
							o = S[j].num;
	
						}
						else
						{
							if(S[j].num<o)
								o = o - tt;
							else
								o = o + tt;
						}
					}
			}


		}

		printf("Case #%d: %d\n",ct++,t);



		

	}
	return 0;


}