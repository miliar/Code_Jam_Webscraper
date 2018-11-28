#include<iostream>
#include<cstdio>
using namespace std;
int times,a1,a2,b1,b2,re;
void mem()
{
//	for (int a=1;a<=)
}
bool check(int x,int y)
{
	if (x>y)
	{
		int t=x;
		x=y;
		y=t;
	}
	if (x==y) return 0;
	if (!x) return 1;
	if (y%x==0) return 1;
	if (check(x,y%x)==0)
	{
		return 1;
	}else
	{
		if (y/x==1) return 0;else return 1;
	}
	/*for (int a=1;a<=y/x;++a)
	{
		if (check(x,y-a*x)==0) return 1;
	}*/
	return 0;
}
int main()
{
//	mem();
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&times);
	for (int z=1;z<=times;++z)
	{
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		re=0;
		for (int a=a1;a<=a2;++a)
		for (int b=b1;b<=b2;++b)
		{
			if (check(a,b))
			{
				re++;
		//		printf("[%d %d]",a,b);
			}
			
		}
		printf("Case #%d: ",z);
		printf("%d\n",re);
	}
}
