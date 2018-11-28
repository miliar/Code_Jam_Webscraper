#include <stdio.h>

#include <queue>
#include <cmath>
#include <iostream>

using namespace std;

struct Button
{
	Button(char color, int location) : color_(color), location_(location)
	{

	}

	char color_;
	int location_;
};

void work()
{
	queue<Button> steps;
	queue<int> a_next;
	queue<int> b_next;

	int step_cnt;
	//scanf("%d", &step_cnt);
	cin >> step_cnt;

	int loc;
	char color;
	for(int i = 0;i< step_cnt;i++)
	{
		//scanf("%c%d", &color, &loc);
		cin >> color >> loc;
		steps.push(Button(color, loc));
		if(color == 'O')
		{
			a_next.push(loc);
		}
		else
		{
			b_next.push(loc);
		}
	}

	int total = 0;
	int loc_a = 1, loc_b = 1;
	while(!steps.empty())
	{
		Button button = steps.front();
		steps.pop();

		if(button.color_ == 'O')
		{
			int time = 1 + abs(loc_a - button.location_);
			total += time;

			loc_a = button.location_;
			a_next.pop();

			if(!b_next.empty() && time >= abs(loc_b - b_next.front()))
			{
				loc_b = b_next.front();
			}
			else if(!b_next.empty())
			{
				if(loc_b > b_next.front())
					loc_b -= time;
				else
					loc_b += time;
			}
		}
		else
		{
			int time = 1 + abs(loc_b - button.location_);
			total += time;

			loc_b = button.location_;
			b_next.pop();

			if(!a_next.empty() && time >= abs(loc_a - a_next.front()))
			{
				loc_a = a_next.front();
			}
			else if(!a_next.empty())
			{
				if(loc_a > a_next.front())
					loc_a -= time;
				else
					loc_a += time;
			}
		}
	}

	static int cas = 1;
	printf("Case #%d: %d\n", cas++, total);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int i = 0;i<t;i++)
	{
		work();
	}
}
