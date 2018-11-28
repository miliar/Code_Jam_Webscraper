#include<stdio.h>

#define MAX_N 1500

#define INCREASE 1
#define DECREASE 2
#define STAY 3
#define PRESS 4

char robot[MAX_N];
int but[MAX_N];
int N;
int Pushs_O[MAX_N];
int Pushs_B[MAX_N];

void read_input()
{
	scanf("%d", &N);
	Pushs_B[0] = 0;
	Pushs_O[0] = 0;
	for (int n = 0; n < N; n++)
	{
		scanf(" %c %d", robot + n, but + n);
		if (robot[n] == 'O')
		{
			Pushs_O[0]++;
			Pushs_O[Pushs_O[0]] = but[n];
		}
		else
		{
			Pushs_B[0]++;
			Pushs_B[Pushs_B[0]] = but[n];
		}
	}
	scanf("\n");
}

void show_input()
{
	printf("%d\n", N);
	for (int n = 0; n < N; n++)
		printf("%c %d\n", robot[n], but[n]);
	return;
}

int process()
{
	int time = 0;
	int curr_o = 1;
	int curr_b = 1;
	int next_step_o = 1;
	int next_step_b = 1;
	int next_step = 0;
	int action_o = STAY;
	int action_b = STAY;
	while (true)
	{
		//COMPUTE O ACTION
		if (next_step_o > Pushs_O[0])
			action_o = STAY;
		else if (Pushs_O[next_step_o] > curr_o)
			action_o = INCREASE;
		else if (Pushs_O[next_step_o] < curr_o)
			action_o = DECREASE;
		else if (Pushs_O[next_step_o] == curr_o)
			if (robot[next_step] == 'O')
				action_o = PRESS;
			else
				action_o = STAY;
		
		//COMPUTE B ACTION
		if (next_step_b > Pushs_B[0])
			action_b = STAY;
		else if (Pushs_B[next_step_b] > curr_b)
			action_b = INCREASE;
		else if (Pushs_B[next_step_b] < curr_b)
			action_b = DECREASE;
		else if (Pushs_B[next_step_b] == curr_b)
			if (robot[next_step] == 'B')
				action_b = PRESS;
			else
				action_b = STAY;
		
		if (action_o == action_b && action_o == STAY)
			return time;

		if (action_o == PRESS){ next_step_o++; next_step++; }
		if (action_b == PRESS){ next_step_b++; next_step++; }
		if (action_o == INCREASE){ curr_o++; }
		if (action_b == INCREASE){ curr_b++; }
		if (action_o == DECREASE){ curr_o--; }
		if (action_b == DECREASE){ curr_b--; }

		time++;
	}
	return time;
}

int main()
{
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; t++)
	{
		read_input();
		printf("Case #%d: %d\n", t, process());
	}
	return 0;
}
