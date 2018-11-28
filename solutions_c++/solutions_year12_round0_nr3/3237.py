/*
Author:MarsChenly
Date:2012.04.14
*/

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>

using namespace std;

bool work(int n,int m)
{
      if (n == 13 && m == 31)
      {
//            cout << 1 << endl;
      }
	int x = 1,y = 1;
	while (y <= n)
		y = y * 10;
//	y = y / 10;
	
	while (x <= n) 
	{
		x = x * 10;
		if (m == n / x + (y / x) * (n % x)) return true;
	}
	return false;
	
	
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int task;
	scanf("%d",&task);
	for (int cnt = 1; cnt <= task; cnt++)
	{
		long long ans = 0;
		int A,B;
		scanf("%d %d",&A,&B);
		for (int n = A; n < B; n++)
		for (int m = n+1; m <= B; m++)
		{
			if (work(n,m)) ans++;
		}
		
		printf("Case #%d: %lld\n",cnt,ans);
	}
	return 0;
}
