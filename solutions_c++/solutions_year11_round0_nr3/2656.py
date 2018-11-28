#include<stdio.h>
#include<vector>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int round=1;round <= T;round++)
	{
		int N;
		scanf("%d",&N);
		vector<int> input;
		for(int i=0;i<N;i++)
		{
			int temp;
			scanf("%d",&temp);
			input.push_back(temp);
		}
		int sumXOR = 0;
		int sum	= 0;
		int min = 99999999;
		for(int i=0;i<N;i++)
		{
			sumXOR = sumXOR^input[i];
			sum = sum + input[i];
			if(input[i] < min)
				min = input[i];
		}
		if(sumXOR == 0)
			printf("Case #%d: %d\n",round,sum - min);
		else
			printf("Case #%d: NO\n",round);
	}
	return 0;
}
