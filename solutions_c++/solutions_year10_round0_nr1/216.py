/* 
 * Problem: IOI2007 sail
 * Author: BYVoid (郭家寶 Guo Jiabao)
 * Time: 2009.7.21 9:12
 * State: Unsolved
 * Memo: 贪心
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

int main()
{
	int T,N,K;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",i);
		int p = 1;
		for (int j=1;j<=N;j++)
			p *= 2;
		if (K % p == (p-1))
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
