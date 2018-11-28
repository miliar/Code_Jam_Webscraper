#include<iostream>
#include<stdio.h>
#include<queue>
using namespace std;

queue<int> que;
queue<int> que_o;
queue<int> que_b;
char PUSH;

struct robots
{
	int cur;
	int next;
};
robots robots_o,robots_b;

void do_o()
{
	robots_o.next = que_o.front();

	if(PUSH == 'O')
	{
		if(que.front() == robots_o.cur)
		{que.pop(),que_o.pop();return;}
		if(que.front() > robots_o.cur)
		{robots_o.cur ++;return;}
		if(que.front() < robots_o.cur)
		{robots_o.cur --;return;}
	}
	else
	{
		if(robots_o.next == robots_o.cur)
			return;
		else
		{
			if(robots_o.next > robots_o.cur)
			{robots_o.cur ++;return;}
			if(robots_o.next < robots_o.cur)
			{robots_o.cur --;return;}
		}
	}

	return;
}

void do_b()
{
	robots_b.next = que_b.front();

	if(PUSH == 'B')
	{
		if(-que.front() == robots_b.cur)
		{que.pop(),que_b.pop();return;}
		if(-que.front() > robots_b.cur)
		{robots_b.cur ++;return;}
		if(-que.front() < robots_b.cur)
		{robots_b.cur --;return;}
	}
	else
	{
		if(robots_b.next == robots_b.cur)
			return;
		else
		{
			if(robots_b.next > robots_b.cur)
			{robots_b.cur ++;return;}
			if(robots_b.next < robots_b.cur)
			{robots_b.cur --;return;}
		}
	}

	return;
}

int main()
{
	
	FILE *fp = fopen("A-large.in","r");
	FILE *fpw = fopen("A-large.out","w");
	int T,N;

	
	

	fscanf(fp, "%d", &T);
	for(int i = 1; i <= T; i ++)
	{
		fscanf(fp, "%d", &N);
		char test;
		int number;
		
		
		robots_o.cur = 1;
		robots_b.cur = 1;

		for(int j = 0; j < N; j ++)
		{
			fscanf(fp, "%c", &test);
			fscanf(fp, "%c", &test);
			fscanf(fp, "%d", &number);
			if(test == 'O')
			{				
				que.push(number);
				que_o.push(number);
			}
			else
			{
				que.push(-number);
				que_b.push(number);
			}
		}

		//robots_o.next = que_o.front();
		
		int time = 0;
		while(!(que.empty()))
		{
			if(que.front() > 0)
			{
				PUSH = 'O';
			}
			else
			{
				PUSH = 'B';
			}
			if(que_o.empty() == 0)
				do_o();
			if(que_b.empty() == 0)
				do_b();

			time ++;
		}
		fprintf(fpw, "Case #%d: %d\n", i, time);
		cout<<time<<endl;
	}	

	return 0;

}

