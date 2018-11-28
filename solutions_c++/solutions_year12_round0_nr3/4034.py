#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

int caldit(int x)
{
	int s = 0;
	while(x)
	{
		s++;
		x /= 10;
	}
	return s;
}
int main()
{
	int T;
	int a,b,m,n;
	int vis[10];
	scanf("%d",&T);
	for(int k = 1;k <= T;++k)
	{
		scanf("%d%d",&a,&b);
		printf("Case #%d: ",k);
		int sum = 0,t = caldit(a),r;
		int p = (int)pow(10.0,t - 1);
		for(int i = a; i <= b;++i)
		{
			r = i; int v = 0;
			vis[v++] = i;
			for(int j = 1;j < t;++j)
			{
				int h = r / p,num = 0;
				num = (r - h * p) * 10 + h;
				if(num > i && num <= b) sum++;
				r = num;
				bool flag = false;
				for(int c = 0;c < v;++c)
					if(vis[c] == r) flag = true;
				if(flag) break;
				vis[v++] = r;
			}
		}
		printf("%d\n",sum);
	}
	return 0;
}