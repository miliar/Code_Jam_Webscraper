#include <cstdio>
#include <iostream>
#include <deque>
#include <queue>
#include <algorithm>

using namespace std;

struct level
{
	int index, length, death;
};

struct level_sort
{
	inline bool operator() (const struct level &a, const struct level &b)
	{
		return a.length * a.death * (100 - b.death) > b.length * b.death * (100 - a.death);
		//return a.death > b.death || (a.death ==  b.death && a.length > b.length);
	}
};


int main()
{
	int N;
	
	scanf("%d\n", &N);
	for(int t = 0; t < N; t++)
	{
		int T;
		scanf("%d\n", &T);
		
		struct level levels[T];
		for(int i = 0; i < T; i++)
			levels[i].index = i, scanf("%d ", &levels[i].length);
		for(int i = 0; i < T; i++)
			scanf("%d ", &levels[i].death);
		
		stable_sort(levels, levels + T, level_sort());
		
		//sort(levels, levels + T, level_sort());
		
		printf("Case #%d: ", t + 1);
		for(int i = 0; i < T; i++)
			printf("%d ", levels[i].index);
		puts("");
	}
	
	return 0;
}
