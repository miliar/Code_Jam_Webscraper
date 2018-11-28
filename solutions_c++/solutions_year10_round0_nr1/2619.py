/*
 * =====================================================================================
 *
 *       Filename:  a.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  05/08/2010 01:41:00 PM
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
	int T,N,K,r;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int t = 1; t <= T; t++)
	{

		scanf("%d %d",&N,&K);
		int num [1001];
		int cnt = 0;
		while(K)
		{
		  	r = K%2;
			K = K/2;
			num[cnt++] = r;
		}
        printf("Case #%d: ",t);
		if(N<=cnt)
		{
			int flag = 0;
			for(int i = 0; i <N; i++)
				if(num[i] == 0)
				{
					flag = 1;
					break;
				}
			if(flag == 0)
			printf("ON\n");
		    else
			printf("OFF\n");
		}
		else
			printf("OFF\n");
	}
	return 0;
}
