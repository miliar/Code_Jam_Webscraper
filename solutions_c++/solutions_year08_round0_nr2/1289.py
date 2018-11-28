#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
#include<vector>
#include<map>
#include<algorithm>
#include<string>
struct node
{
	int time;
	char station;
	int type;
};
int cmp(const void * p1, const void * p2)
{
	node t1 = *((node *)p1);
	node t2 = *((node *)p2);
	if(t1.time < t2.time)
		return -1;
	else if(t1.time == t2.time)
	{
		if(t1.type > t2.type)
			return -1;
		else if(t1.type == t2.type)
			return 0;
		else
			return 1;
	}
	else
		return 1;
}
node a[1000];
int main()
{
	int n;
	int i;
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );
	scanf("%d", &n);
	for(i = 0; i < n; i++)
	{
		int na, nb;
		int time;
		scanf("%d", &time);
		scanf("%d%d", &na,&nb);
		int j;
		int num = 0;
		for(j = 0; j < na; j++)
		{
			int h, m;
			scanf("%d:%d", &h, &m);
			node t; 
			t.station = 0;
			t.time = h * 60 + m;
			t.type = 0;
			a[num++] = t;
			scanf("%d:%d", &h, &m); 
			t.station = 1;
			t.time = h * 60 + m + time;
			t.type = 1;
			a[num++] = t;
		}
		for(j = 0; j < nb; j++)
		{
			int h, m;
			scanf("%d:%d", &h, &m);
			node t; 
			t.station = 1;
			t.time = h * 60 + m;
			t.type = 0;
			a[num++] = t;
			scanf("%d:%d", &h, &m); 
			t.station = 0;
			t.time = h * 60 + m + time;
			t.type = 1;
			a[num++] = t;
		}
		qsort(a, num, sizeof(node), cmp);
		int num1[2] = {0};
		int cur[2] = {0};
		for(j = 0; j < num; j++)
		{
			if(a[j].type == 0)
			{
				if(cur[a[j].station] == 0)
					num1[a[j].station]++;
				else
					cur[a[j].station]--;
			}
			else
				cur[a[j].station]++;
		}
		printf("Case #%d: %d %d\n", i + 1, num1[0], num1[1]);
	}	
}