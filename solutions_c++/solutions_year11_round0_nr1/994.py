#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

const int maxn = 100;
char robot[maxn];
int locations[maxn];
int n;

void read() {
	char blank;
	scanf("%d", &n);
//	printf("\ntotal positions in case: %d\n",n);
	for (int i=0; i<n; i++)
	{
		scanf("%c", &blank);
		scanf("%c", &robot[i]);
		scanf("%d", &locations[i]);
		
//printf("\ni: %d, robot:%c, locations:%d\n",i,robot[i],locations[i]);
	}	
}

int getNextPos(char r, int cur)
{
	while(cur<n)
	{
		if(robot[cur]==r)
			return locations[cur];
		cur++;
	}
	return -1;
}

int main()
{
	int i,t,k;
	int time;
	int posO, posB, nextPos;
	char nextToPress;
	int pressed;
	scanf("%d", &t);
	for(i = 1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		read();
		posO=1;
		posB=1;
		time=0;
		pressed=0;
		while(pressed<n)
		{
			nextToPress=robot[pressed];
			if(nextToPress=='O')
			{
				if(posO==locations[pressed])
					pressed++;
				else if(posO<locations[pressed])
					posO++;
				else if(posO>locations[pressed])
					posO--;
				nextPos = getNextPos('B',pressed);
				if(nextPos>0)
				{
					if(posB<nextPos)
						posB++;
					if(posB>nextPos)
						posB--;
				}
			}
			else
			{
				if(posB==locations[pressed])
					pressed++;
				else if(posB<locations[pressed])
					posB++;
				else if(posB>locations[pressed])
					posB--;
				nextPos = getNextPos('O',pressed);
				if(nextPos>0)
				{
					if(posO<nextPos)
						posO++;
					if(posO>nextPos)
						posO--;
				}
			}
			time++;
//printf("time:%d, posO:%d, posB:%d,pressed:%d \n",time,posO,posB,pressed);
		}
		printf("%d",time);
		printf("\n");
	}
	return 0;
}
