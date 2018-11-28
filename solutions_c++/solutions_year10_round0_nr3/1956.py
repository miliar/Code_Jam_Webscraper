#include <iostream>
#include <string>

using namespace std;

int group[1001], max_capacity[1001], skip[1001], order[1001];

void fill_data(int i, int k, int N)
{
	int original=i, current_capacity=0;
	while(current_capacity+group[i%N]<=k)
	{
		current_capacity+=group[i%N], i+=1;
		if(original==i%N)
			break;
	}
	max_capacity[original]=current_capacity;
	skip[original]=i-original;
}

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int i=1; i<=T; i++)
	{
		fill(group, group+1001, 0);
		fill(max_capacity, max_capacity+1001, 0);
		fill(skip, skip+1001, 0);
		fill(order, order+1001, 0);

		int R, k, N;
		scanf("%d%d%d", &R, &k, &N);
		for(int j=0; j<N; j++)
		{
			int people;
			scanf("%d", &people);
			group[j]=people;
		}

		for(int j=0; j<N; j++)
			fill_data(j, k, N);

		for(int j=1; j<=N; j++)
			order[j]=(order[j-1]+skip[order[j-1]])%N;
		
		int repeat, original, length;
		bool found=false;
		for(int j=0; j<N && !found; j++)
			for(int k=j+1; k<=N; k++)
				if(order[j]==order[k])
				{
					original=j;
					repeat=k;
					found=true;
					break;
				}
		length=repeat-original;

		long long profit=0;
		if(repeat+1>R)
			for(int j=0; j<R; j++)
				profit+=max_capacity[order[j]];
		else
		{
			long long first_cycle_profit=0, repeat_cycle_profit=0;
			for(int j=0; j<repeat; j++)
				first_cycle_profit+=max_capacity[order[j]];
			R-=repeat;
			for(int j=original; j<repeat; j++)
				repeat_cycle_profit+=max_capacity[order[j]];
			profit=first_cycle_profit+R/length*repeat_cycle_profit;
			R%=length;
			for(int j=0; j<R; j++)
				profit+=max_capacity[order[original+j]];
		}
		printf("Case #%d: ", i);
		cout << profit << endl;
	}
	return 0;
}