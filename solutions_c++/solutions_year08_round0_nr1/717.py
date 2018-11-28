#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
string a[105],sq[105];
#define MAX 100000
int lens ,dp[10005][10005];
int main()
{
	int test,z,num,i,j,qnum;
	char g[10005];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&test);
	for(z = 1; z <= test; z ++)
	{
		scanf("%d",&lens);
		getchar();
		for(i = 1 ;i <= lens ;i ++)
		{
			gets(g);
			a[i] = "";
			for(j = 0 ;j < strlen(g) ;j ++)
				a[i]+= g[j];
		}
		scanf("%d",&qnum);
		getchar();
		for(i = 1 ;i <= qnum; i ++)
		{
			gets(g);
			sq[i] = "";
			for(j = 0 ;j < strlen(g) ;j ++)
			{
				sq[i]+= g[j];
			}
		}
		int s,q,later;/// string ,when you have  dp[1000][1000],it will goes wrong
		for(q =  0; q <= qnum; q ++)
			for(s = 0 ;s <= lens;s ++)
			{
				dp[q][s] = MAX; 
			}
		
		for(s = 1;s <=lens; s ++)
		{
			if(sq[1] == a[s])
				continue;
			else
				dp[1][s] = 0;
		}
		for(q = 2; q <= qnum; q ++)
			for(s = 1;s <= lens; s ++)
			{
				if(sq[q] == a[s])
					continue;
				for(later= 1 ;later  <= lens; later ++)
				{
					if(dp[q -1][later] != MAX)
					{
						 if(later == s)
						 {
							if(dp[q -1][later] < dp[q][s])
								dp[q][s] = dp[q -1][later];
						 }
						 else
						 {
							 if(dp[q -1 ][later] + 1 < dp[q][s])
							 dp[q][s] = dp[q - 1][later]  + 1; 
						 }
					}
				}
			}
		int min1 = MAX;
		if(qnum == 0)
			min1 = 0;
		else
		{
			for(s =1 ; s <= lens; s ++)
				if(min1 > dp[qnum ][s])
					min1 = dp[qnum ][s];
		}
		printf("Case #%d: %d\n",z,min1);
	}
	return 0;
}

