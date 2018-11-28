#include <cstdio>
#include <iostream>
#include <deque>
#include <queue>
#include <algorithm>

using namespace std;

struct level
{
	int value, priority, level;
};

struct compare
{
	inline bool operator() (const struct level &a, const struct level &b )
	{
		return a.value < b.value;
	}
};

struct promote
{
	inline bool operator() (const struct level &a, const struct level &b )
	{
		return a.priority < b.priority;
	}
};

int main()
{
	int N;
	
	scanf("%d\n", &N);
	for(int t = 0; t < N; t++)
	{
		int L;
		scanf("%d\n", &L);
		
		int completed[L];		
		deque<struct level> first, second;
		priority_queue<struct level, deque<struct level>, promote> third;
		first.resize(L), second.resize(L);
		
		for(int i = 0; i < L; i++)
			first[i].level = second[i].level = i, scanf("%d %d\n", &first[i].value, &second[i].value), completed[i] = 0, first[i].priority = second[i].value;
		
		sort(first.begin(), first.end(), compare());
		sort(second.begin(), second.end(), compare());
		
		int max = 0, moves = 0;
		while(!second.empty())
		{
			while(!first.empty() && first.front().value <= max)
			{
				third.push(first.front());
				first.pop_front();
			}
			
			if(!second.empty() && second.front().value <= max)
				max += completed[second.front().level] ? 1 : 2, moves++, completed[second.front().level] = 2, second.pop_front();
			else if(!third.empty())
			{
				if(!completed[third.top().level])
					max++, moves++, completed[third.top().level] = 1;
				third.pop();
			}
			else
				break;
		}
		
		if(max < 2 * L)
			printf("Case #%d: Too Bad\n", t + 1);
		else
			printf("Case #%d: %d\n", t + 1, moves);
	}
	
	return 0;
}
