#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t=0; t<T; t++)
	{
		//TODO: implement your algorithm here
		int last_orange_push_time = 0, last_blue_push_time = 0;
		int last_orange_push_button = 1, last_blue_push_button = 1;
		int time = 0;
				
		int N;
		scanf("%d", &N);
		for (int i=0; i<N; i++)
		{
			char c;
			int p;
			scanf(" %c", &c);
			scanf("%d", &p);
			
			if (c == 'O')
			{
				int temp_time = last_orange_push_time + abs(p - last_orange_push_button) + 1;
				time = max(temp_time, time+1);
				last_orange_push_button = p;
				last_orange_push_time = time;
			}
			else if (c == 'B')
			{
				int temp_time = last_blue_push_time + abs(p - last_blue_push_button) + 1;
				time = max(temp_time, time+1);
				last_blue_push_button = p;
				last_blue_push_time = time;
			}
		}

		printf("Case #%d: %d\n", t+1, time);
	}
}