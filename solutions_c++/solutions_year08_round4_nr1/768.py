#include "iostream"
#include <stdlib.h>
#include <math.h>
#include <vector>

#define MAX 100000

using namespace std;



int main()
{
	int N;
	scanf("%d\n",&N);
	for (int c = 0; c < N; c++)
	{
		int M,V;
	
		scanf("%d %d\n",&M,&V);
		vector<int> nodes;
		vector<int> change;
		vector<int> Zero;
		vector<int> One;
		for (int i = 0; i < M; i++)
		{
			One.push_back(MAX);
			Zero.push_back(MAX);
		}
		for (int i = 0; i < (M-1)/2; i++)
		{
			int a,b;
			scanf("%d %d\n",&a,&b);
			nodes.push_back(a);
			change.push_back(b);
		}
		for (int i = (M-1)/2; i < M; i++)
		{
			int a;
			scanf("%d\n",&a);
			nodes.push_back(a);
		}
		for (int i = M-1; i>= 0; i--)
		{
			if (i >= (M-1)/2)
			{
				if (nodes[i] == 1)
					One[i] = 0;
				else
					Zero[i] = 0;
				continue;
			}
			int q = 0;
			int w = 2*(i+1)-1;
			int e = 2*(i+1);
			if (nodes[i] == 0)
			{
				Zero[i] = min(Zero[i],(Zero[w]+Zero[e]));
				One[i] = min(One[i],(Zero[w]+One[e]));
				One[i] = min(One[i],(Zero[e]+One[w]));
				One[i] = min(One[i],(One[w]+One[e]));
			}
			if (nodes[i] == 1)
			{
				Zero[i] = min(Zero[i],(Zero[w]+Zero[e]));
				Zero[i] = min(Zero[i],(Zero[w]+One[e]));
				Zero[i] = min(Zero[i],(Zero[e]+One[w]));
				One[i] = min(One[i],(One[w]+One[e]));
			}
			if (change[i] == 1)
			{
				if (nodes[i] == 1)
				{
					Zero[i] = min(Zero[i],(Zero[w]+Zero[e])+1);
					One[i] = min(One[i],(Zero[w]+One[e])+1);
					One[i] = min(One[i],(Zero[e]+One[w])+1);
					One[i] = min(One[i],(One[w]+One[e])+1);
				}
				if (nodes[i] == 0)
				{
					Zero[i] = min(Zero[i],(Zero[w]+Zero[e])+1);
					Zero[i] = min(Zero[i],(Zero[w]+One[e])+1);
					Zero[i] = min(Zero[i],(Zero[e]+One[w])+1);
					One[i] = min(One[i],(One[w]+One[e])+1);
				}
			}

		}
		printf("Case #%d: ",c+1);
		if (V == 0)
		{
			if (Zero[0] < MAX)
				printf("%d\n",Zero[0]);
			else
				printf("IMPOSSIBLE\n");
		}
		else
		{
			if (One[0] < MAX)
				printf("%d\n",One[0]);
			else
				printf("IMPOSSIBLE\n");
		}

	}
	return 0;
}
