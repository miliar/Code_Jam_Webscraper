#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <stdarg.h>
#include <string>
#include <map>
void dbg(char * fmt, ...)
{
	va_list args;
	va_start(args, fmt);
	vfprintf(stderr, fmt, args);
	va_end(fmt);
}

std::map<std::string, int> map;


class Segment
{
public:
	int start;
	int color;
	int finish;
	bool operator < (const Segment & s) const
	{
		return start < s.start;
	}
} events[700];

void solve(int test_case)
{
	int n;
	scanf("%d", &n);
	int color_count = 0;
	map.clear();
	for(int i = 0; i < n; i++)
	{
		int l,r;
		char temp[50];
		scanf("%s%d%d", &temp, &l, &r);
		std::string temp_str = temp;
		events[i].start = l-1;
		events[i].finish = r;
			
		if (map.find(temp_str) == map.end())
		{
			map.insert(make_pair(temp_str, color_count++));
		}
		events[i].color = map[temp_str];
	}
	std::sort(events, events + n);
	
	int current = 0;
	int current_last = 0;
	int next_last = 0;
	int answer = 1000;
	for(int c1 = 0; c1 < color_count; c1++)
		for(int c2 = c1; c2 < color_count; c2++)
			for(int c3 = c2; c3 < color_count; c3++)
			{
				current = 1;
				current_last = next_last = 0;
				for(int i = 0; i < n; i++)
				{
					if(events[i].color == c1 || events[i].color == c2 || events[i].color == c3)
					{
						if (events[i].start > current_last)
						{
							current ++;
							current_last = next_last;
						}
						if (events[i].start > next_last)
						{
							current = 1000;
							break;
						}
						next_last = std::max(next_last, events[i].finish);
						if (next_last == 10000)
							break;
					}
				}
				if (next_last < 10000)
					current = 1000;
				answer = std::min(answer, current);
			}
	if (answer == 1000)
	{
		printf("Case #%d: IMPOSSIBLE\n", test_case);
	}
	else
	{
		printf("Case #%d: %d\n", test_case, answer);
	}

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);
	return 0;
}
