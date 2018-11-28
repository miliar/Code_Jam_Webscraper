#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 128
using namespace std;
unsigned int speed[MAX];
unsigned int lo[MAX];
int flag[MAX],flag_index;
unsigned N, K, B ,T ,i;

int maxspeed()
{
	int sum=0;
	int i;
	for (i=N-1; i>=0; --i)
	{
		if (T >= (B-lo[i]+speed[i]-1)/speed[i])
		{	
			sum++;
			flag_index++;
			flag[i] = flag_index;
		}
	}
	return sum;
}
int minspeed()
{
	int sum=0;
	int i;
	for (i=N-1; i>=0; --i)
	{
		if (T >= (B-lo[i]+speed[i]-1)/speed[i])
			sum++;
		else
			return sum;
	}
	return sum;
}
int main()
{
	freopen("B-large.in", "rt", stdin);
	freopen("large.txt", "wt", stdout);
	int nt, it,min,d;
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		memset(flag,0,sizeof(flag));
		flag_index = 0; 
		scanf("%d%d%d%d\n",&N,&K,&B,&T);
		for (i=0; i<N; ++i)
		{
			scanf("%d",&lo[i]);
		}
		for (i=0; i<N; ++i)
		{
			scanf("%d",&speed[i]);
		}
		if (maxspeed() < K){ printf("Case #%d: IMPOSSIBLE\n",it); continue;}
		min = minspeed();
		if (min >= K){ printf("Case #%d: 0\n",it); continue;}
		d = K - min;
		int index,sum=0,j;
		for (i=min+1; i<=K; ++i)
		{
			for (j=N-1; j>=0; --j)
			{
				if (flag[j] == i)
				{
					index = j;
					break;
				}
			}
			for (j=index+1; j<N; ++j)
			{
				if (flag[j] == 0)
				{	
					sum++;
				}
				else
				{					
					break;
				}
			}
			swap(flag[j-1],flag[index]);
		}
		printf("Case #%d: %d\n",it,sum);
	//	printf("Case #%d: %d\n",it,sum);
	}
	return 0;
}