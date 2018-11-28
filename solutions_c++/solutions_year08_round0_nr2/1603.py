#include<stdio.h>
#include<limits.h>
#include<string.h>
#include<stdlib.h>
#include<queue>

//#define DEBUG

using namespace std;

struct action
{
	int time;
	bool isstart;
	bool startisa;
};

static int comp(const void *p1, const void *p2)
{
	if(((action*)p1)->time < ((action*)p2)->time)
	{
		return -1;
	}

	if(((action*)p1)->time == ((action*)p2)->time)
	{
		if(((action*)p1)->isstart == false)
			return -1;
		else
			return 1;
	}

	return 1;
}

int n;
int t;
int anza, anzb;
action actions[400];

int tanza = 0;
int tanzb = 0;
int bufa = 0;
queue<int> bufatimes;
int bufb = 0;
queue<int> bufbtimes;

int gettime(int h, int m)
{
	return h*60+m;
}

void readdata()
{
	int i,sh,sm,ah,am;
	scanf("%d%d%d", &t, &anza, &anzb);
	for(i=0; i<anza; i++)
	{
		scanf("%d:%d %d:%d\n", &sh,&sm,&ah,&am);
		actions[i*2].time = gettime(sh,sm);
		actions[i*2].isstart = true;
		actions[i*2].startisa = true;
		
		actions[i*2+1].time = gettime(ah,am);
		actions[i*2+1].isstart = false;
		actions[i*2+1].startisa = true;
	}

	for(; i<anza+anzb; i++)
	{
		scanf("%d:%d %d:%d\n", &sh,&sm,&ah,&am);
		actions[i*2].time = gettime(sh,sm);
		actions[i*2].isstart = true;
		actions[i*2].startisa = false;

		actions[i*2+1].time = gettime(ah,am);
		actions[i*2+1].isstart = false;
		actions[i*2+1].startisa = false;
	}
}

void calc()
{
	int i,j,k;

	for(i=0; i<2*(anza+anzb); i++)
	{
		// for each action
		if(actions[i].isstart)
		{
			// train starts
			if(actions[i].startisa)
			{
				// starts in a
				if(bufa && bufatimes.front()<=actions[i].time)
				{
#ifdef DEBUG
					printf("train starts in station A at %d from buffer\n", actions[i].time);
#endif
					--bufa;
					bufatimes.pop();
				}
				else
				{
#ifdef DEBUG
					printf("new train starts in station A at %d from buffer\n", actions[i].time);
#endif
					++tanza;
				}
			}
			else
			{
				// starts in b
				if(bufb && bufbtimes.front()<=actions[i].time)
				{
#ifdef DEBUG
					printf("train starts in station B from buffer at %d\n", actions[i].time);
#endif
					--bufb;
					bufbtimes.pop();
				}
				else
				{
#ifdef DEBUG
					printf("new train starts in station B at %d\n", actions[i].time);
#endif
					++tanzb;
				}
			}
		}
		else
		{
			// train arives
			if(actions[i].startisa)
			{
				// arives in b
#ifdef DEBUG
				printf("train arrived in station B at %d\n", actions[i].time);
#endif
				bufb++;
				bufbtimes.push(actions[i].time+t);
			}
			else
			{
				// arives in a
#ifdef DEBUG
				printf("trin arrives in station A at %d\n", actions[i].time);
#endif
				bufa++;
				bufatimes.push(actions[i].time+t);
			}
		}
	}
}

int main()
{
	int i,j,k;
	scanf("%d", &n);

	for(i=0; i<n; i++)
	{
		readdata();
		qsort(actions, 2*(anza+anzb), sizeof(action), comp);
		calc();
		printf("Case #%d: %d %d\n", i+1, tanza, tanzb);

		// reset values
		while(!bufatimes.empty())
			bufatimes.pop();
		while(!bufbtimes.empty())
			bufbtimes.pop();
		tanza = 0;
		tanzb = 0;
		bufa = 0;
		bufb = 0;
	}

	return 0;
}
