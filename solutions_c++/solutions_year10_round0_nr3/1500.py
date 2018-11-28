#include <cstdio>
#include <iostream>
using namespace std;

#define MAX 1000

int T;

int rides,capacity,num_groups;
long long groups[MAX];

int next[MAX];
long long income[MAX];

int get_cycle_start(int loc)
{
	int i = loc;
	long long sum = 0;
	while(sum + groups[i] <= capacity)
	{
		sum += groups[i];
		i++;
		if(i == num_groups)
			i = 0;
		if(i == loc)
			break;
	}
	income[loc] = sum;
	next[loc] = i;
	if(next[i] == -1)
		return get_cycle_start(i);
	else
		return i;
}

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %d %d", &rides, &capacity, &num_groups);
		for(int i = 0; i < num_groups; i++)
		{
			scanf("%d", &groups[i]);
			next[i] = -1;
		}
		int cycle_start = get_cycle_start(0);
		long long cycle_income = income[cycle_start];
		int cycle_length = 1;
		int loc = next[cycle_start];
		while(loc != cycle_start)
		{
			cycle_income += income[loc];
			loc = next[loc];
			cycle_length++;
		}
		
		
		long long result = 0;
		loc = 0;
		while(rides > 0 && loc != cycle_start)
		{
			result += income[loc];
			loc = next[loc];
			rides--;
		}
		long long cycles = rides / cycle_length;
		rides = rides%cycle_length;
		result += cycles*cycle_income;
		while(rides > 0)
		{
			result += income[loc];
			loc = next[loc];
			rides--;
		}
		cout << "Case #" << t << ": " << result << endl;
	}
	return 0;
}
