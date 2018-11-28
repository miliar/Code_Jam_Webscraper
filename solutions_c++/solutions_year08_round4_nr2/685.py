#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;


int test_num,n,m,a;


void out(int res)
{
	printf("Case #%d: %d",test_num,res);
}


void inp()
{
	scanf("%d%d%d",&n,&m,&a);
}


void run()
{
	for(int x1=0; x1<=n; x1++)
	{
		for(int y1=0; y1<=m; y1++)
		{
			for(int x2=0; x2<=n; x2++)
			{
				for(int y2=0; y2<=m; y2++)
				{
					if(abs(x1*y2-x2*y1)==a)
					{
						printf("Case #%d: %d %d %d %d %d %d\n",test_num,0,0,x1,y1,x2,y2);
						return;
					}
				}
			}
		}
	}
	printf("Case #%d: IMPOSSIBLE\n",test_num);
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test_count;
	scanf("%d",&test_count);
	for(test_num=1; test_num<=test_count; test_num++)
	{
		inp();
		run();
	}
	return 0;
}