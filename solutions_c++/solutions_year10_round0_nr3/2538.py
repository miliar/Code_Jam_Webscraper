/*
 * =====================================================================================
 *
 *       Filename:  b.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  05/08/2010 02:18:59 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <stdio.h>
#include <stdlib.h>
int main( )
{
	int T,R,K,N;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int q[1001];
	scanf("%d",&T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %d %d",&R,&K,&N);
		for(int i = 0; i < N; i++)
			scanf("%d",&q[i]);
		int front = 0;
		int sol = 0; 
		int ans = 0;
		while(R--)
		{
		   int 	tmp = 0;
		   int flag = 0;	
			while(1)
			{
				if(flag && front == sol)
					break;
				tmp += q[front];
				if(tmp > K)
				{
					tmp -= q[front];
					break;
				}
				if(flag == 0)
				{
					sol = front;
					flag = 1;
				}
				front++;
				if(front == N)
					front = 0;
			}
			ans += tmp;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
