#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

using namespace std;

struct wire
{
	int A;
	int B;
}wires[1005];
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n;
		int result=0;
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		{
			scanf("%d%d",&wires[j].A,&wires[j].B);
		}
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<n;k++)
			{
				if(j!=k && ((wires[j].A>wires[k].A && wires[j].B<wires[k].B)||(wires[j].A<wires[k].A && wires[j].B>wires[k].B)))
				{
					result++;
				}
			}
		}
		printf("Case #%d: %d\n",i,result/2);
	}
	return 0;
}
