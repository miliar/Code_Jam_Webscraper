#include <iostream>
using namespace std;
const int SIZE = 1024;

struct SEG
{
	int a,b;
}seg[SIZE];

bool cross(const SEG &a, const SEG &b)
{
	if ((a.a < b.a && a.b > b.b) || (a.a > b.a && a.b < b.b))
		return true;
	return false;
}

int main()
{
	freopen("A-large2.in","r",stdin);
	freopen("large.txt","w",stdout);
	int cases,cas = 1;
	scanf("%d",&cases);
	int n,i,j;
	while(cases --)
	{
		scanf("%d",&n);
		for (i = 0; i < n; i++)
		{
			scanf("%d %d",&seg[i].a,&seg[i].b);
		}
		__int64 sum = 0;
		for (i = 0; i < n; i++)
		{
			for (j = i+1; j < n; j++)
			{
				if (cross(seg[i],seg[j]))
					sum ++;
			}
		}
		printf("Case #%d: %I64d\n",cas++,sum);
	}
	return 0;
}