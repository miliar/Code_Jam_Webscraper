#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <math.h>

#define N 105
#define P 105
#define T 105
using namespace std;

char robots[N];
int buttons[N];
char total[2*N];

int main()
{
	freopen("A-large.in", "r" ,stdin);
	FILE* f = fopen("a-large.out","w");

	int t,n;
 	cin >> t;
	for(int i=0;i<t;i++)
	{
		cin>>n;

		for(int j=0;j<n;j++)
			cin >> robots[j] >> buttons[j];
		
		// if only one step
		if(n==1)
		{
			printf("Case #%d: %ld\n", i+1, buttons[0]);
			fprintf(f, "Case #%d: %ld\n", i+1, buttons[0] );
			continue;
		}

		// Calculate
		int prev_B = 1,prev_O = 1;
		int elaps_B=0, elaps_O=0;

		char curr_robot; char prev_robot;

		long long time=buttons[0];
		if(robots[0]=='O')
		{
			elaps_B = buttons[0];
			prev_O=buttons[0];
		}
		else
		{
			elaps_O = buttons[0];
			prev_B = buttons[0];
		}

		for(int j=1;j<n;j++)
		{
			curr_robot = robots[j];
			prev_robot = robots[j-1];
			if(curr_robot == prev_robot)
			{
				if(curr_robot == 'O')
				{
					int delta = abs(buttons[j]-prev_O)+1;	// time needed to finish this step
					time+=delta;
					elaps_B+=delta;
					prev_O = buttons[j];
				}
				else
				{
					int delta = abs(buttons[j]-prev_B)+1;
					time+=delta;
					elaps_O+=delta;
					prev_B = buttons[j];
				}
			}
			else
			{
				if(curr_robot == 'O')
				{
					int delta = abs(buttons[j]-prev_O);
					if(delta <= elaps_O)
					{
						// already there, just push button
						time++;
						elaps_B++;
					}
					else
					{
						time += delta-elaps_O + 1;
						elaps_B += delta-elaps_O +1;
					}
					prev_O=buttons[j];
					elaps_O=0;
				}
				else
				{
					int delta=abs(buttons[j]-prev_B);
					if(delta <= elaps_B)
					{
						time++;
						elaps_O++;
					}
					else
					{
						time += delta-elaps_B + 1;
						elaps_O= delta -elaps_B + 1;
					}
					prev_B=buttons[j];
					elaps_B=0;
				}
			}
		}

		// print result;
		printf("Case #%d: %ld\n", i+1, time);
		fprintf(f, "Case #%d: %ld\n", i+1, time);
	}
	return 0;
}