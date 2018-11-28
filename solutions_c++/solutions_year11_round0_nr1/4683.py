#include <stdio.h>
#include <math.h>

int T;
int N;

int Aout[100];

char robot[100];
int button[100];


int search()
{
	int i;
	int k;
	int current_o = 1;
	int current_b = 1;
	int next_o;
	int next_b;
	int direct_o;
	int direct_b;
	int timestamp;
	int totaltime = 0;

	for(i=0;i<N;i++) {

		for(k=i;k<N;k++) {
			if(robot[k] == 'O') {
				next_o = button[k];
				break;
			}
		}

		for(k=i;k<N;k++) {
			if(robot[k] == 'B') {
				next_b = button[k];
				break;
			}
		}

		if(robot[i] == 'O') {

			timestamp = abs(next_o - current_o) + 1;

			current_o = next_o;

			direct_b = next_b>=current_b;

			current_b = current_b + (direct_b?timestamp:(-timestamp));
			current_b = (                  direct_b?(current_b>next_b):(current_b<next_b)       )?next_b:current_b;

			totaltime += timestamp;
		}
		else if(robot[i] == 'B') {

			timestamp = abs(next_b - current_b) + 1;

			current_b = next_b;

			direct_o = next_o>=current_o;

			current_o = current_o + (direct_o?timestamp:(-timestamp));
			current_o = (                  direct_o?(current_o>next_o):(current_o<next_o)       )?next_o:current_o;

			totaltime += timestamp;
		}

	}

	return totaltime;
}

void main()
{
	int i;
	int k;
	char ch;
	int bt;

	scanf("%d",&T);

	for(i=0;i<T;i++) {

		scanf("%d", &N);

		for(k=0;k<N;k++) {

			scanf(" %c", &ch);
			scanf(" %d", &bt);
			robot[k] = ch;
			button[k] = bt;
		}

		Aout[i] = search();
	}

	for(i=0;i<T;i++) {

		printf("Case #%d: %d\n",i+1,Aout[i]);
	}

	return;
}